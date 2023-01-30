import React, {useState} from 'react';
import './Header.css';
import { useNavigate } from 'react-router-dom';
import DropDown from '../DropDown/DropDown';
import styled, { css } from 'styled-components';

function Header(){


    const [isOpen, setIsOpen] = useState(false);
    const [searchID, setSearchID] = useState('');
    const searchIDHandler = ()=>{
        //search 처리 함수
    }
    // const [explanationIsOpen, explanationRef, explanationHandler] = DropDown(false);
    const explanationHandler = () => {
        setIsOpen(!isOpen)
    }
    
    const onClickLogoHandler = () => {
        return navigate('/')
    }
    const navigate = useNavigate();

    return (
        <div className='header'>
            <div className='logo'>
                <text onClick={onClickLogoHandler}>TFTInfo</text>
                <form onSubmit={searchIDHandler}>
                    <input id='search-id-window' value={searchID} placeholder='소환사 이름을 입력하세요.' onChange={(e)=>setSearchID(e.target.value)}></input>
                    <button type='submit'>검색</button>
                </form>
            </div>
            <ul className='page-list'>
                <div className = 'menu-list'>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' style={{fontSize:'2vh'}} onClick={explanationHandler}>TFT 시즌 8 정보</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#trait-info-box'>
                                        시너지
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#item-info-box'>
                                        아이템
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        증강체
                                    </a>
                                </li>
                            </ul>
                            :<></>
                        }
                    </div>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' style={{fontSize:'2vh'}} onClick={explanationHandler}>TFT 시즌 8 추천 메타</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#trait-info-box'>
                                        특성과 증강체
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#item-info-box'>
                                        유닛과 아이템
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn'style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        유닛과 증강체
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        가장 승률 높은 덱
                                    </a>
                                </li>
                            </ul>
                            :<></>
                        }
                    </div>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' style={{fontSize:'2vh'}} onClick={explanationHandler}>통계</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#trait-info-box'>
                                        아이템 승률 계산
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#item-info-box'>
                                        챔피언 승률 계산
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn'style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        챔피언 별 아이템 승률 계산
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        가장 승률 높은 덱
                                    </a>
                                </li>
                            </ul>
                            :<></>
                        }
                    </div>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' style={{fontSize:'2vh'}} onClick={explanationHandler}>랭킹</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#trait-info-box'>
                                        특성과 증강체
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#item-info-box'>
                                        유닛과 아이템
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn'style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        유닛과 증강체
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        가장 승률 높은 덱
                                    </a>
                                </li>
                            </ul>
                            :<></>
                        }
                    </div>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' style={{fontSize:'2vh'}} onClick={explanationHandler}>유저 통계</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#trait-info-box'>
                                        내가 주로 무슨 덱 할 때 승률 높은지
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#item-info-box'>
                                        등등
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn'style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        등등
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' style={{paddingLeft:'5px'}} href='#augment-info-box'>
                                        등등
                                    </a>
                                </li>
                            </ul>
                            :<></>
                        }
                    </div>
                </div>
                {/* <Link id = 'navigate-btn' to='/decinfo'>롤토체스 순위 덱 알아보기</Link>
                <Link id = 'navigate-btn' to='/augmentstat'>롤토체스 승률 높은 증강체 알아보기</Link>
                <Link id = 'navigate-btn' to='/suggestion'>건의사항</Link> */}
            </ul>
        </div>
    );
    
}

export default Header;

