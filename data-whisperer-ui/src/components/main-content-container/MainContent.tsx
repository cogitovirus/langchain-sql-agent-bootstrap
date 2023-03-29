import React from 'react';
import { TablesComponent } from './TablesComponent/TablesComponent';
import { UploadFileComponent } from './UploadFileComponent/UploadFileComponent';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

const MainContent = () => (
  <Container maxWidth="lg">
    <Typography variant="h5" gutterBottom sx={{ paddingTop: "1rem" }}>
      Table view
    </Typography>
    <Grid container spacing={3} direction="column">
      <Grid item xs={12} sm={6}>
        <TablesComponent />
      </Grid>
      <Grid item xs={12} sm={6}>
        <UploadFileComponent />
      </Grid>
    </Grid>
  </Container>
);

export default MainContent;
