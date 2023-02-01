import React, { useEffect, useState } from 'react';
import './DiceStat.css';
import { useDispatch } from 'react-redux';
import { AppDispatch } from '../../store';
import { fetchDiceStat, selectdicestat } from '../../store/slices/riotAPI';
import { useSelector } from 'react-redux';
import Header from '../../component/Header/Header';


function DiceStat() {

    const [type, setType] = useState<number>(1);
    const [level, setLevel] = useState<number>(3);
    const [champion, setChampion] = useState<string>('TFT8_Samira');
    const dispatch = useDispatch<AppDispatch>();
    const [ready, setReady] = useState<boolean>(false);
    const dicestat = useSelector(selectdicestat);
    const TYPE_OPTION = [
        {value: 1, name:'챔피언한테 사용할 때 나올 수 있는 챔피언의 확률'},
        {value: 2, name:'원하는 챔피언이 등장할 확률'}
    ]

    useEffect(()=>{
        if(dicestat.targetChampion!==""){
            setReady(true)
            console.log('useeffect')
            console.log(dicestat.diceStat[0].champion_name)
        }
    },[dicestat])
    
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

    const onClickSearchHandler = () => {
        setReady(false)
        dispatch(fetchDiceStat({type:type,level:level,name:champion}))
        console.log(dicestat.targetChampion)
    }
    
    return(
        <div className = "diceStatBox" id = "diceStatBox">
            <Header/>
            <div>
                <select id="type-select" onChange={(e:any)=>setType(e.target.value)}
                defaultValue={TYPE_OPTION[0].value}>
                    {TYPE_OPTION.map((option)=>(
                        <option
                        key={option.value}
                        value={option.value}
                        >{option.name}</option>
                    ))}
                </select>
                <select id="level-select" onChange={(e:any)=>setLevel(e.target.value)}
                defaultValue={LEVEL_OPTION[0].value}>
                    {LEVEL_OPTION.map((option)=>(
                        <option
                        key={option.value}
                        value={option.value}
                        >{option.name}</option>
                    ))}
                </select>
                <select id="champion-select" onChange={(e:any)=>setChampion(e.target.value)}
                defaultValue={CHAMPION_OPTION[0].value}>
                    {CHAMPION_OPTION.map((option)=>(
                        <option
                        key={option.value}
                        value={option.value}
                        >{option.name}</option>
                    ))}
                </select>
                <button className='navigate-btn' onClick={onClickSearchHandler}>찾기</button>
            </div>
            {ready?
                <div>
                    {dicestat.diceStat.map((e)=>(
                        <div>
                            <p>name: {e.champion_name}</p>
                            <p>stat: {e.stat}</p>
                        </div>
                    ))}
                </div>
                :
                <></>
            }
        </div>
    );
}

export default DiceStat;