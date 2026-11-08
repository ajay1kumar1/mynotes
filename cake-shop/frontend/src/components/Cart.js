import React from 'react';
import './Cart.css';

function Cart() {
  return (
    <div className="cart-page">
      <h1>Your Cart</h1>
      <div className="empty-cart">
        <span className="cart-icon">🛒</span>
        <p>Your cart is empty</p>
        <p>Add some delicious cakes from our collection!</p>
      </div>
    </div>
  );
}

export default Cart;
