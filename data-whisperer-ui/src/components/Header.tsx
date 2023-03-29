// Header.tsx
import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const Header: React.FC = () => (
  <header className="header">
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Data Whisperer v.0.0.1
        </Typography>
        {/* <Button color="inherit">Menu Item 1</Button>
        <Button color="inherit">Menu Item 2</Button>
        <Button color="inherit">Menu Item 3</Button> */}
      </Toolbar>
    </AppBar>
  </header>
);

export default Header;
