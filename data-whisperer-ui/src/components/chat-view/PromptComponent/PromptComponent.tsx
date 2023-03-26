import React, { useState } from "react";
import styles from './PromptComponent.module.css';
import axios from "axios";


const PromptComponent: React.FC = () => {
    const [text, setText] = useState("");
    const [generatedText, setGeneratedText] = useState("");

    const generateText = async () => {
        const API_KEY = process.env.REACT_APP_OPENAI_API_KEY;
        const API_URL = "https://api.openai.com/v1/chat/completions";

        const headers = {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`,
        };

        const messages = [
            { role: "system", content: "You are a helpful assistant that translates English to French." },
            { role: "user", content: `Translate the following English text to French: "${text}"` }
        ];

        const data = {
            model: "gpt-3.5-turbo",
            messages,
            max_tokens: 50,
        };

        try {
            const response = await axios.post(API_URL, data, { headers });
            const generated = response.data.choices[0].message.content;
            setGeneratedText(generated);
        } catch (error) {
            console.error("Error generating text:", error);
        }
    };

  return (
    <div className={styles.promptComponent}>
      <h1>AI assisted SQL transformations</h1>
        <input
            type="text"
            placeholder="Enter English text"
            value={text}
            onChange={(e) => setText(e.target.value)}
        />
        <button onClick={generateText}>Generate French translation</button>
        {generatedText && <p>Translation: {generatedText}</p>}
    </div>
  );
};

export default PromptComponent;
