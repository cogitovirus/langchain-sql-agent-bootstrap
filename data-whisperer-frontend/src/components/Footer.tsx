// Footer.tsx
import React from 'react';
import { Container, Box, Typography } from '@mui/material';
import './Footer.module.css';

const Footer: React.FC = () => (
  <footer className="footer">
    <Container maxWidth="lg">
      <Box display="flex" justifyContent="center" py={2}>
        <Typography variant="body1">
          2023 cogitovirus.com
        </Typography>
      </Box>
    </Container>
  </footer>
);

export default Footer;
