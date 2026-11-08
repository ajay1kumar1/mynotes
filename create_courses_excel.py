import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

wb = openpyxl.Workbook()

# Style definitions
header_font = Font(name='Arial', bold=True, size=11, color='FFFFFF')
header_fill = PatternFill(start_color='2F5496', end_color='2F5496', fill_type='solid')
subheader_fill = PatternFill(start_color='D6E4F0', end_color='D6E4F0', fill_type='solid')
subheader_font = Font(name='Arial', bold=True, size=11, color='2F5496')
normal_font = Font(name='Arial', size=10)
link_font = Font(name='Arial', size=10, color='0563C1', underline='single')
priority_fill = PatternFill(start_color='FFF2CC', end_color='FFF2CC', fill_type='solid')
thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)
wrap_align = Alignment(wrap_text=True, vertical='top')
center_align = Alignment(horizontal='center', vertical='top', wrap_text=True)

# Course data
courses = [
    # Generative AI & AI Architecture
    {"category": "Generative AI & AI Architecture", "priority": "HIGH", "num": 1, "title": "Generative AI for Enterprise: Architecture, Governance & Scale", "instructor": "Kumaran Ponnambalam", "duration": "12 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/generative-ai-enterprise-architecture-governance/", "topics": "ISO 42001, NIST AI RMF, AI governance boards, responsible AI, multi-region deployment, cost optimization"},
    {"category": "Generative AI & AI Architecture", "priority": "HIGH", "num": 2, "title": "Building LLM Applications for Production", "instructor": "Huyen Chip", "duration": "15 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/building-llm-applications-production/", "topics": "LLM evaluation (RAGAS), guardrails, observability, A/B testing, cost management, latency optimization"},
    {"category": "Generative AI & AI Architecture", "priority": "HIGH", "num": 3, "title": "Enterprise AI Strategy & Architecture Masterclass", "instructor": "Daniel Bourke", "duration": "18 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/enterprise-ai-strategy-architecture/", "topics": "ADR framework, architecture review boards, build vs buy, vendor evaluation, ROI modeling"},
    {"category": "Generative AI & AI Architecture", "priority": "HIGH", "num": 4, "title": "Designing Generative AI Systems: From Prototype to Production", "instructor": "Venelin Valkov", "duration": "14 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/designing-generative-ai-systems/", "topics": "LiteLLM gateway, semantic caching, rate limiting, fallback chains, token metering, multi-region"},
    {"category": "Generative AI & AI Architecture", "priority": "HIGH", "num": 5, "title": "AI Agent Architecture: Multi-Agent Systems with LangGraph & AutoGen", "instructor": "Nirant Kasliwal", "duration": "16 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/ai-agent-architecture-multi-agent/", "topics": "Multi-agent patterns, human-in-the-loop, agent evaluation, MCP integration, deployment"},

    # RAG, LangChain, LangGraph & Agentic Systems
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 6, "title": "Complete RAG Masterclass: Basic to Advanced (2024-2025)", "instructor": "Paulo Dichone", "duration": "20 hrs", "level": "Beginner-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/complete-rag-masterclass/", "topics": "Naive RAG → Advanced RAG → Hybrid → GraphRAG → Multimodal RAG, evaluation with RAGAS"},
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 7, "title": "LangChain & LangGraph: Build Production-Grade LLM Apps", "instructor": "Eden Marco", "duration": "18 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/langchain-langgraph-production/", "topics": "Chains, agents, memory, tools, streaming, human-in-loop, LangSmith observability, deployment"},
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 8, "title": "Advanced RAG Techniques: GraphRAG, Multimodal & Agentic RAG", "instructor": "Greg Kamradt", "duration": "12 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/advanced-rag-techniques/", "topics": "Knowledge graphs, entity extraction, multimodal embeddings, ColPali, agentic workflows"},
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 9, "title": "Building AI Agents with LangGraph, AutoGen & CrewAI", "instructor": "Alexandros Mouratidis", "duration": "14 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/building-ai-agents-langgraph-autogen/", "topics": "ReAct, plan-and-execute, reflection, multi-agent collaboration, tool calling, evaluation"},
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 10, "title": "LLM Evaluation & Observability: RAGAS, LangSmith, Arize", "instructor": "Aman Anand", "duration": "10 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/llm-evaluation-observability/", "topics": "RAGAS metrics, custom evaluators, LangSmith, Arize Phoenix, CI/CD gates, regression testing"},
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 11, "title": "MCP (Model Context Protocol) & AI Gateway Patterns", "instructor": "Sam Witteveen", "duration": "8 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/mcp-ai-gateway-patterns/", "topics": "MCP specification, server/client implementation, gateway patterns, rate limiting, audit logging"},
    {"category": "RAG, LangChain, LangGraph & Agentic Systems", "priority": "HIGH", "num": 12, "title": "Prompt Engineering Masterclass: Advanced Techniques for Production", "instructor": "Sunny Savita", "duration": "12 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/prompt-engineering-masterclass/", "topics": "Chain-of-thought, tree-of-thoughts, DSPy optimization, prompt versioning, CLAUDE.md patterns"},

    # AWS Solutions Architecture
    {"category": "AWS Solutions Architecture", "priority": "HIGH", "num": 13, "title": "Ultimate AWS Certified Solutions Architect Professional (SAP-C02)", "instructor": "Stephane Maarek", "duration": "35 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/aws-certified-solutions-architect-professional/", "topics": "SAP-C02 exam prep, advanced networking, migration, cost optimization, security, hybrid"},
    {"category": "AWS Solutions Architecture", "priority": "MEDIUM", "num": 14, "title": "AWS Certified Solutions Architect Associate (SAA-C03) - Complete", "instructor": "Stephane Maarek", "duration": "27 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/", "topics": "SAA-C03 exam prep, compute, storage, database, networking, security, monitoring"},
    {"category": "AWS Solutions Architecture", "priority": "HIGH", "num": 15, "title": "AWS Bedrock & Generative AI: Build Enterprise GenAI Apps", "instructor": "Frank Kane", "duration": "14 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/aws-bedrock-generative-ai/", "topics": "Bedrock models, KB with OpenSearch, Agents, Guardrails, prompt management, model evaluation"},
    {"category": "AWS Solutions Architecture", "priority": "MEDIUM", "num": 16, "title": "AWS SageMaker & MLOps: End-to-End ML Pipeline", "instructor": "Frank Kane", "duration": "16 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/aws-sagemaker-mlops/", "topics": "Pipelines, training, tuning, deployment, monitoring, drift detection, multi-account"},
    {"category": "AWS Solutions Architecture", "priority": "HIGH", "num": 17, "title": "Advanced AWS Architecture: Multi-Account, Landing Zone, Control Tower", "instructor": "Neal Davis", "duration": "18 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/advanced-aws-architecture/", "topics": "Multi-account strategy, Control Tower, IAM Identity Center, networking hub-spoke, security hub"},
    {"category": "AWS Solutions Architecture", "priority": "HIGH", "num": 18, "title": "AWS EKS Deep Dive: Production-Grade Kubernetes on AWS", "instructor": "Michael Levan", "duration": "20 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/aws-eks-deep-dive/", "topics": "EKS provisioning, managed node groups, Fargate, IRSA, VPC CNI, ALB controller, GitOps"},
    {"category": "AWS Solutions Architecture", "priority": "MEDIUM", "num": 19, "title": "AWS Step Functions & EventBridge: Serverless Orchestration", "instructor": "Stephane Maarek", "duration": "10 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/aws-step-functions/", "topics": "Standard/Express workflows, EventBridge pipes, scheduler, error handling, observability"},

    # Azure Solutions Architecture
    {"category": "Azure Solutions Architecture", "priority": "HIGH", "num": 20, "title": "AZ-305: Microsoft Azure Solutions Architect Expert - Complete", "instructor": "Scott Duffy", "duration": "30 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/az-305-azure-solutions-architect-expert/", "topics": "AZ-305 exam prep, governance, security, migration, identity, monitoring, cost"},
    {"category": "Azure Solutions Architecture", "priority": "MEDIUM", "num": 21, "title": "AZ-104: Microsoft Azure Administrator Associate - Complete", "instructor": "Scott Duffy", "duration": "25 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/az-104-azure-administrator/", "topics": "AZ-104 exam prep, compute, storage, networking, identity, governance, backup"},
    {"category": "Azure Solutions Architecture", "priority": "HIGH", "num": 22, "title": "Azure AI Foundry & OpenAI: Build Enterprise GenAI Applications", "instructor": "Frank Kane", "duration": "14 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/azure-ai-foundry-openai/", "topics": "AI Foundry hub/projects, model catalog, prompt flow, evaluation, content safety, deployment"},
    {"category": "Azure Solutions Architecture", "priority": "HIGH", "num": 23, "title": "Azure AKS Deep Dive: Production Kubernetes on Azure", "instructor": "Michael Levan", "duration": "18 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/azure-aks-deep-dive/", "topics": "AKS provisioning, managed identity, Azure CNI, policy, GitOps Flux/ArgoCD, monitoring"},
    {"category": "Azure Solutions Architecture", "priority": "MEDIUM", "num": 24, "title": "Azure Databricks & Data Engineering: Lakehouse Architecture", "instructor": "Adam Anderson", "duration": "16 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/azure-databricks-data-engineering/", "topics": "Medallion architecture, Unity Catalog, Delta Live Tables, MLflow, feature store"},
    {"category": "Azure Solutions Architecture", "priority": "MEDIUM", "num": 25, "title": "Azure DevOps & GitHub Actions: Enterprise CI/CD", "instructor": "Paul Hacker", "duration": "14 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/azure-devops-github-actions-enterprise/", "topics": "YAML pipelines, templates, environments, secret management, policy as code, deployment gates"},
    {"category": "Azure Solutions Architecture", "priority": "HIGH", "num": 26, "title": "Azure Landing Zones & Cloud Adoption Framework", "instructor": "John Savill", "duration": "12 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/azure-landing-zones-caf/", "topics": "Cloud Adoption Framework, landing zone accelerators, management groups, Azure Policy, Blueprints"},

    # DevOps: Docker, Kubernetes & CI/CD
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "HIGH", "num": 27, "title": "Docker Mastery: Complete Toolset - Docker, Compose, Swarm, Registry", "instructor": "Bret Fisher", "duration": "22 hrs", "level": "Beginner-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/docker-mastery/", "topics": "Dockerfile best practices, multi-stage, BuildKit, Compose v2, Swarm mode, security, registries"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "MEDIUM", "num": 28, "title": "Kubernetes for the Absolute Beginners - Hands-On", "instructor": "Mumshad Mannambeth", "duration": "12 hrs", "level": "Beginner", "hands_on": "Yes", "link": "https://www.udemy.com/course/kubernetes-for-the-absolute-beginners/", "topics": "Core concepts, architecture, kubectl, pods, deployments, services, ConfigMaps, Secrets"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "HIGH", "num": 29, "title": "Certified Kubernetes Administrator (CKA) - Complete Course", "instructor": "Mumshad Mannambeth", "duration": "25 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/certified-kubernetes-administrator-cka/", "topics": "CKA exam prep, cluster architecture, networking, storage, security, troubleshooting"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "HIGH", "num": 30, "title": "Certified Kubernetes Application Developer (CKAD) - Complete", "instructor": "Mumshad Mannambeth", "duration": "18 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/certified-kubernetes-application-developer/", "topics": "CKAD exam prep, core concepts, config, multi-container, observability, services"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "HIGH", "num": 31, "title": "Kubernetes the Hard Way: From Scratch to Production", "instructor": "Kelsey Hightower (adapted)", "duration": "20 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/kubernetes-the-hard-way/", "topics": "Bootstrap, TLS, kubeconfig, control plane, worker nodes, networking, addons, HA"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "MEDIUM", "num": 32, "title": "GitLab CI/CD: Complete Pipeline & DevOps Automation", "instructor": "Valentin Despa", "duration": "14 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/gitlab-cicd-complete/", "topics": "Pipeline architecture, templates, environments, SAST/DAST, dependency scanning, pages"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "MEDIUM", "num": 33, "title": "GitHub Actions: Complete CI/CD Pipeline & Automation", "instructor": "Valentin Despa", "duration": "12 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/github-actions-complete/", "topics": "Workflow syntax, actions, matrix, environments, OIDC, secret scanning, reusable workflows"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "LOW", "num": 34, "title": "Jenkins: Complete CI/CD Pipeline with Docker & Kubernetes", "instructor": "In28Minutes", "duration": "16 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/jenkins-complete-cicd-pipeline/", "topics": "Declarative pipelines, shared libraries, Kubernetes agents, Blue Ocean, promotion, audit"},
    {"category": "DevOps: Docker, Kubernetes & CI/CD", "priority": "HIGH", "num": 35, "title": "ArgoCD & GitOps: Continuous Delivery for Kubernetes", "instructor": "Ahmet Alp Balkan", "duration": "10 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/argocd-gitops-kubernetes/", "topics": "GitOps principles, ArgoCD architecture, application sets, sync waves, Rollouts, analysis"},

    # MLOps / LLMOps & AI Platform Engineering
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "HIGH", "num": 36, "title": "MLOps Fundamentals: CI/CD/CT for Machine Learning", "instructor": "Noah Gift", "duration": "16 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/mlops-fundamentals/", "topics": "CI/CD/CT, MLflow, Kubeflow, model versioning, A/B testing, data drift, concept drift"},
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "HIGH", "num": 37, "title": "LLMOps: Operationalizing Large Language Models", "instructor": "Chip Huyen", "duration": "14 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/llmops-operationalizing-llms/", "topics": "Prompt management, evaluation pipelines, guardrails, routing, caching, fine-tuning pipelines"},
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "HIGH", "num": 38, "title": "Kubeflow End-to-End: ML Pipelines on Kubernetes", "instructor": "Anish Divase", "duration": "18 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/kubeflow-end-to-end/", "topics": "Pipeline SDK, components, KServe inference, Katib tuning, Feast feature store, multi-user"},
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "MEDIUM", "num": 39, "title": "MLflow in Production: Model Registry, Tracking & Deployment", "instructor": "Javan Chan", "duration": "12 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/mlflow-in-production/", "topics": "Tracking API, model registry stages, model serving, Docker packaging, CI/CD integration"},
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "MEDIUM", "num": 40, "title": "Feature Engineering & Feature Store for ML Systems", "instructor": "Soledad Galli", "duration": "14 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/feature-engineering-feature-store/", "topics": "Feature engineering techniques, Feast offline/online store, feature pipelines, monitoring"},
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "MEDIUM", "num": 41, "title": "ML Model Monitoring & Observability: Evidently, WhyLogs, Arize", "instructor": "Emre Ozer", "duration": "10 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/ml-model-monitoring/", "topics": "Data drift, concept drift, target drift, Evidently AI, WhyLogs, Arize, alerting"},
    {"category": "MLOps / LLMOps & AI Platform Engineering", "priority": "HIGH", "num": 42, "title": "Building AI Platforms: Internal Developer Platforms for ML", "instructor": "Mauricio Salatino", "duration": "16 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/building-ai-platforms/", "topics": "IDP principles, Backstage, Crossplane, Kubernetes operators, self-service, golden paths"},

    # Infrastructure as Code
    {"category": "Infrastructure as Code (Terraform, Helm, ArgoCD)", "priority": "HIGH", "num": 43, "title": "Terraform for AWS: Beginner to Advanced (2024-2025)", "instructor": "Zeal Vora", "duration": "22 hrs", "level": "Beginner-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/terraform-for-aws/", "topics": "HCL, modules, workspaces, state backend, testing (Terratest), CI/CD, drift detection"},
    {"category": "Infrastructure as Code (Terraform, Helm, ArgoCD)", "priority": "HIGH", "num": 44, "title": "Terraform for Azure: Complete Infrastructure as Code", "instructor": "Scott Duffy", "duration": "18 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/terraform-for-azure/", "topics": "Azure provider, resource groups, networking, AKS, Databricks, CAF landing zones"},
    {"category": "Infrastructure as Code (Terraform, Helm, ArgoCD)", "priority": "MEDIUM", "num": 45, "title": "Helm & Kustomize: Kubernetes Package Management Mastery", "instructor": "Ahmet Alp Balkan", "duration": "10 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/helm-kustomize-kubernetes/", "topics": "Chart templates, values, dependencies, Kustomize bases/overlays, Helmfile, testing"},
    {"category": "Infrastructure as Code (Terraform, Helm, ArgoCD)", "priority": "HIGH", "num": 46, "title": "Infrastructure Testing: Terratest, Kitchen-Terraform, OPA", "instructor": "Anton Babenko", "duration": "12 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/infrastructure-testing/", "topics": "Terratest Go tests, Kitchen-Terraform, OPA/Rego policies, Checkov, tfsec, CI/CD gates"},
    {"category": "Infrastructure as Code (Terraform, Helm, ArgoCD)", "priority": "HIGH", "num": 47, "title": "Crossplane: Control Plane for Cloud-Native Infrastructure", "instructor": "Bassam Tabbara", "duration": "14 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/crossplane-cloud-native/", "topics": "Provider architecture, managed resources, compositions, XRDs, ArgoCD/Flux integration"},
    {"category": "Infrastructure as Code (Terraform, Helm, ArgoCD)", "priority": "HIGH", "num": 48, "title": "Policy as Code: OPA/Gatekeeper, Kyverno, CEL for Kubernetes", "instructor": "Torin Sandall", "duration": "10 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/policy-as-code-kubernetes/", "topics": "OPA Gatekeeper, Kyverno, CEL, constraint templates, audit, mutation, testing"},

    # AI Governance, Security & Responsible AI
    {"category": "AI Governance, Security & Responsible AI", "priority": "HIGH", "num": 49, "title": "ISO/IEC 42001: AI Management System Implementation", "instructor": "Adrian Resag", "duration": "12 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/iso-42001-ai-management-system/", "topics": "ISO 42001 clauses, AI risk assessment, Statement of Applicability, internal audit, certification"},
    {"category": "AI Governance, Security & Responsible AI", "priority": "HIGH", "num": 50, "title": "NIST AI Risk Management Framework (AI RMF) in Practice", "instructor": "Patrick Hall", "duration": "10 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/nist-ai-rmf-practice/", "topics": "AI RMF core, profiles, playbooks, measurement, risk tolerance, governance structures"},
    {"category": "AI Governance, Security & Responsible AI", "priority": "MEDIUM", "num": 51, "title": "Responsible AI: Bias Detection, Fairness & Explainability", "instructor": "Krish Naik", "duration": "14 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/responsible-ai-bias-fairness/", "topics": "Bias metrics, demographic parity, equalized odds, SHAP/LIME, counterfactual explanations"},
    {"category": "AI Governance, Security & Responsible AI", "priority": "HIGH", "num": 52, "title": "AI Security & Privacy: PII Protection, Guardrails & Red Teaming", "instructor": "Joseph Thacker", "duration": "12 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/ai-security-privacy/", "topics": "PII detection/tokenization, NeMo Guardrails, Lakera, prompt injection, jailbreak testing"},
    {"category": "AI Governance, Security & Responsible AI", "priority": "MEDIUM", "num": 53, "title": "SOC 2, GDPR & PDPA Compliance for AI Systems", "instructor": "David Chapman", "duration": "10 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/soc2-gdpr-pdpa-ai-compliance/", "topics": "SOC 2 Type II, GDPR Art 25/32, PDPA, evidence automation, continuous compliance"},
    {"category": "AI Governance, Security & Responsible AI", "priority": "HIGH", "num": 54, "title": "AI Governance Platform: Building Guardrails, Audit & Policy Engine", "instructor": "Navin Patel", "duration": "14 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/ai-governance-platform/", "topics": "Policy-as-code, audit logging, automated evidence, dashboard, integration patterns"},

    # Data Engineering & Vector Databases
    {"category": "Data Engineering & Vector Databases", "priority": "HIGH", "num": 55, "title": "Vector Databases Masterclass: Pinecone, Weaviate, Qdrant, Chroma", "instructor": "James Briggs", "duration": "16 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/vector-databases-masterclass/", "topics": "Index types (HNSW, IVF), hybrid search, metadata filtering, multi-tenancy, benchmarking"},
    {"category": "Data Engineering & Vector Databases", "priority": "MEDIUM", "num": 56, "title": "OpenSearch & Elasticsearch: Search, Analytics & Vector Search", "instructor": "Frank Kane", "duration": "18 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/opensearch-elasticsearch-complete/", "topics": "Cluster architecture, k-NN plugin, hybrid search, ISM, security, performance tuning"},
    {"category": "Data Engineering & Vector Databases", "priority": "HIGH", "num": 57, "title": "Neo4j Graph Database & GraphRAG: Complete Guide", "instructor": "William Lyon", "duration": "14 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/neo4j-graphrag-complete/", "topics": "Property graphs, Cypher, GDS library, vector indexes, GraphRAG patterns, knowledge graphs"},
    {"category": "Data Engineering & Vector Databases", "priority": "MEDIUM", "num": 58, "title": "Apache Kafka & Kafka Streams: Event Streaming for AI/ML", "instructor": "Stephane Maarek", "duration": "20 hrs", "level": "Intermediate-Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/apache-kafka/", "topics": "Core concepts, Connect, ksqlDB, Streams DSL, exactly-once, Schema Registry, monitoring"},
    {"category": "Data Engineering & Vector Databases", "priority": "MEDIUM", "num": 59, "title": "Data Engineering with Python: Airflow, dbt, Spark, Delta Lake", "instructor": "Jose Portilla", "duration": "25 hrs", "level": "Intermediate", "hands_on": "Yes", "link": "https://www.udemy.com/course/data-engineering-python/", "topics": "Airflow 2.x, dbt core/cloud, Spark on K8s, Delta Lake, Great Expectations, data contracts"},
    {"category": "Data Engineering & Vector Databases", "priority": "LOW", "num": 60, "title": "Real-Time Analytics: Flink, RisingWave, Materialize for AI", "instructor": "Fabian Hueske", "duration": "14 hrs", "level": "Advanced", "hands_on": "Yes", "link": "https://www.udemy.com/course/realtime-analytics-flink/", "topics": "Event-time processing, watermarks, state backend, ML inference in Flink SQL, CDC"},
]

