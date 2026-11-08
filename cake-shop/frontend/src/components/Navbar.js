import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">🍰 Sweet Delights</Link>
        <div className="menu-icon" onClick={() => setMenuOpen(!menuOpen)}>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <ul className={menuOpen ? 'nav-menu active' : 'nav-menu'}>
          <li><Link to="/" className="nav-link">Home</Link></li>
          <li><Link to="/products" className="nav-link">Products</Link></li>
          <li><Link to="/cart" className="nav-link">Cart 🛒</Link></li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
