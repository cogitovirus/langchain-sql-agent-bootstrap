import React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import { Container, Grid } from '@mui/material';
import Header from './Header';
import Sidebar from './sidebar-chat-container/Sidebar';
import MainContent from './main-content-container/MainContent';
import Footer from './Footer';
import '../styles/styles.css';

function App() {
  return (
    <div className="app">
      <CssBaseline />
      <Header />
      <Container maxWidth="xl" sx={{ display: 'flex', flexDirection: 'column', minHeight: '90vh' }}>
        <Grid container spacing={5} sx={{ flexGrow: 1 }}>
          <Grid item xs={12} md={6}>
            <Sidebar />
          </Grid>
          <Grid item xs={12} md={6}>
            <MainContent />
          </Grid>
        </Grid>
        <Footer />
      </Container>
    </div>
  );
}

export default App;
