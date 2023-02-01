import React from 'react';
import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Explanation from './container/Explanation/Explanation';
import AugmentStat from './container/AugmentStat/AugmentStat';
import UserInfo from './component/UserInfo/UserInfo';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Explanation/>}/>
        <Route path='/userinfo' element={<UserInfo/>}/>
        <Route path='/augmentstat' element={<AugmentStat/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
