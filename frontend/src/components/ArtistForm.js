import React, { useState } from 'react';
import axios from 'axios';

const ArtistForm = () => {
    const [email, setEmail] = useState('');
    const [artist, setArtist] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:5000/register', { email, artist });
            alert('User registered for notifications!');
        } catch (error) {
            console.error('Error registering user', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email:</label>
                <input 
                    type="email" 
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)} 
                    required 
                />
            </div>
            <div>
                <label>Artist:</label>
                <input 
                    type="text" 
                    value={artist} 
                    onChange={(e) => setArtist(e.target.value)} 
                    required 
                />
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default ArtistForm;
