import React from 'react';
import './DecInfo.css';
export interface IProps {
    decName:string[];
    decImg:string[];
    decDetailUnit:string[];
    decDetailUnitImg:string[];
    decInfo:string;
}
function DecInfo(props:IProps) {
    return(
        <div className = "decInfoBox">
            <div className = "decNameNInfo">
                {props.decName.map((e)=>{
                    return <text id="decName">{e}</text>
                })}
                {props.decImg.map((e)=>{
                    return <img src={e}/>
                })}
            </div>
            <text id="unitInfoTitle">유닛 종류</text>
            <div className = "decUnitNameNInfo">
                {props.decDetailUnit.map((e)=>{
                    return <text id="decUnitName">{e}</text>
                })}
                {props.decDetailUnitImg.map((e)=>{
                    return <img src={e}/>
                })}
            </div>
            <text id="decInfo">{props.decInfo}</text>
        </div>
    );
}

export default DecInfo;