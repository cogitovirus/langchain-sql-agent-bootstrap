// src/components/SideDrawer.tsx

import React from 'react';
import './SideDrawer.css';

interface SideDrawerProps {
  show: boolean;
}

const SideDrawer: React.FC<SideDrawerProps> = ({ show }) => {
  const drawerClasses = show ? 'side-drawer open' : 'side-drawer';

  return (
    <nav className={drawerClasses}>
      <ul>
        <li>
          <a href="/">Link 1</a>
        </li>
        <li>
          <a href="/">Link 2</a>
        </li>
        <li>
          <a href="/">Link 3</a>
        </li>
      </ul>
    </nav>
  );
};

export default SideDrawer;
