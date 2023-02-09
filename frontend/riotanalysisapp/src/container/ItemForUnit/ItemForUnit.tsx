import './ItemForUnit.css';
import { AppDispatch } from '../../store';
import Header from '../../component/Header/Header';
import ItemInfo from '../../component/ItemInfo/ItemInfo';
import { RiotBaseItemType, RiotUpperItemType, fetchItemForUnit, fetchItems, selectbaseitems, selectitemforunit } from '../../store/slices/riotAPI';
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import { useEffect, useState } from 'react';

function ItemForUnit(){

    const CHAMPION_OPTION = [
        {value:'TFT8_Samira', name:'사미라'},
        {value:'TFT8_Sylas', name:'사일러스'},
        {value:'TFT8_Nasus', name:'나서스'},
        {value:'TFT8_Jinx', name:'징크스'},
        {value:'TFT8_Vayne', name:'베인'},
        {value:'TFT8_Riven', name:'리븐'},
        {value:'TFT8_MissFortune', name:'미스 포츈'},
        {value:'TFT8_Galio', name:'갈리오'},
        {value:'TFT8_Sivir', name:'시비르'},
        {value:'TFT8_Janna', name:'잔나'},
        {value:'TFT8_Taliyah', name:'탈리야'},
        {value:'TFT8_Lux', name:'럭스'},
        {value:'TFT8_Nilah', name:'닐라'},
        {value:'TFT8_Kaisa', name:'카이사'},
        {value:'TFT8_Rell', name:'렐'},
        {value:'TFT8_Ekko', name:'에코'},
        {value:'TFT8_Syndra', name:'신드라'},
        {value:'TFT8_Sett', name:'세트'},
        {value:'TFT8_Draven', name:'드레이븐'},
        {value:'TFT8_Leona', name:'레오나'},
        {value:'TFT8_Jax', name:'잭스'},
        {value:'TFT8_Sejuani', name:'세주아니'},
        {value:'TFT8_Ashe', name:'애쉬'},
        {value:'TFT8_Senna', name:'세나'},
        {value:'TFT8_Zed', name:'제드'},
        {value:'TFT8_Mordekaiser', name:'모데카이저'},
        {value:'TFT8_Annie', name:'애니'},
        {value:'TFT8_Fiora', name:'피오라'},
        {value:'TFT8_Alistar', name:'알리스타'},
        {value:'TFT8_Aphelios', name:'아펠리오스'},
        {value:'TFT8_Viego', name:'비에고'},
        {value:'TFT8_Kayle', name:'케일'},
        {value:'TFT8_Vi', name:'바이'},
        {value:'TFT8_Sona', name:'소나'},
        {value:'TFT8_Lulu', name:'룰루'},
        {value:'TFT8_Zoe', name:'조이'},
        {value:'TFT8_Nunu', name:'누누'},
        {value:'TFT8_Blitzcrank', name:'블리츠크랭크'},
        {value:'TFT8_Camille', name:'카밀'},
        {value:'TFT8_Gangplank', name:'갱플랭크'},
        {value:'TFT8_LeeSin', name:'리 신'},
        {value:'TFT8_Malphite', name:'말파이트'},
        {value:'TFT8_Velkoz', name:'벨코즈'},
        {value:'TFT8_Chogath', name:'초가스'},
        {value:'TFT8_AurelionSol', name:'아우렐리온 솔'},
        {value:'TFT8_Rammus', name:'람머스'},
        {value:'TFT8_BelVeth', name:'벨베스'},
        {value:'TFT8_Zac', name:'자크'},
        {value:'TFT8_Urgot', name:'우르곳'},
        {value:'TFT8_Fiddlesticks', name:'피들스틱'},
        {value:'TFT8_Yuumi', name:'유미'},
        {value:'TFT8_Yasuo', name:'야스오'},
        {value:'TFT8_Poppy', name:'뽀삐'},
        {value:'TFT8_Talon', name:'탈론'},
        {value:'TFT8_Renekton', name:'레넥톤'},
        {value:'TFT8_WuKong', name:'오공'},
        {value:'TFT8_Ezreal', name:'이즈리얼'},
        {value:'TFT8_Soraka', name:'소라카'},
        {value:'TFT8_Leblanc', name:'르블랑'},
    ]

    const dispatch = useDispatch<AppDispatch>();
    const [selectedChamp, setSelectedChamp] = useState<string>("")
    const [ready, setReady] = useState<boolean>(false);
    const itemForUnit = useSelector(selectitemforunit);
    const baseitems = useSelector(selectbaseitems);
    useEffect(()=>{
        if (selectedChamp!==""){
            setReady(true)
        }
    },[itemForUnit])
    
    useEffect(()=>{
        dispatch(fetchItems())
    },[])
    const championSelectHandler= () =>{
        if (selectedChamp!=="")
        {   setReady(false)
            console.log(selectedChamp)
            dispatch(fetchItemForUnit(selectedChamp))
        }
    }
        return(
        <div className='page'>
            <Header />
            <div className='content'>
                <div id='title'>
                    <text className="title-text">챔피언 별 아이템 랭킹</text>
                </div>
                <div className='champion-select'>
                    <select id="champion-select" onChange={(e:any)=>setSelectedChamp(e.target.value)}
                    defaultValue={CHAMPION_OPTION[0].value}>
                        {CHAMPION_OPTION.map((option)=>(
                            <option
                            key={option.value}
                            value={option.value}
                            >{option.name}</option>
                        ))}
                    </select>
                    <button className='navigate-btn' onClick={championSelectHandler}>찾기</button>
                </div>
                {ready?
                    <div className = 'item-info-box' id = 'item-info-box'>
                        <div id='sub-title'>
                            <text className="title-text">아이템</text>
                        </div>
                        {itemForUnit.map((e:RiotUpperItemType)=>{
                            return <ItemInfo itemName={e.name} itemImg={e.img} itemDetail={e.info} itemCombination={e.baseItems} base_item_list={baseitems}/>})
                        }
                    </div>
                    :<></>
                }
            </div>
        </div>
    )
}
export default ItemForUnit;