import React from 'react';
import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Explanation from './container/Explanation/Explanation';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Explanation/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
