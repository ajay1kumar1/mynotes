from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cakes, orders
from app.config import DEBUG

app = FastAPI(
    title="Cake Shop API",
    description="Backend API for Cake Shop",
    version="1.0.0",
    debug=DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cakes.router, prefix="/api/cakes", tags=["cakes"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "Welcome to Cake Shop API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "cake-shop-api"}