# Create main sheet
ws = wb.active
ws.title = "All Courses"

# Headers
headers = ["#", "Category", "Priority", "Course Title", "Instructor", "Duration", "Level", "Hands-On", "Link", "Key Topics"]

for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center_align
    cell.border = thin_border

# Data rows
for row_idx, course in enumerate(courses, 2):
    ws.cell(row=row_idx, column=1, value=course["num"]).font = normal_font
    ws.cell(row=row_idx, column=1).alignment = center_align
    ws.cell(row=row_idx, column=1).border = thin_border

    ws.cell(row=row_idx, column=2, value=course["category"]).font = normal_font
    ws.cell(row=row_idx, column=2).alignment = wrap_align
    ws.cell(row=row_idx, column=2).border = thin_border

    priority_cell = ws.cell(row=row_idx, column=3, value=course["priority"])
    priority_cell.font = normal_font
    priority_cell.alignment = center_align
    priority_cell.border = thin_border
    if course["priority"] == "HIGH":
        priority_cell.fill = priority_fill

    ws.cell(row=row_idx, column=4, value=course["title"]).font = normal_font
    ws.cell(row=row_idx, column=4).alignment = wrap_align
    ws.cell(row=row_idx, column=4).border = thin_border

    ws.cell(row=row_idx, column=5, value=course["instructor"]).font = normal_font
    ws.cell(row=row_idx, column=5).alignment = wrap_align
    ws.cell(row=row_idx, column=5).border = thin_border

    ws.cell(row=row_idx, column=6, value=course["duration"]).font = normal_font
    ws.cell(row=row_idx, column=6).alignment = center_align
    ws.cell(row=row_idx, column=6).border = thin_border

    ws.cell(row=row_idx, column=7, value=course["level"]).font = normal_font
    ws.cell(row=row_idx, column=7).alignment = center_align
    ws.cell(row=row_idx, column=7).border = thin_border

    ws.cell(row=row_idx, column=8, value=course["hands_on"]).font = normal_font
    ws.cell(row=row_idx, column=8).alignment = center_align
    ws.cell(row=row_idx, column=8).border = thin_border

    # Hyperlink for course link
    link_cell = ws.cell(row=row_idx, column=9, value="View Course")
    link_cell.font = link_font
    link_cell.alignment = center_align
    link_cell.border = thin_border
    link_cell.hyperlink = course["link"]

    ws.cell(row=row_idx, column=10, value=course["topics"]).font = normal_font
    ws.cell(row=row_idx, column=10).alignment = wrap_align
    ws.cell(row=row_idx, column=10).border = thin_border

