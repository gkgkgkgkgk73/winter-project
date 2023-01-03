import React from 'react';
import './AugmentInfo.css';
export interface IProps {
    augmentName:string;
    augmentImg:string;
    augmentInfo:string;
}
function AugmentInfo(props:IProps) {
    return(
        <div className = "augmentInfoBox">
            <text id="augmentName">{props.augmentName}</text>
            <img src={props.augmentImg} alt="로딩중"/>
            <text id="augmentInfo">{props.augmentInfo}</text>
        </div>
    );
}

export default AugmentInfo;