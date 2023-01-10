import React from 'react';
import { RiotBaseItemType } from '../../store/slices/riotAPI';
import './ItemInfo.css';

export interface IProps {
    itemName:string;
    itemImg:string;
    itemDetail:string;
    itemCombination:number[];
    base_item_list:RiotBaseItemType[];
}
function ItemInfo(props:IProps) {
    return(
        <div className = "itemInfoBox">
            <img src={props.itemImg}/>
            <text id="itemName">{props.itemName}</text>
            <div className="itemCombinationBox">
                {/* <img src={props.itemCombination[0]}/>
                <text>+</text>
                <img src={props.itemCombination[1]}/> */}
            </div>
            <text id="itemDetail">{props.itemDetail}</text>
        </div>
    );
}

export default ItemInfo;