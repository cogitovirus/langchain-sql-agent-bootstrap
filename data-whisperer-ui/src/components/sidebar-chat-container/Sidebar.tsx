import React from 'react';
import PromptComponent from './PromptComponent/PromptComponent';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

const Sidebar = () => (
  <Container
    sx={{
      minHeight: '100%',
      display: 'flex',
      flexDirection: 'column',
      padding: '1rem',
    }}
  >
    <Box>
      <Typography variant="h5" gutterBottom>
        GPT Agent
      </Typography>
    </Box>
    <PromptComponent />
  </Container>
);

export default Sidebar;