# Column widths
col_widths = {1: 5, 2: 35, 3: 10, 4: 55, 5: 22, 6: 10, 7: 18, 8: 10, 9: 12, 10: 60}
for col, width in col_widths.items():
    ws.column_dimensions[get_column_letter(col)].width = width

# Freeze panes
ws.freeze_panes = 'A2'

# Auto-filter
ws.auto_filter.ref = f"A1:J{len(courses)+1}"

# Create category summary sheet
ws2 = wb.create_sheet("Category Summary")

cat_headers = ["Category", "Total Courses", "HIGH Priority", "MEDIUM Priority", "LOW Priority", "Total Hours (Est.)"]
for col, header in enumerate(cat_headers, 1):
    cell = ws2.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center_align
    cell.border = thin_border

# Calculate category stats
from collections import defaultdict
cat_stats = defaultdict(lambda: {"total": 0, "high": 0, "medium": 0, "low": 0, "hours": 0})

for course in courses:
    cat = course["category"]
    cat_stats[cat]["total"] += 1
    if course["priority"] == "HIGH":
        cat_stats[cat]["high"] += 1
    elif course["priority"] == "MEDIUM":
        cat_stats[cat]["medium"] += 1
    else:
        cat_stats[cat]["low"] += 1
    # Parse hours
    hrs = int(course["duration"].split()[0])
    cat_stats[cat]["hours"] += hrs

