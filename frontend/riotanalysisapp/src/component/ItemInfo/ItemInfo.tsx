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
            <img id="item-img" src={props.itemImg}/>
            <text id="itemName">{props.itemName}</text>
            {
                Object.keys(props.itemCombination).length==2?
                    <div className="itemCombinationBox">
                        <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[0] === i.id)?.img}/>
                        <text>+</text>
                        <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[1] === i.id)?.img}/>
                    </div>
                    :
                    Object.keys(props.itemCombination).length == 1?
                    <div className="itemCombinationBox">
                        <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[0] === i.id)?.img}/>
                        <text>+</text>
                        <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[0] === i.id)?.img}/>
                    </div>
                    :<></>
            }
            <text id="itemDetail">{props.itemDetail}</text>
        </div>
    );
}

export default ItemInfo;