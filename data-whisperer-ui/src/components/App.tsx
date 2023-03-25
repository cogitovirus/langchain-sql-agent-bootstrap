import React, { useState } from "react";
import ChatComponent from "./ChatComponent";
import DBViewComponent from "./DBViewComponent";
import SideDrawer from './SideDrawer';


const App: React.FC = () => {

  const [sideDrawerOpen, setSideDrawerOpen] = useState(false);

  const toggleSideDrawer = () => {
    setSideDrawerOpen((prevState) => !prevState);
  };

  return (

    <div className="container">
      {/* <div>
        <button onClick={toggleSideDrawer}>Toggle Side Drawer</button>
        <SideDrawer show={sideDrawerOpen} />
      </div> */}
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
