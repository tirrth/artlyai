import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [imageURL, setImageURL] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const headers = {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.REACT_APP_OPENAI_API_KEY}`,
    };

    const payload = {
      'prompt': text,
      'n': 1,
      'size': '1024x1024',
    };

    try {
      const response = await axios.post('https://api.openai.com/v1/images/generations', payload, { headers });
      if (response.status === 200) {
        setImageURL(response.data.data[0].url);
      }
    } catch (error) {
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>AI Art Generator</h1>
        <form onSubmit={handleSubmit}>
          <label htmlFor="text">Text Prompt:</label>
          <input
            type="text"
            id="text"
            name="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            required
          />
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Generating...' : 'Generate Art'}
          </button>
        </form>
        {imageURL && (
          <div className="result-container">
            <h3>Generated Art:</h3>
            <img
              src={imageURL}
              alt="Generated Art"
              className="generated-image"
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
