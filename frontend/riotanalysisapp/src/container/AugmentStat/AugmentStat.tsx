import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import './AugmentStat.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';
import ItemInfo from '../../component/ItemInfo/ItemInfo';
import DecInfo from '../../component/DecInfo/DecInfo';
import AugmentInfo from '../../component/AugmentInfo/AugmentInfo';
import { fetchAugments, fetchChampions, fetchItems, fetchTraits, selectAPI } from '../../store/slices/riotAPI';
import { useSelector } from 'react-redux';

function AugmentStat(){
    const dd = [""]

    return(
        
        <div className='page'>
            <Header />
            <table>
                <colgroup>
                    <col width="70"></col>
                    <col width="140"></col>
                    <col width="70"></col>
                    <col width="70"></col> 
                </colgroup>
                <thead>
                    <tr>
                        <th scope = "col">순위</th>
                        <th scope = "col">증강체</th>
                        <th scope = "col">승률</th>
                        <th scope = "col">픽률</th>
                    </tr>
                </thead>
                <tbody>
                    
                </tbody>
            </table>
           
        </div>

    );
}

export default AugmentStat;