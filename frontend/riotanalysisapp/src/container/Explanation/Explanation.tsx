import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import './Explanation.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';
import ItemInfo from '../../component/ItemInfo/ItemInfo';
import DecInfo from '../../component/DecInfo/DecInfo';
import AugmentInfo from '../../component/AugmentInfo/AugmentInfo';
import { AugmentState, RiotChampionType, RiotAugmentType, RiotBaseItemType, RiotUpperItemType, fetchAugments, fetchChampions, fetchItems, fetchTraits, selectAPI, RiotTraitType } from '../../store/slices/riotAPI';
import { useSelector } from 'react-redux';

function Explanation(){

    const dispatch = useDispatch<AppDispatch>();
    // const [augment, setAugment] = useState<RiotAugmentType[] | undefined>();
    // const [upperItem, setUpperItem] = useState<RiotUpperItemType[] | undefined>()
    // const [baseItem, setBaseItem] = useState<RiotBaseItemType[] | undefined>()
    // const [champion, setChampion] = useState<RiotChampionType[] | undefined>()
    // const [trait, setTrait] = useState<RiotTraitType[] | undefined>();
    let augment;
    let champion;
    let item;
    let trait;

    const dd = [""]
    useEffect(()=>{
        async function fetchAll(){
            augment = await (await dispatch(fetchAugments())).payload
            champion = await (await dispatch(fetchChampions())).payload
            item = await (await dispatch(fetchItems())).payload
            trait = await (await dispatch(fetchTraits())).payload
            console.log(augment)
        }
        fetchAll()
    },[])
    return(
        <div className='page'>
            <Header />
            <ItemInfo itemName="itemName" itemImg="itemImg" itemDetail="itemDetail" itemCombination={dd} />
            <DecInfo decName={dd} decImg={dd} decDetailUnit={dd} decDetailUnitImg={dd} decInfo="decInfo"/>
            <AugmentInfo augmentName="augmentName" augmentImg="augmentImg" augmentInfo="augmentInfo"/>
            <div>
                {/* <p>augment:{augment.name}</p>
                <p>upperitem:{upperitem.name}</p>
                <p>baseitem:{baseitem.name}</p>
                <p>champion:{champion.name}</p>
                <p>trait:{trait[0].name}</p> */}
                <p>{augment}</p>
            </div>
        </div>
    );
}

export default Explanation;