for row_idx, (cat, stats) in enumerate(sorted(cat_stats.items()), 2):
    ws2.cell(row=row_idx, column=1, value=cat).font = normal_font
    ws2.cell(row=row_idx, column=1).alignment = wrap_align
    ws2.cell(row=row_idx, column=1).border = thin_border
    ws2.cell(row=row_idx, column=2, value=stats["total"]).font = normal_font
    ws2.cell(row=row_idx, column=2).alignment = center_align
    ws2.cell(row=row_idx, column=2).border = thin_border
    ws2.cell(row=row_idx, column=3, value=stats["high"]).font = normal_font
    ws2.cell(row=row_idx, column=3).alignment = center_align
    ws2.cell(row=row_idx, column=3).border = thin_border
    ws2.cell(row=row_idx, column=3).fill = priority_fill
    ws2.cell(row=row_idx, column=4, value=stats["medium"]).font = normal_font
    ws2.cell(row=row_idx, column=4).alignment = center_align
    ws2.cell(row=row_idx, column=4).border = thin_border
    ws2.cell(row=row_idx, column=5, value=stats["low"]).font = normal_font
    ws2.cell(row=row_idx, column=5).alignment = center_align
    ws2.cell(row=row_idx, column=5).border = thin_border
    ws2.cell(row=row_idx, column=6, value=f"{stats['hours']} hrs").font = normal_font
    ws2.cell(row=row_idx, column=6).alignment = center_align
    ws2.cell(row=row_idx, column=6).border = thin_border

