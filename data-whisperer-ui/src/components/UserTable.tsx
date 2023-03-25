import React, { useEffect, useState } from 'react';
import { fetchCustomers, Customer } from '../api';

const UserTable: React.FC = () => {
  const [customers, setCustomers] = useState<Customer[]>([]);

  useEffect(() => {
    const fetchUserData = async () => {
      const data = await fetchCustomers();
      setCustomers(data);
    };
    fetchUserData();
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>First Name</th>
          <th>Last Name</th>
        </tr>
      </thead>
      <tbody>
        {customers.map((customer) => (
          <tr key={customer.id}>
            <td>{customer.id}</td>
            <td>{customer.first_name}</td>
            <td>{customer.last_name}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};


export default UserTable;
