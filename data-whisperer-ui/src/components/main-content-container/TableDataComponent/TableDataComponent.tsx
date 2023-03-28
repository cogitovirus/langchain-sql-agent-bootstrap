// TableData.tsx

import React, { useEffect, useState } from "react";
import { fetchTableData } from "../../../api/index";
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
      <h3>{tableName}</h3>
      <div className={styles.tableContainer}>
        <table>
          <thead>
            <tr>
              {tableHeaders.map((header, index) => (
                <th key={index}>{header}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {tableData.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {tableHeaders.map((header, cellIndex) => (
                  <td key={cellIndex}>{row[header]}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
