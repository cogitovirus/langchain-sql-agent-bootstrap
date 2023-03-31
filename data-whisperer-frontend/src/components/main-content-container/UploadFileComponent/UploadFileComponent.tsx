// src/components/main-content-container/UploadFileComponent/UploadFileComponent.tsx

import React from "react";
import { Box, Button, Card, CardContent, Typography } from "@mui/material";
import { styled } from "@mui/system";

const StyledInput = styled("input")({
  display: "none",
});

export const UploadFileComponent: React.FC = () => {
  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files && event.target.files[0];
    if (file) {
      // Handle file upload logic here
    }
  };

  return (
    <Card>
      <CardContent>
        <Box
          display="flex"
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
        >
          <Typography variant="h6" gutterBottom>
            Upload a file
          </Typography>
          <StyledInput
            id="upload-file-input"
            type="file"
            onChange={handleFileUpload}
          />
          <label htmlFor="upload-file-input">
            <Button component="span" variant="contained">
              Choose file
            </Button>
          </label>
        </Box>
      </CardContent>
    </Card>
  );
};
