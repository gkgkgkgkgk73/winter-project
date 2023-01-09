import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import './Explanation.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';
import ItemInfo from '../../component/ItemInfo/ItemInfo';
import DecInfo from '../../component/DecInfo/DecInfo';
import AugmentInfo from '../../component/AugmentInfo/AugmentInfo';
import { fetchAugments, fetchChampions, fetchItems, fetchTraits, selectAPI } from '../../store/slices/riotAPI';
import { useSelector } from 'react-redux';

function Explanation(){

    const dispatch = useDispatch<AppDispatch>();
    const augment = useSelector(selectAPI).augment;
    const upperitem = useSelector(selectAPI).item.upperitem;
    const baseitem = useSelector(selectAPI).item.baseitem;
    const champion = useSelector(selectAPI).champion;
    const trait = useSelector(selectAPI).trait;

    const dd = [""]
    useEffect(()=>{
        dispatch(fetchAugments())
        dispatch(fetchChampions())
        dispatch(fetchItems())
        dispatch(fetchTraits())
    })
    return(
        <div className='page'>
            <Header />
            <ItemInfo itemName="itemName" itemImg="itemImg" itemDetail="itemDetail" itemCombination={dd} />
            <DecInfo decName={dd} decImg={dd} decDetailUnit={dd} decDetailUnitImg={dd} decInfo="decInfo"/>
            <AugmentInfo augmentName="augmentName" augmentImg="augmentImg" augmentInfo="augmentInfo"/>
            <div>
                <p>augment:{augment[0].name}</p>
                <p>upperitem:{upperitem[0].name}</p>
                <p>baseitem:{baseitem[0].name}</p>
                <p>champion:{champion[0].name}</p>
                <p>trait:{trait[0].name}</p>
            </div>
        </div>
    );
}

export default Explanation;