# 🍰 Cake Shop - Full Stack E-commerce Application

A stunning, mobile-responsive cake shop e-commerce platform built with React frontend and FastAPI backend, featuring MongoDB database and Docker containerization.

## ✨ Features

- **Stunning UI**: Modern, responsive design with smooth animations
- **Mobile First**: Fully responsive on all devices (mobile, tablet, desktop)
- **React Frontend**: Modern SPA with React Router, Axios
- **FastAPI Backend**: High-performance Python API with async MongoDB
- **Docker Ready**: Complete containerization with docker-compose
- **CI/CD**: GitHub Actions automation
- **Test Coverage**: Python pytest tests included

## 📁 Project Structure

```
cake-shop/
├── frontend/           # React application
│   ├── src/
│   │   ├── components/ # Reusable UI components
│   │   ├── App.js
│   │   └── index.js
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
├── backend/            # FastAPI application
│   ├── app/
│   │   ├── routers/    # API endpoints
│   │   ├── models.py   # Pydantic models
│   │   ├── config.py   # Configuration with dotenv
│   │   ├── database.py # MongoDB connection
│   │   └── main.py     # FastAPI app
│   ├── tests/          # Python tests
│   ├── Dockerfile
│   └── requirements.txt
├── .github/workflows/  # CI/CD pipelines
└── docker-compose.yml  # Multi-service orchestration
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Clone and start**:
   ```bash
   git clone <your-repo>
   cd cake-shop
   docker-compose up -d
   ```

2. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Option 2: Without Docker

#### Backend Setup

1. **Navigate to backend**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB URL
   ```

5. **Run backend**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

#### Frontend Setup

1. **Navigate to frontend**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit REACT_APP_API_URL if needed
   ```

4. **Run frontend**:
   ```bash
   npm start
   ```

## 🧪 Running Tests

```bash
cd backend
pytest -v
```

## ⚙️ Environment Variables

### Backend (.env)
```
MONGODB_URL=mongodb://localhost:27017/cake_shop
DATABASE_NAME=cake_shop
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_NAME=Sweet Delights
```

## 🐳 Docker Commands

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

## 📱 Mobile Responsive

The application is fully responsive and tested on:
- Mobile phones (320px - 768px)
- Tablets (768px - 1024px)
- Desktop (1024px+)

## 🛠️ Tech Stack

**Frontend:**
- React 18
- React Router DOM
- Axios
- CSS3 with animations

**Backend:**
- FastAPI
- MongoDB (Motor - async driver)
- Pydantic
- Python-dotenv

**DevOps:**
- Docker & Docker Compose
- GitHub Actions
- Nginx

## 📄 API Endpoints

- `GET /api/cakes/` - List all cakes
- `GET /api/cakes/{id}` - Get cake details
- `POST /api/cakes/` - Create cake
- `GET /api/orders/` - List orders
- `POST /api/orders/` - Create order
- `GET /health` - Health check

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

MIT License - feel free to use for your projects!
