# OCI Website Deployment Guide: GitHub Actions, Docker, Kubernetes (Always Free Tier)

This guide will walk you through deploying your web application to Oracle Cloud Infrastructure (OCI) using containerization with Docker, orchestration with Kubernetes (OKE), and automated CI/CD with GitHub Actions. The focus will be on leveraging OCI's "Always Free" tier resources to minimize costs.

## I. Introduction & Prerequisites

### A. What You'll Achieve
By following this guide, you will:
*   Host your web application on a scalable Kubernetes cluster in OCI.
*   Automate your deployment process using GitHub Actions, from code push to live updates.
*   Secure your website with a custom domain and SSL/TLS.
*   Utilize OCI's "Always Free" resources to keep your operational costs minimal.

### B. Always Free Tier Considerations (as of November 2026)
Oracle Cloud Infrastructure offers a generous "Always Free" tier, which is crucial for running your website without incurring significant costs. Here are the key resources we'll be relying on:

*   **Compute:**
    *   **Ampere A1 Compute (ARM-based):** Up to 4 OCPUs and 24 GB of memory. This is highly flexible; you can allocate these resources to one powerful instance or spread them across multiple smaller instances. These instances are excellent for running Kubernetes worker nodes or even a standalone VM for simpler deployments.
    *   **AMD Epyc Compute (x86-based):** 2 OCPUs and 15 GB of memory (limited to micro instances). Less flexible than Ampere A1 but still useful.
*   **Storage:**
    *   **Block Volume:** Up to 2 Block Volumes, each up to 200 GB. This is suitable for persistent storage needs for your applications.
    *   **Object Storage:** 10 GB (Standard).
*   **Networking:**
    *   **Egress Data Transfer:** Up to 10 TB per month, which is ample for most small to medium websites.
    *   **Load Balancer:** One flexible load balancer with 10 Mbps bandwidth.
*   **Oracle Kubernetes Engine (OKE):**
    *   **Control Plane:** The OKE control plane itself is generally free for the first 3000 OCPU-hours per month per tenancy. For small clusters with Always Free worker nodes, you can often run OKE without control plane costs.
    *   **Worker Nodes:** These will consume your Always Free Compute resources (e.g., Ampere A1 instances). Careful sizing is essential to stay within the free limits.
*   **Container Registry (OCIR):** Free for storing a reasonable number of Docker images.
*   **Database:** Oracle Autonomous Database (shared) with 2 OCPUs and 20 GB storage is available, but this guide will focus on compute and orchestration; database setup will be a separate consideration.

**Key Strategy for "Always Free":** Leverage the Ampere A1 compute instances for your OKE worker nodes. Carefully monitor your resource usage to avoid exceeding the free tier limits, especially for compute OCPU-hours and storage.

### C. Prerequisites
Before you begin, ensure you have the following:
*   **Oracle Cloud Infrastructure (OCI) Account:** Signed up for the "Always Free" tier.
*   **GitHub Account:** To host your application code and manage CI/CD workflows.
*   **Registered Domain Name:** A domain you own and have access to manage its DNS records.
*   **Basic Knowledge:** Familiarity with Docker, Kubernetes concepts, and Git.
*   **OCI CLI & kubectl:** (Optional, but recommended for local management) Installed and configured on your local machine.

## II. Oracle Cloud Infrastructure (OCI) Setup