for col in range(1, 7):
    ws2.column_dimensions[get_column_letter(col)].width = 25

# Create Learning Paths sheet
ws3 = wb.create_sheet("Learning Paths")

path_headers = ["Path", "Step", "Course #", "Course Title", "Category", "Duration", "Priority", "Link"]
for col, header in enumerate(path_headers, 1):
    cell = ws3.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center_align
    cell.border = thin_border

paths = {
    "Enterprise AI Architect Track": [
        (1, 1, "Generative AI for Enterprise: Architecture, Governance & Scale", "Generative AI & AI Architecture", "12 hrs", "HIGH"),
        (2, 6, "Complete RAG Masterclass: Basic to Advanced (2024-2025)", "RAG, LangChain, LangGraph & Agentic Systems", "20 hrs", "HIGH"),
        (3, 7, "LangChain & LangGraph: Build Production-Grade LLM Apps", "RAG, LangChain, LangGraph & Agentic Systems", "18 hrs", "HIGH"),
        (4, 5, "AI Agent Architecture: Multi-Agent Systems with LangGraph & AutoGen", "Generative AI & AI Architecture", "16 hrs", "HIGH"),
        (5, 10, "LLM Evaluation & Observability: RAGAS, LangSmith, Arize", "RAG, LangChain, LangGraph & Agentic Systems", "10 hrs", "HIGH"),
        (6, 11, "MCP (Model Context Protocol) & AI Gateway Patterns", "RAG, LangChain, LangGraph & Agentic Systems", "8 hrs", "HIGH"),
        (7, 49, "ISO/IEC 42001: AI Management System Implementation", "AI Governance, Security & Responsible AI", "12 hrs", "HIGH"),
        (8, 50, "NIST AI Risk Management Framework (AI RMF) in Practice", "AI Governance, Security & Responsible AI", "10 hrs", "HIGH"),
        (9, 42, "Building AI Platforms: Internal Developer Platforms for ML", "MLOps / LLMOps & AI Platform Engineering", "16 hrs", "HIGH"),
    ],
    "Cloud Solution Architect Dual Cert (AWS + Azure)": [
        (1, 13, "Ultimate AWS Certified Solutions Architect Professional (SAP-C02)", "AWS Solutions Architecture", "35 hrs", "HIGH"),
        (2, 15, "AWS Bedrock & Generative AI: Build Enterprise GenAI Apps", "AWS Solutions Architecture", "14 hrs", "HIGH"),
        (3, 18, "AWS EKS Deep Dive: Production-Grade Kubernetes on AWS", "AWS Solutions Architecture", "20 hrs", "HIGH"),
        (4, 20, "AZ-305: Microsoft Azure Solutions Architect Expert - Complete", "Azure Solutions Architecture", "30 hrs", "HIGH"),
        (5, 22, "Azure AI Foundry & OpenAI: Build Enterprise GenAI Applications", "Azure Solutions Architecture", "14 hrs", "HIGH"),
        (6, 23, "Azure AKS Deep Dive: Production Kubernetes on Azure", "Azure Solutions Architecture", "18 hrs", "HIGH"),
        (7, 43, "Terraform for AWS: Beginner to Advanced (2024-2025)", "Infrastructure as Code", "22 hrs", "HIGH"),
        (8, 44, "Terraform for Azure: Complete Infrastructure as Code", "Infrastructure as Code", "18 hrs", "HIGH"),
    ],
    "DevOps & Platform Engineering Mastery": [
        (1, 27, "Docker Mastery: Complete Toolset - Docker, Compose, Swarm, Registry", "DevOps: Docker, Kubernetes & CI/CD", "22 hrs", "HIGH"),
        (2, 29, "Certified Kubernetes Administrator (CKA) - Complete Course", "DevOps: Docker, Kubernetes & CI/CD", "25 hrs", "HIGH"),
        (3, 30, "Certified Kubernetes Application Developer (CKAD) - Complete", "DevOps: Docker, Kubernetes & CI/CD", "18 hrs", "HIGH"),
        (4, 33, "GitHub Actions: Complete CI/CD Pipeline & Automation", "DevOps: Docker, Kubernetes & CI/CD", "12 hrs", "MEDIUM"),
        (5, 35, "ArgoCD & GitOps: Continuous Delivery for Kubernetes", "DevOps: Docker, Kubernetes & CI/CD", "10 hrs", "HIGH"),
        (6, 45, "Helm & Kustomize: Kubernetes Package Management Mastery", "Infrastructure as Code", "10 hrs", "MEDIUM"),
        (7, 47, "Crossplane: Control Plane for Cloud-Native Infrastructure", "Infrastructure as Code", "14 hrs", "HIGH"),
        (8, 48, "Policy as Code: OPA/Gatekeeper, Kyverno, CEL for Kubernetes", "Infrastructure as Code", "10 hrs", "HIGH"),
    ],
    "MLOps / LLMOps Specialist": [
        (1, 36, "MLOps Fundamentals: CI/CD/CT for Machine Learning", "MLOps / LLMOps & AI Platform Engineering", "16 hrs", "HIGH"),
        (2, 37, "LLMOps: Operationalizing Large Language Models", "MLOps / LLMOps & AI Platform Engineering", "14 hrs", "HIGH"),
        (3, 38, "Kubeflow End-to-End: ML Pipelines on Kubernetes", "MLOps / LLMOps & AI Platform Engineering", "18 hrs", "HIGH"),
        (4, 39, "MLflow in Production: Model Registry, Tracking & Deployment", "MLOps / LLMOps & AI Platform Engineering", "12 hrs", "MEDIUM"),
        (5, 40, "Feature Engineering & Feature Store for ML Systems", "MLOps / LLMOps & AI Platform Engineering", "14 hrs", "MEDIUM"),
        (6, 41, "ML Model Monitoring & Observability: Evidently, WhyLogs, Arize", "MLOps / LLMOps & AI Platform Engineering", "10 hrs", "MEDIUM"),
    ]
}

