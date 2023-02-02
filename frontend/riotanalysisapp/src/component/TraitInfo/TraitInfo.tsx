import React, { useState } from 'react';
import { RiotChampionType } from '../../store/slices/riotAPI';
import './TraitInfo.css';
import styled from 'styled-components';

export interface IProps {
    traitName:string;
    traitImg:string;
    traitDetail:string;
    champion_list:RiotChampionType[];
    traitID:number;
}
function TraitInfo(props:IProps) {

    const trait_champion_list = props.champion_list.filter(c => c.traits.includes(props.traitID))
    trait_champion_list.sort((a, b)=> a.championCost - b.championCost)
    const [hover, setHover] = useState<number>(-1);

    return(
        <div>
            <div className = "traitInfoBox">
                <img id = "champion-img" src={props.traitImg}/>
                <text id="traitName">{props.traitName}</text>
                <text id="traitDetail">{props.traitDetail}</text>
            </div>
            <div className = "UnitInfoBow">
                {
                    trait_champion_list.map(e=>{
                        return (
                            <div>
                                <div onMouseEnter={()=>setHover(e.id)} onMouseLeave={()=>setHover(-1)}>
                                    <img id = "champion-img" src={e.img}/>
                                </div>
                            </div>
                        )
                    })
                }
                </div>
                {
                    trait_champion_list.map(e=>{
                        return (
                            <div>
                                <DIV_Hover className = {`${hover !== -1 ? 'hover' : 'none'}`}>
                                    {hover === e.id && (
                                        <div className = "hover-text">
                                            <text>name : {trait_champion_list.find(e => e.id === hover)?.name}</text>
                                            <text>stat : {JSON.stringify(trait_champion_list.find(e => e.id === hover)?.championStats)}</text>
                                            <text>info : {trait_champion_list.find(e => e.id === hover)?.info}</text>
                                        </div>
                                    )
                                    }
                                </DIV_Hover>
                            </div>
                        )
                    })
                }
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




export default TraitInfo;