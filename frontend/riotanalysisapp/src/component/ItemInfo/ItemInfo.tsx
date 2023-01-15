import React, {useState} from 'react';
import { RiotBaseItemType } from '../../store/slices/riotAPI';
import './ItemInfo.css';
import styled from 'styled-components';

export interface IProps {
    itemName:string;
    itemImg:string;
    itemDetail:string;
    itemCombination:number[];
    base_item_list:RiotBaseItemType[];
}
function ItemInfo(props:IProps) {

    const [hover, setHover] = useState<number>(-1);

    return(
        <div className = "itemInfoBox">
            <img id="item-img" src={props.itemImg}/>
            <text id="itemName">{props.itemName}</text>
            {
                Object.keys(props.itemCombination).length==2?
                    <div className="itemCombinationBox">
                        <div onMouseEnter={()=>setHover(props.itemCombination[0])} onMouseLeave={()=>setHover(-1)}>
                            <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[0] === i.id)?.img}/>
                        </div>
                        <DIV_Hover className = {`${hover !== -1 ? 'hover' : 'none'}`}>
                                    {hover === props.itemCombination[0] && (
                                        <div className = "hover-text">
                                            <text>name : {props.base_item_list.find(e => e.id === hover)?.name}</text>
                                            <br></br>
                                            <text>info : {props.base_item_list.find(e => e.id === hover)?.info}</text>
                                        </div>
                                    )
                                    }
                                </DIV_Hover>
                        <text>+</text>
                        <div onMouseEnter={()=>setHover(props.itemCombination[1])} onMouseLeave={()=>setHover(-1)}>
                            <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[1] === i.id)?.img}/>
                        </div>
                        <DIV_Hover className = {`${hover !== -1 ? 'hover' : 'none'}`}>
                                    {hover === props.itemCombination[1] && (
                                        <div className = "hover-text">
                                            <text>name : {props.base_item_list.find(e => e.id === hover)?.name}</text>
                                            <br></br>
                                            <text>info : {props.base_item_list.find(e => e.id === hover)?.info}</text>
                                        </div>
                                    )
                                    }
                                </DIV_Hover>
                    </div>
                    :
                    Object.keys(props.itemCombination).length == 1?
                    <div className="itemCombinationBox">
                        <div onMouseEnter={()=>setHover(props.itemCombination[0])} onMouseLeave={()=>setHover(-1)}>
                            <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[0] === i.id)?.img}/>
                        </div>
                        <DIV_Hover className = {`${hover !== -1 ? 'hover' : 'none'}`}>
                                    {hover === props.itemCombination[0] && (
                                        <div className = "hover-text">
                                            <text>name : {props.base_item_list.find(e => e.id === hover)?.name}</text>
                                            <br></br>
                                            <text>info : {props.base_item_list.find(e => e.id === hover)?.info}</text>
                                        </div>
                                    )
                                    }
                                </DIV_Hover>
                        <text>+</text>
                        <div onMouseEnter={()=>setHover(props.itemCombination[0])} onMouseLeave={()=>setHover(-1)}>
                            <img id = "item-img" src={props.base_item_list.find(i => props.itemCombination[0] === i.id)?.img}/>
                        </div>
                        <DIV_Hover className = {`${hover !== -1 ? 'hover' : 'none'}`}>
                                    {hover === props.itemCombination[0] && (
                                        <div className = "hover-text">
                                            <text>name : {props.base_item_list.find(e => e.id === hover)?.name}</text>
                                            <br></br>
                                            <text>info : {props.base_item_list.find(e => e.id === hover)?.info}</text>
                                        </div>
                                    )
                                    }
                                </DIV_Hover>
                    </div>
                    :<></>
            }
            <text id="itemDetail">{props.itemDetail}</text>
        </div>
    );
}

const DIV_Hover = styled.div`
  transition: top 1s ease-in;
  top: 20px; 

  &.hover { 		
    top: 0px;
    animation-duration: 1s;
    animation-name: fadeout;
  }
  
  @keyframes fadeout { 	
    0% {
      opacity: 0; 
    }

    100% {
      opacity: 1;
    }
  }
`;



export default ItemInfo;