import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import './Explanation.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';
import ItemInfo from '../../component/ItemInfo/ItemInfo';
import DecInfo from '../../component/DecInfo/DecInfo';
import AugmentInfo from '../../component/AugmentInfo/AugmentInfo';
import { fetchAugments, fetchChampions, fetchItems, fetchTraits, RiotAugmentType, RiotTraitType, RiotUpperItemType, selectAPI } from '../../store/slices/riotAPI';
import { useSelector } from 'react-redux';
import TraitInfo from '../../component/TraitInfo/TraitInfo';

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
            <DecInfo decName={dd} decImg={dd} decDetailUnit={dd} decDetailUnitImg={dd} decInfo="decInfo"/>
            <AugmentInfo augmentName="augmentName" augmentImg="augmentImg" augmentInfo="augmentInfo"/>
            <div className = 'trait-info-box'>
                {
                    trait.map((e:RiotTraitType)=>{
                        return(
                            <TraitInfo traitDetail={e.info} traitImg = {e.img} traitName = {e.name} champion_list={champion}/>
                        )
                    })
                }
            </div>
            <div className = 'item-info-box'>
                {
                    upperitem.map((e:RiotUpperItemType)=>{
                        return (
                            <ItemInfo itemName={e.name} itemDetail = {e.info} itemImg = {e.img} itemCombination = {e.baseItems} base_item_list={baseitem}/>
                        )
                    })
                }
            </div>
            <div className = 'augment-info-box'>
                {
                    augment.map((e:RiotAugmentType)=>{
                        return (
                            <AugmentInfo augmentImg={e.img} augmentInfo={e.info} augmentName={e.name} />
                        )
                    })
                }
            </div>
        </div>
    );
}

export default Explanation;