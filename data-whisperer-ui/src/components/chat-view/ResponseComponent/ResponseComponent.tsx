import React from 'react';
import styles from './ResponseComponent.module.css';

const ResponseComponent: React.FC = () => {
  return (
    <div className={styles.responseComponent}>
      <p>Response content goes here</p>
    </div>
  );
};

export default ResponseComponent;
