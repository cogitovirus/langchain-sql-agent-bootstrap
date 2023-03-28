import React, { useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./sidebar-chat-container/Sidebar";
import MainContent from "./main-content-container/MainContent";
import './../styles/styles.css';



const App: React.FC = () => {

  return (
    <div className="app">
      <Header />
    <main className="main">
      <Sidebar />
      <MainContent />
    </main>
    <Footer />

  </div>

  );
};

export default App;
