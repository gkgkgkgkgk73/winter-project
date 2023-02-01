import React, { useState } from 'react';
import './DiceStat.css';

const TYPE_OPTION = [
    {value: 1, name:'챔피언한테 사용할 때 나올 수 있는 챔피언의 확률'},
    {value: 2, name:'원하는 챔피언이 등장할 확률'}
]

const LEVEL_OPTION = [
    {value: 3, name:'3'},
    {value: 4, name:'4'},
    {value: 5, name:'5'},
    {value: 6, name:'6'},
    {value: 7, name:'7'},
    {value: 8, name:'8'},
    {value: 9, name:'9'},
    {value: 10, name:'10'},
]

//TODO
const CHAMPION_OPTION = [
    {value:'TFT8_Samira', name:'사미라'}
]

const SelectBox = (props:typeof LEVEL_OPTION|typeof TYPE_OPTION|typeof CHAMPION_OPTION) => {
    return (
        <select>
            {props.map((option)=>(
                <option
                    key={option.value}
                    value={option.value}
                >
                    {option.name}
                </option>
            ))}
        </select>
    )
}

function DiceStat() {

    return(
        <div className = "diceStatBox">
            <SelectBox props={TYPE_OPTION}></SelectBox>
        </div>
    );
}

export default DiceStat;