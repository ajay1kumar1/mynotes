import React, { useState, useEffect } from 'react';
import './Products.css';

const mockProducts = [
  { id: 1, name: 'Chocolate Fudge Cake', price: 29.99, image: '🍫', description: 'Rich chocolate with fudge filling' },
  { id: 2, name: 'Red Velvet Dream', price: 32.99, image: '❤️', description: 'Classic red velvet with cream cheese' },
  { id: 3, name: 'Vanilla Bean Delight', price: 27.99, image: '🍦', description: 'Pure vanilla with fresh berries' },
  { id: 4, name: 'Strawberry Cheesecake', price: 34.99, image: '🍓', description: 'Creamy cheesecake with strawberries' },
  { id: 5, name: 'Lemon Drizzle', price: 26.99, image: '🍋', description: 'Zesty lemon with sweet glaze' },
  { id: 6, name: 'Carrot Spice Cake', price: 28.99, image: '🥕', description: 'Warm spices with cream cheese frosting' },
];

function Products() {
  const [products] = useState(mockProducts);
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    setCart([...cart, product]);
    alert(`${product.name} added to cart!`);
  };

  return (
    <div className="products-page">
      <h1>Our Delicious Cakes</h1>
      <div className="products-grid">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <div className="product-image">{product.image}</div>
            <h3>{product.name}</h3>
            <p className="description">{product.description}</p>
            <div className="product-footer">
              <span className="price">${product.price}</span>
              <button onClick={() => addToCart(product)} className="add-btn">Add to Cart</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Products;
