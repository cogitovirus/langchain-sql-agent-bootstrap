// src/api/index.ts

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL ||  'http://localhost:5000';

export interface Customer {
  id: number;
  first_name: string;
  last_name: string;
}

export async function fetchTables(): Promise<string[]> {
  const response = await fetch(`${API_BASE_URL}/api/v1/tables`);
  const data = await response.json();
  return data;
}

export async function fetchCustomers(): Promise<Customer[]> {
  const response = await fetch(`${API_BASE_URL}/api/v1/customers`);
  const data: Customer[] = await response.json();
  return data;
}

export async function fetchTableData(tableName: string): Promise<any[]> {
  const response = await fetch(`${API_BASE_URL}/api/v1/${tableName}`);
  const data = await response.json();
  return data;
}
