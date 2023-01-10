import React from 'react';
import { RiotChampionType } from '../../store/slices/riotAPI';
import './TraitInfo.css';

export interface IProps {
    traitName:string;
    traitImg:string;
    traitDetail:string;
    champion_list:RiotChampionType[];
}
function TraitInfo(props:IProps) {
    return(
        <div className = "traitInfoBox">
            <img src={props.traitImg}/>
            <text id="traitName">{props.traitName}</text>
            <text id="traitDetail">{props.traitDetail}</text>
        </div>
    );
}

export default TraitInfo;