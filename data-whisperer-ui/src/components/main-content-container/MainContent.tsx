import React from 'react';
import { TableDataComponent } from './TableDataComponent/TableDataComponent';
import { TablesComponent } from './TablesComponent/TablesComponent';
import { UploadFileComponent } from './UploadFileComponent/UploadFileComponent';

const MainContent = () => (
  <section className="content">
    <h2>Table view</h2>
    <TablesComponent />
    <UploadFileComponent />
  </section>
);

export default MainContent;
