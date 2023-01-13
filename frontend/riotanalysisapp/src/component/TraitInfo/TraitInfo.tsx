import React from 'react';
import { RiotChampionType } from '../../store/slices/riotAPI';
import './TraitInfo.css';

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

    return(
        <div>
            <div className = "traitInfoBox">
                <img id = "champion-img" src={props.traitImg}/>
                <text id="traitName">{props.traitName}</text>
                <text id="traitDetail">{props.traitDetail}</text>
            </div>
            <div>
                {
                    trait_champion_list.map(e=>{
                        return (
                            <img id = "champion-img" src={e.img}/>
                        )
                    })
                }
            </div>
        </div>
    );
}

export default TraitInfo;