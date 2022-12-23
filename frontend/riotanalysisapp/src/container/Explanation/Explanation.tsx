import React from 'react';
import { useDispatch } from 'react-redux';
import './Explanation.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';

function Explanation(){

    const dispatch = useDispatch<AppDispatch>();
    
    return(
        <div className='page'>
            <Header />
        </div>
    );
}

export default Explanation;