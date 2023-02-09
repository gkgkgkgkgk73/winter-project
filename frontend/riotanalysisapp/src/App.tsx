import React from 'react';
import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Explanation from './container/Explanation/Explanation';
import AugmentStat from './container/AugmentStat/AugmentStat';
import UserInfo from './container/UserInfo/UserInfo';
import DiceStat from './container/DiceStat/DiceStat';
import ItemForUnit from './container/ItemForUnit/ItemForUnit';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Explanation/>}/>
        <Route path='/userinfo' element={<UserInfo/>}/>
        <Route path='/augmentstat' element={<AugmentStat/>}/>
        <Route path='/dicestat' element={<DiceStat/>}/>
        <Route path='/itemforunit' element={<ItemForUnit/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
