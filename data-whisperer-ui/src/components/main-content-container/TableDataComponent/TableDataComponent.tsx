// TableDataComponent.tsx

import React, { useEffect, useState } from "react";
import { fetchTableData } from "../../../api/index";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
} from "@mui/material";
import styles from "./TableDataComponent.module.css";

interface TableDataProps {
  tableName: string;
}

export const TableDataComponent: React.FC<TableDataProps> = ({ tableName }) => {
  const [tableData, setTableData] = useState<any[]>([]);
  const [tableHeaders, setTableHeaders] = useState<string[]>([]);

  useEffect(() => {
    fetchTableData(tableName).then((data) => {
      if (data.length > 0) {
        setTableHeaders(Object.keys(data[0]));
      }
      setTableData(data);
    });
  }, [tableName]);

  return (
    <div className={styles.tabpanel}>
      <Typography variant="h6" component="div">
        {tableName}
      </Typography>
      <TableContainer component={Paper} className={styles.tableContainer}>
        <Table>
          <TableHead>
            <TableRow>
              {tableHeaders.map((header, index) => (
                <TableCell key={index}>{header}</TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {tableData.map((row, rowIndex) => (
              <TableRow key={rowIndex}>
                {tableHeaders.map((header, cellIndex) => (
                  <TableCell key={cellIndex}>{row[header]}</TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};
