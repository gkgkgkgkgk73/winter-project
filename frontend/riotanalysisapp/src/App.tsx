import React from 'react';
import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Explanation from './container/Explanation/Explanation';
import AugmentStat from './container/AugmentStat/AugmentStat';
import DecInfo from './component/DecInfo/DecInfo';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Explanation/>}/>
        {/* <Route path='/decinfo' element={<DecInfoPage/>}/> */}
        <Route path='/augmentstat' element={<AugmentStat/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
