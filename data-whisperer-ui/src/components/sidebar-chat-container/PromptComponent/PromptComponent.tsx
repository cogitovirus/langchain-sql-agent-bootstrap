import React, { useState, useEffect } from "react";
import styles from './PromptComponent.module.css';
import axios from "axios";
import io from 'socket.io-client';

const PromptComponent: React.FC = () => {
  const [text, setText] = useState("");
  const [generatedText, setGeneratedText] = useState("");
  const [output, setOutput] = useState(""); // New state variable for the output

  const generateText = async () => {
    const API_BASE_URL = process.env.REACT_APP_API_BASE_URL ||  'http://localhost:5000';
    const API_URL = `${API_BASE_URL}/api/v1/run`;

    const data = {
      command: text,
    };

    try {
        const response = await axios.post(API_URL, data);
        const generated = response.data.choices[0].message.content;
        setGeneratedText(generated);
      } catch (error) {
        console.error("Error generating text:", error);
      }
  };

  // Socket.io integration
  useEffect(() => {
    const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';
    const socket = io(API_BASE_URL);

    socket.on('output', (data) => {
        console.log(data.message);
        setOutput((prevOutput) => prevOutput + data.message + '\n'); // Update the output state
    });

    return () => {
        socket.disconnect();
    };
  }, []);

  return (
    <div className={styles.promptComponent}>
      <input
        type="text"
        placeholder="Enter command here"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={generateText}>Generate SQL transformation</button>
      {generatedText && <p>Output: {generatedText}</p>}
      {/* Display the output */}
      <pre id="output" className="output-box">{output}</pre>
    </div>
  );
};

export default PromptComponent;
