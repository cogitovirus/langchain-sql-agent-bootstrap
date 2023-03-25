import React, { useEffect, useState } from 'react';
import { fetchUsers, User } from '../api';

const UserTable: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    const fetchUserData = async () => {
      const data = await fetchUsers();
      setUsers(data);
    };
    fetchUserData();
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.name}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};


export default UserTable;
