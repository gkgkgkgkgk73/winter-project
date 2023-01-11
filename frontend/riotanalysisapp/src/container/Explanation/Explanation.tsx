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
import TraitInfo from '../../component/TraitInfo/TraitInfo';

function Explanation(){

    const dispatch = useDispatch<AppDispatch>();
    const trait = useSelector(selectAPI).trait.traits;
    const champion = useSelector(selectAPI).champion.champions;
    const upperitem = useSelector(selectAPI).item.upperItems;
    const baseitem = useSelector(selectAPI).item.baseItems;
    const augment = useSelector(selectAPI).augment.augments;

    const dd = [""]
    useEffect(()=>{
        async function fetchAll(){
            await dispatch(fetchAugments())
            await dispatch(fetchChampions())
            await dispatch(fetchItems())
            await dispatch(fetchTraits())
        }
        fetchAll()
    },[])
    return(
        <div className='page'>
            <Header />
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