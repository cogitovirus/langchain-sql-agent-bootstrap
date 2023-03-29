// src/components/main-content-container/TablesComponent/TablesComponent.tsx

import React, { useEffect, useState } from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { fetchTables } from "../../../api/index";
import { TableDataComponent } from "../TableDataComponent/TableDataComponent";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";

interface TabPanelProps {
  children: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index } = props;
  return (
    <div role="tabpanel" hidden={value !== index}>
      {value === index && (
        <Box>
          <Typography component="div">{children}</Typography>
        </Box>
      )}
    </div>
  );
}

export const TablesComponent: React.FC = () => {
  const [tables, setTables] = useState<string[]>([]);
  const [activeTab, setActiveTab] = useState(0);

  useEffect(() => {
    fetchTables().then((data) => setTables(data));
  }, []);

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue);
  };

  return (
    <Card>
      <CardContent
        sx={{
          maxHeight: "400px",
          overflow: "auto",
          boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
          borderRadius: "4px",
          backgroundColor: "#fff",
          padding: "1rem",
        }}
      >
        <Tabs value={activeTab} onChange={handleTabChange} centered>
          {tables.map((table, index) => (
            <Tab key={index} label={table} />
          ))}
        </Tabs>
        {tables.map((table, index) => (
          <TabPanel key={index} value={activeTab} index={index}>
            <TableDataComponent tableName={table} />
          </TabPanel>
        ))}
      </CardContent>
    </Card>
  );
};
