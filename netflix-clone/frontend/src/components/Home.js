import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Home.css';

function Home() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8001/api/movies')
      .then(res => setMovies(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="home-container">
      <header className="hero-section">
        <h1>Unlimited movies, TV shows, and more.</h1>
      </header>
      <section className="content-section">
        <h2>Popular Movies</h2>
        <div className="movie-carousel">
          {movies.map(movie => (
            <Link key={movie._id} to={`/movie/${movie._id}`} className="movie-card-link">
              <div className="movie-card">
                <div className="thumbnail">{movie.title.charAt(0)}</div>
                <h3>{movie.title}</h3>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
export default Home;