### A. Sign Up for OCI Free Tier
1.  Navigate to the [Oracle Cloud Free Tier page](https://www.oracle.com/cloud/free/) and sign up for a new account. You will need a credit card for verification, but you won't be charged unless you explicitly upgrade to a paid account.
2.  Complete the sign-up process and log in to your OCI Console.

### B. Create a Compartment
Compartments help organize your cloud resources. It's good practice to create one for your project.
1.  In the OCI Console, open the navigation menu (hamburger icon) and go to **Identity & Security > Compartments**.
2.  Click **Create Compartment**.
3.  Enter a **Name** (e.g., `my-website-project`), an optional **Description**, and select the **Parent Compartment** (usually your root tenancy).
4.  Click **Create Compartment**.

### C. Create a Virtual Cloud Network (VCN)
A VCN is a customizable, private network in OCI that functions much like a traditional network with firewalls and routing tables.
1.  From the navigation menu, go to **Networking > Virtual Cloud Networks**.
2.  Select the **Compartment** you created.
3.  Click **Create VCN**.
4.  Choose **CREATE VCN WITH INTERNET CONNECTIVITY** (this option automatically sets up an Internet Gateway, NAT Gateway, and Service Gateway).
5.  Enter a **Name** (e.g., `my-website-vcn`), choose your **Compartment**, and leave other settings as default for a simple setup.
6.  Click **Create VCN**.

### D. Set Up Security Lists / Network Security Groups
These act as virtual firewalls to control ingress (inbound) and egress (outbound) traffic.

**Option 1: Security List (for simpler setups)**
When you create a VCN with internet connectivity, a default security list is created. We will modify it.
1.  In your VCN details, click **Security Lists**.
2.  Click on the **Default Security List**.
3.  **Add Ingress Rules:**
    *   Allow HTTP (port 80): Source CIDR `0.0.0.0/0`, IP Protocol `TCP`, Destination Port Range `80`.
    *   Allow HTTPS (port 443): Source CIDR `0.0.0.0/0`, IP Protocol `TCP`, Destination Port Range `443`.
    *   (Optional, for SSH access if you create a VM directly): Source CIDR `0.0.0.0/0` (or your IP range), IP Protocol `TCP`, Destination Port Range `22`.
4.  Leave the default Egress Rules (allowing all outbound traffic) for now.

**Option 2: Network Security Groups (NSG) (recommended for OKE)**
For Kubernetes, NSGs offer more granular control by associating security rules directly with specific resources (like OKE nodes or load balancers) rather than entire subnets. You will typically configure these when creating your OKE cluster and related resources.

### E. Set up Container Registry (OCIR)
OCIR is where your Docker images will be stored.
1.  From the navigation menu, go to **Developer Services > Container Registry**.
2.  Note your tenancy's registry URL (e.g., `fra.ocir.io/your_tenancy_namespace`). You'll need this later.
3.  **Create an Auth Token:** This is required for Docker login from GitHub Actions.
    *   Click the **User icon** (top right) and then **User Settings**.
    *   Go to **Auth Tokens**.
    *   Click **Generate Token**.
    *   Provide a **Description** (e.g., `github-actions-ocir`).
    *   Copy the generated token immediately and securely save it. You will NOT be able to see it again.

### F. Create an Oracle Kubernetes Engine (OKE) Cluster
This is where your application containers will run.
1.  From the navigation menu, go to **Developer Services > Kubernetes Clusters (OKE)**.
2.  Select your **Compartment**.
3.  Click **Create Cluster**.
4.  Choose **Quick Create** for simplicity.
5.  **Configure Cluster:**
    *   **Name:** `my-website-cluster`
    *   **Kubernetes Version:** Select the latest stable version.
    *   **Shape:** For Always Free, select an **Ampere A1 (ARM)** shape (e.g., `VM.Standard.A1.Flex`). Set the **Number of OCPUs** and **Memory (GB)** to stay within your Always Free limits (e.g., 4 OCPUs, 24GB Memory total across all nodes, or smaller if you need multiple worker nodes. A single 4 OCPU, 24GB node is a good start).
    *   **Number of Nodes:** Start with `1` to stay within free tier easily. You can scale up later if needed.
    *   **Public IP Address:** Ensure this is enabled for your worker nodes if you need direct external access, or rely on a Load Balancer for public access.
    *   **VCN:** Select the VCN you created earlier.
    *   **Subnets:** Oracle will create new subnets for you. Ensure they are public if you need ingress from the internet.
6.  Review and click **Create Cluster**.
    *   **Important:** The OKE control plane is free up to 3000 OCPU-hours/month. Your worker nodes will consume your Always Free compute resources (e.g., the 4 OCPU/24GB A1 Flex instance). Configure carefully to stay within these limits.

### G. Configure `kubectl` Access (from OCI Console)
Once your OKE cluster is provisioned:
1.  Click on your newly created OKE cluster.
2.  Click **Access Kubeconfig**.
3.  Follow the instructions to generate and download your `kubeconfig` file. It will typically involve running an OCI CLI command.
    *   Save this file to `~/.kube/config` on your local machine. This allows your local `kubectl` to interact with your OKE cluster.
    *   Test your connection: `kubectl get nodes` should show your OKE worker node(s).

## III. Application Preparation (Local)

### A. Dockerize Your Application
Your application needs a `Dockerfile` to be packaged into a Docker image. Here's a generic example:

```dockerfile
# Use a lightweight base image suitable for your application
# Example for a Node.js app
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker cache
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of your application code
COPY . .

# Expose the port your application listens on
EXPOSE 8080

# Command to run your application
CMD ["npm", "start"]

# --- OR --- 

# Example for a Python Flask app
# FROM python:3.9-slim-buster

# WORKDIR /app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5000

# CMD ["python", "app.py"]
```

*   Replace the example content with your application's specific needs.
*   Ensure your application listens on the port specified in `EXPOSE`.

### B. Build and Test Docker Image Locally
1.  Open your terminal in your application's root directory (where `Dockerfile` is located).
2.  Build the Docker image:
    ```bash
    docker build -t my-website-app:latest .
    ```
3.  Run the container locally to test:
    ```bash
    docker run -p 8080:8080 my-website-app:latest
    ```
    (Adjust ports if your app uses a different one).
4.  Access your application in your browser at `http://localhost:8080`.

## IV. GitHub Repository Setup

### A. Create a GitHub Repository
1.  Create a new public or private repository on GitHub (e.g., `my-website-repo`).
2.  Push your application code, including the `Dockerfile`, to this repository.

### B. Store OCI Credentials Securely in GitHub Secrets
GitHub Actions needs OCI credentials to push Docker images to OCIR and deploy to OKE. **Never hardcode credentials in your workflow files.** Use GitHub Secrets.

1.  In your GitHub repository, go to **Settings > Secrets and variables > Actions**.
2.  Click **New repository secret** and add the following:
    *   **`OCI_REGION`**: Your OCI region identifier (e.g., `us-ashburn-1` or `eu-frankfurt-1`).
    *   **`OCIR_USERNAME`**: Your OCI username (typically in the format `your_tenancy_namespace/your_username`).
    *   **`OCIR_PASSWORD`**: The Auth Token you generated in OCIR setup (starting with `ocid1.authtoken...`).
    *   **`OCI_KUBECONFIG_CONTENT`**: The content of your `kubeconfig` file (the YAML text). Copy the entire content of the `kubeconfig` file you downloaded from OCI and paste it here. **Ensure this is handled carefully as it grants cluster access.**

## V. GitHub Actions Workflow

Create a file named `deploy.yml` inside the `.github/workflows/` directory in your GitHub repository. This file defines your CI/CD pipeline.

```yaml
name: Deploy to OCI OKE

on:
  push:
    branches:
      - main # or master, or your main development branch
  workflow_dispatch: # Allows manual triggering

env:
  OCIR_REPO: ${{ secrets.OCI_REGION }}.ocir.io/your_tenancy_namespace/my-website-app # Adjust tenancy namespace and image name
  IMAGE_TAG: ${{ github.sha }} # Use Git SHA as image tag for uniqueness
  KUBECONFIG_PATH: /tmp/kubeconfig # Temporary path for kubeconfig inside runner

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker BuildX
        uses: docker/setup-buildx-action@v2

      - name: Login to OCIR
        uses: docker/login-action@v2
        with:
          registry: ${{ secrets.OCI_REGION }}.ocir.io
          username: ${{ secrets.OCIR_USERNAME }}
          password: ${{ secrets.OCIR_PASSWORD }}

      - name: Build and push Docker image to OCIR
        run: |
          docker build -t $OCIR_REPO:$IMAGE_TAG -f Dockerfile .
          docker push $OCIR_REPO:$IMAGE_TAG

      - name: Create Kubeconfig file
        run: |
          mkdir -p ~/.kube
          echo "${{ secrets.OCI_KUBECONFIG_CONTENT }}" > ${{ env.KUBECONFIG_PATH }}
          chmod 600 ${{ env.KUBECONFIG_PATH }}

      - name: Set KUBECONFIG environment variable
        run: echo "KUBECONFIG=${{ env.KUBECONFIG_PATH }}" >> $GITHUB_ENV

      - name: Install kubectl
        uses: azure/setup-kubectl@v3

      - name: Update Kubernetes Deployment
        run: |
          # Set current context to your OKE cluster (if not already set by kubeconfig)
          kubectl config use-context my-website-cluster-context # Replace with your actual context name if different
          # Update the image tag in your deployment manifest
          # This assumes your k8s deployment.yaml is in a `k8s` directory
          sed -i "s|image: .*/my-website-app:.*|image: ${OCIR_REPO}:${IMAGE_TAG}|g" k8s/deployment.yaml
          # Apply the updated deployment to OKE
          kubectl apply -f k8s/
        env:
          KUBECONFIG: ${{ env.KUBECONFIG_PATH }}
```

*   **Remember to update:**
    *   `main` branch name if yours is different.
    *   `your_tenancy_namespace` in `OCIR_REPO`.
    *   `my-website-cluster-context` with the correct context name from your `kubeconfig` file (you can find this by running `kubectl config get-contexts` locally).
    *   The `sed` command to match your exact image name and path in `deployment.yaml`.

## VI. Kubernetes Deployment

Your application needs Kubernetes manifest files to define how it should be deployed and exposed.

Create a directory named `k8s` in your GitHub repository.

### A. Deployment Manifest (`k8s/deployment.yaml`)
This file describes your application's deployment, including the Docker image, replicas, and resource requests.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-website-deployment
  labels:
    app: my-website-app
spec:
  replicas: 1 # Start with 1 replica for Always Free tier
  selector:
    matchLabels:
      app: my-website-app
  template:
    metadata:
      labels:
        app: my-website-app
    spec:
      containers:
      - name: my-website-container
        image: ${{ secrets.OCI_REGION }}.ocir.io/your_tenancy_namespace/my-website-app:latest # Initial image, will be replaced by GitHub Actions
        ports:
        - containerPort: 8080 # Port your application listens on
        resources:
          requests:
            cpu: "250m" # Request 0.25 CPU core
            memory: "512Mi" # Request 512 MB memory
          limits:
            cpu: "500m" # Limit to 0.5 CPU core
            memory: "1Gi" # Limit to 1 GB memory
```

*   **Adjust:**
    *   `replicas`: Keep at `1` to stay within Always Free compute limits.
    *   `image`: Set a placeholder. GitHub Actions will update the tag.
    *   `containerPort`: Match the `EXPOSE` port from your `Dockerfile`.
    *   `resources`: Adjust `cpu` and `memory` requests/limits based on your application's needs and your Always Free compute allocation.

### B. Service Manifest (`k8s/service.yaml`)
This file defines how to access your application. For external access, we'll use a `LoadBalancer` type service, which OCI will provision an OCI Load Balancer for.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-website-service
  labels:
    app: my-website-app
spec:
  selector:
    app: my-website-app
  type: LoadBalancer # OCI will provision a Load Balancer
  ports:
    - protocol: TCP
      port: 80 # External port for HTTP traffic
      targetPort: 8080 # Internal container port
      name: http
```

*   **Adjust:**
    *   `targetPort`: Match your application's listening port.
    *   `port`: You can add `port: 443` and `targetPort: 8080` (or `443` if your app handles SSL) for HTTPS directly here, but managing SSL at the Load Balancer is often simpler.

### C. Ingress Controller (Optional, for advanced routing/SSL management)
While a LoadBalancer service works, for more advanced routing rules, path-based routing, or centralized SSL management, an Ingress Controller (like Nginx Ingress Controller) is common.

**Always Free Considerations:** Deploying an Ingress Controller *itself* will consume resources on your OKE worker nodes. An Ingress Controller typically needs an OCI Load Balancer to expose it to the internet, which is covered by the Always Free tier's 10 Mbps Load Balancer.

For simplicity and to stick to Always Free, the `LoadBalancer` service directly exposing your app (as shown above) is sufficient for most cases.

If you choose to use an Ingress Controller:
1.  Deploy an Ingress Controller to your cluster (e.g., using Helm).
    ```bash
    helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
    helm repo update
    helm install nginx-ingress ingress-nginx/ingress-nginx \
      --namespace ingress-nginx --create-namespace \
      --set controller.service.type=LoadBalancer
    ```
2.  Create an Ingress resource (`k8s/ingress.yaml`):
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-website-ingress
      annotations:
        kubernetes.io/ingress.class: "nginx"
        # Add OCI specific annotations if needed, consult OKE documentation
    spec:
      rules:
      - host: your.custom.domain # Replace with your actual domain
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-website-service # Name of your Kubernetes Service
                port:
                  number: 80 # Port of your Kubernetes Service
    ```

### D. Apply Kubernetes Manifests
1.  **Initial Manual Deployment:** Push your `k8s` directory to your GitHub repository.
2.  **Trigger GitHub Actions:** Your workflow will automatically run on `push` to the `main` branch. You can also manually trigger it from the GitHub Actions tab by clicking "Run workflow".
3.  Monitor the GitHub Actions run. Once it succeeds, your application should be deployed to OKE.
4.  **Get Load Balancer IP:**
    ```bash
    kubectl get service my-website-service
    ```
    Look for the `EXTERNAL-IP` of your `my-website-service`. This is the public IP address of the OCI Load Balancer created for your service.

## VII. Custom Domain Configuration

### A. Get OCI Load Balancer / Service IP
As mentioned in the previous step, use `kubectl get service my-website-service` to retrieve the `EXTERNAL-IP` of your Kubernetes LoadBalancer service.

### B. Configure DNS Records
Now you need to point your custom domain to the OCI Load Balancer's IP address.
1.  Go to your domain registrar (e.g., GoDaddy, Namecheap, Cloudflare, etc.).
2.  Navigate to the DNS management section for your domain.
3.  Create or update an **A record**:
    *   **Type:** `A`
    *   **Host/Name:** `@` (for your root domain, e.g., `example.com`) or `www` (for `www.example.com`). You might need both.
    *   **Value/Points to:** The `EXTERNAL-IP` of your OCI Load Balancer.
    *   **TTL (Time To Live):** Set to a lower value (e.g., 300 seconds or 5 minutes) initially for faster propagation during testing. Increase it later.
4.  Save the changes. DNS propagation can take some time (minutes to hours).

### C. SSL/TLS Certificate (HTTPS)
HTTPS is crucial for security. You have a few "Always Free"-friendly options:

**Option 1: OCI Load Balancer SSL (Recommended for simplicity)**
OCI Load Balancers can terminate SSL/TLS traffic, simplifying certificate management for your Kubernetes application.
1.  In the OCI Console, go to **Networking > Load Balancers**.
2.  Find the Load Balancer provisioned for your `my-website-service`.
3.  **Add a Listener:**
    *   Add a listener for HTTPS on port `443`.
    *   For **Certificate**, you can upload your own SSL certificate (if you have one) or generate a free one using services like Let's Encrypt manually and then upload it here. You can also use OCI Certificate Service for managing certificates.
    *   Select your backend set (which points to your OKE service).

**Option 2: Let's Encrypt with Cert-Manager (if using Ingress Controller)**
If you chose to deploy an Ingress Controller, Cert-Manager can automate the provisioning and renewal of Let's Encrypt certificates directly within your Kubernetes cluster.
1.  Install Cert-Manager in your OKE cluster using Helm.
    ```bash
    helm repo add jetstack https://charts.jetstack.io
    helm repo update
    helm install cert-manager jetstack/cert-manager \
      --namespace cert-manager --create-namespace \
      --version v1.10.0 # Check for latest compatible version
      --set installCRDs=true
    ```
2.  Create a `ClusterIssuer` (or `Issuer`) resource to configure Cert-Manager to use Let's Encrypt.
3.  Update your Ingress resource (`k8s/ingress.yaml`) to request a certificate from Cert-Manager:
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-website-ingress
      annotations:
        kubernetes.io/ingress.class: "nginx"
        cert-manager.io/cluster-issuer: "letsencrypt-prod" # Name of your ClusterIssuer
    spec:
      tls:
      - hosts:
        - your.custom.domain
        secretName: my-website-tls # Kubernetes Secret to store the certificate
      rules:
      - host: your.custom.domain
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-website-service
                port:
                  number: 80
    ```

**Testing SSL:** Once configured, access your domain using `https://your.custom.domain`.

## VIII. Monitoring & Maintenance

### A. OCI Monitoring
*   OCI provides built-in monitoring for your compute instances, load balancers, and OKE clusters. Access it via the OCI Console under **Monitoring**.
*   Set up alarms for CPU/memory usage on your OKE worker nodes to ensure you stay within Always Free limits.

### B. OKE Updates
*   Regularly check for new Kubernetes versions and apply updates to your OKE cluster for security and new features. You can do this via the OCI Console or OCI CLI.

This guide provides a robust and cost-effective way to deploy your website on OCI. Remember to adjust resource requests and limits according to your application's actual needs and OCI's "Always Free" tier specifications. Enjoy your deployed website!