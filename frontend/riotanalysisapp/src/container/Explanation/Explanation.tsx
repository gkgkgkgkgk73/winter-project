import React from 'react';
import { useDispatch } from 'react-redux';
import './Explanation.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';
import ItemInfo from '../../component/ItemInfo/ItemInfo';
import DecInfo from '../../component/DecInfo/DecInfo';
import AugmentInfo from '../../component/AugmentInfo/AugmentInfo';

function Explanation(){

    const dispatch = useDispatch<AppDispatch>();
    const dd = [""]
    return(
        <div className='page'>
            <Header />
            <ItemInfo itemName="itemName" itemImg="itemImg" itemDetail="itemDetail" itemCombination={dd} />
            <DecInfo decName={dd} decImg={dd} decDetailUnit={dd} decDetailUnitImg={dd} decInfo="decInfo"/>
            <AugmentInfo augmentName="augmentName" augmentImg="augmentImg" augmentInfo="augmentInfo"/>
        </div>
    );
}

export default Explanation;