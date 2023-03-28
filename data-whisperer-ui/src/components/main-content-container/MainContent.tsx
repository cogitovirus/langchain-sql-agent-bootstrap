import React from 'react';
import { TableDataComponent } from './TableDataComponent/TableDataComponent';
import { TablesComponent } from './TablesComponent/TablesComponent';

const MainContent = () => (
  <section className="content">
    <h2>Table view</h2>
    <TablesComponent />
    {/* Add your main content here */}
  </section>
);

export default MainContent;
