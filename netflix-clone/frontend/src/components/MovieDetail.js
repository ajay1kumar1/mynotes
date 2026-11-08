import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './MovieDetail.css';

function MovieDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8001/api/movies/${id}`)
      .then(res => setMovie(res.data))
      .catch(err => console.error(err));
  }, [id]);

  if (!movie) return <div className="detail-container">Loading...</div>;

  return (
    <div className="detail-container">
      <button className="back-btn" onClick={() => navigate('/')}>← Back</button>
      <div className="detail-content">
        <div className="detail-poster">
          {movie.thumbnail_url ? <img src={movie.thumbnail_url} alt={movie.title} /> : <div className="placeholder">{movie.title.charAt(0)}</div>}
        </div>
        <div className="detail-info">
          <h1>{movie.title}</h1>
          <p className="meta">{movie.release_year} | {movie.is_series ? 'TV Series' : 'Movie'} | {movie.duration_minutes ? `${movie.duration_minutes}m` : ''}</p>
          <p className="description">{movie.description}</p>
          <p><strong>Genre:</strong> {movie.genre ? movie.genre.join(', ') : 'N/A'}</p>
          <p><strong>Director:</strong> {movie.director || 'N/A'}</p>
          <p><strong>Cast:</strong> {movie.cast ? movie.cast.join(', ') : 'N/A'}</p>
          <button className="play-btn">▶ Play</button>
        </div>
      </div>
    </div>
  );
}
export default MovieDetail;