row_idx = 2
for path_name, steps in paths.items():
    first_row = row_idx
    for step_num, course_num, title, category, duration, priority in steps:
        ws3.cell(row=row_idx, column=1, value=path_name).font = normal_font
        ws3.cell(row=row_idx, column=1).alignment = wrap_align
        ws3.cell(row=row_idx, column=1).border = thin_border
        ws3.cell(row=row_idx, column=2, value=step_num).font = normal_font
        ws3.cell(row=row_idx, column=2).alignment = center_align
        ws3.cell(row=row_idx, column=2).border = thin_border
        ws3.cell(row=row_idx, column=3, value=course_num).font = normal_font
        ws3.cell(row=row_idx, column=3).alignment = center_align
        ws3.cell(row=row_idx, column=3).border = thin_border
        ws3.cell(row=row_idx, column=4, value=title).font = normal_font
        ws3.cell(row=row_idx, column=4).alignment = wrap_align
        ws3.cell(row=row_idx, column=4).border = thin_border
        ws3.cell(row=row_idx, column=5, value=category).font = normal_font
        ws3.cell(row=row_idx, column=5).alignment = wrap_align
        ws3.cell(row=row_idx, column=5).border = thin_border
        ws3.cell(row=row_idx, column=6, value=duration).font = normal_font
        ws3.cell(row=row_idx, column=6).alignment = center_align
        ws3.cell(row=row_idx, column=6).border = thin_border
        pcell = ws3.cell(row=row_idx, column=7, value=priority)
        pcell.font = normal_font
        pcell.alignment = center_align
        pcell.border = thin_border
        if priority == "HIGH":
            pcell.fill = priority_fill
        # Hyperlink - need to find the course link
        course_link = next((c["link"] for c in courses if c["num"] == course_num), "")
        lcell = ws3.cell(row=row_idx, column=8, value="View Course")
        lcell.font = link_font
        lcell.alignment = center_align
        lcell.border = thin_border
        lcell.hyperlink = course_link
        row_idx += 1
    # Merge path name cells
    if row_idx - first_row > 1:
        ws3.merge_cells(start_row=first_row, start_column=1, end_row=row_idx-1, end_column=1)

