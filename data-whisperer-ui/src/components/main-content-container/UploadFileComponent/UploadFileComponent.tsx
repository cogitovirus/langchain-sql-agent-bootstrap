// src/components/main-content-container/UploadFileComponent/UploadFileComponent.tsx

import React from "react";
import styles from "./UploadFileComponent.module.css";

export const UploadFileComponent: React.FC = () => {
  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files && event.target.files[0];
    if (file) {
      // Handle file upload logic here
    }
  };

  return (
    <div className={styles.uploadFile}>
      <h3>Upload a file</h3>
      <input type="file" onChange={handleFileUpload} />
    </div>
  );
};
