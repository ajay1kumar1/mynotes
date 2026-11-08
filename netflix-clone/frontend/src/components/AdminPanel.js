import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function AdminPanel() {
  const [movies, setMovies] = useState([]);
  const [newMovie, setNewMovie] = useState({ title: '', description: '', genre: [], release_year: 2023 });
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) { navigate('/login'); return; }
    
    axios.get('http://localhost:8001/api/movies')
      .then(res => setMovies(res.data))
      .catch(err => { if(err.response.status === 403) navigate('/'); });
  }, [navigate]);

  const addMovie = async () => {
    const token = localStorage.getItem('token');
    await axios.post('http://localhost:8001/api/admin/movies', newMovie, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert('Movie Added');
    window.location.reload();
  };

  const deleteMovie = async (id) => {
    const token = localStorage.getItem('token');
    await axios.delete(`http://localhost:8001/api/admin/movies/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setMovies(movies.filter(m => m._id !== id));
  };

  return (
    <div style={{ padding: '2rem', background: '#111', color: '#fff', minHeight: '100vh' }}>
      <h1>Admin Panel</h1>
      <section>
        <h2>Add Movie</h2>
        <input placeholder="Title" onChange={e => setNewMovie({...newMovie, title: e.target.value})} />
        <button onClick={addMovie}>Add</button>
      </section>
      <section>
        <h2>Movies</h2>
        {movies.map(m => (
          <div key={m._id} style={{ display: 'flex', gap: '1rem', marginBottom: '10px' }}>
            <span>{m.title}</span>
            <button onClick={() => deleteMovie(m._id)}>Delete</button>
          </div>
        ))}
      </section>
    </div>
  );
}
export default AdminPanel;