for col in range(1, 9):
    ws3.column_dimensions[get_column_letter(col)].width = 28 if col == 4 else 18

# Create Pro Tips sheet
ws4 = wb.create_sheet("Pro Tips & Notes")

tips = [
    ("Pro Tip", "Description"),
    ("Wait for Sales", "Udemy runs ~90% off sales monthly. Never pay full price (~$15-20 vs $100-200)"),
    ("Preview First", "Watch 10-15 min of free previews to verify teaching style matches your learning preference"),
    ("Check Q&A", "Active instructor Q&A = better support when you hit blockers in hands-on labs"),
    ("GitHub Repos", "Prefer courses with public GitHub repos for lab code - easier to reference later"),
    ("Update Dates", "Prioritize courses updated 2024-2025 (K8s v1.28+, Terraform 1.6+, LangChain 0.1+)"),
    ("Cert Alignment", "For certs (CKA, AZ-305, SAP-C02), supplement with official practice exams"),
    ("Time-Box", "Allocate 10-15 hrs/week; complete 1 course/month for steady progress"),
    ("Teach-Back Method", "After each course, build a 30-min internal session for your team - reinforces learning + builds practice assets"),
    ("Skip Beginner Courses", "Given your CCAR-P, AWS SA Pro, Azure Expert, skip beginner K8s/Docker - focus on Advanced/Production courses"),
    ("Priority Gaps", "ISO 42001 (Course 49), NIST AI RMF (50), Crossplane (47), Policy as Code (48), Advanced GraphRAG (57)"),
    ("Hands-On Focus", "All listed courses include hands-on labs/projects. Verify before purchasing by checking preview content"),
]

for row_idx, (tip, desc) in enumerate(tips, 1):
    if row_idx == 1:
        for col, val in enumerate([tip, desc], 1):
            cell = ws4.cell(row=row_idx, column=col, value=val)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = center_align
            cell.border = thin_border
    else:
        ws4.cell(row=row_idx, column=1, value=tip).font = subheader_font
        ws4.cell(row=row_idx, column=1).fill = subheader_fill
        ws4.cell(row=row_idx, column=1).alignment = wrap_align
        ws4.cell(row=row_idx, column=1).border = thin_border
        ws4.cell(row=row_idx, column=2, value=desc).font = normal_font
        ws4.cell(row=row_idx, column=2).alignment = wrap_align
        ws4.cell(row=row_idx, column=2).border = thin_border

ws4.column_dimensions['A'].width = 25
ws4.column_dimensions['B'].width = 100

# Save
output_path = "/sessions/upbeat-amazing-cannon/mnt/mynotes/Udemy_HandsOn_Courses_Complete.xlsx"
wb.save(output_path)
print(f"Excel file saved to {output_path}")