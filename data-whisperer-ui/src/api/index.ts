// src/api/index.ts

const API_BASE_URL = 'http://localhost:5000';

export interface User {
  id: number;
  name: string;
}

export async function fetchUsers(): Promise<User[]> {
  const response = await fetch(`${API_BASE_URL}/api/users`);
  const data: User[] = await response.json();
  return data;
}
