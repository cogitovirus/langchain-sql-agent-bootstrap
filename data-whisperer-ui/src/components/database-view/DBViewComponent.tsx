// DBViewComponent.tsx

import React, { useEffect, useState } from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { fetchTables } from "../../api/index"
import { TableData } from "./TableData";
import "./DBViewComponent.module.css";



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

export const DBViewComponent: React.FC = () => {
  const [tables, setTables] = useState<string[]>([]);
  const [activeTab, setActiveTab] = useState(0);

  useEffect(() => {
    fetchTables().then((data) => setTables(data));
  }, []);

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue);
  };

  return (
    <div className="db-view-component">
    <Tabs value={activeTab} onChange={handleTabChange}>
      {tables.map((table, index) => (
        <Tab key={index} label={table} />
      ))}
    </Tabs>
    {tables.map((table, index) => (
      <TabPanel key={index} value={activeTab} index={index}>
        <TableData tableName={table} />
      </TabPanel>
    ))}
  </div>
  );
};
