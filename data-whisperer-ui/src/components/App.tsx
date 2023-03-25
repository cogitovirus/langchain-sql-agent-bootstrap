import React, { useState } from "react";
import ChatComponent from "./ChatComponent";
import DBViewComponent from "./DBViewComponent";

const App: React.FC = () => {

  return (
    <div className="container">
      <div className="left">
        <ChatComponent />
      </div>
      <div className="right">
        <DBViewComponent />
      </div>
    </div>
  );
};

export default App;
