import React, { useState } from "react";
import PromptComponent from "./PromptComponent/PromptComponent";
import ResponseComponent from "./ResponseComponent/ResponseComponent";
import styles from "./ChatComponent.module.css";

const ChatComponent = () => {

    return (
    <div className={styles.promptComponent}>
        <PromptComponent />
        <ResponseComponent />

    </div>
    );

};

export default ChatComponent;
