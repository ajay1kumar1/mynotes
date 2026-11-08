import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <section className="hero">
        <div className="hero-content">
          <h1>Welcome to Sweet Delights</h1>
          <p>Handcrafted cakes made with love and the finest ingredients</p>
          <Link to="/products" className="cta-button">Explore Cakes</Link>
        </div>
      </section>
      
      <section className="features">
        <div className="feature-card">
          <span className="emoji">🎂</span>
          <h3>Fresh Daily</h3>
          <p>Baked fresh every morning</p>
        </div>
        <div className="feature-card">
          <span className="emoji">🚚</span>
          <h3>Free Delivery</h3>
          <p>Free delivery on orders over $50</p>
        </div>
        <div className="feature-card">
          <span className="emoji">⭐</span>
          <h3>5 Star Rated</h3>
          <p>Loved by thousands of customers</p>
        </div>
      </section>
    </div>
  );
}

export default Home;
