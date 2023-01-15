import React, {useState} from 'react';
import './Header.css';
import { useNavigate } from 'react-router-dom';
import DropDown from '../DropDown/DropDown';
import styled, { css } from 'styled-components';

function Header(){


    const [isOpen, setIsOpen] = useState(false);
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
                <text onClick={onClickLogoHandler}>롤체 정보</text>
            </div>
            <ul className='page-list'>
                <div className = 'menu-list'>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' onClick={explanationHandler}>롤토체스 설명</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' href='#trait-info-box'>
                                        특성
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' href='#item-info-box'>
                                        아이템
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' href='#augment-info-box'>
                                        증강체
                                    </a>
                                </li>
                            </ul>
                            :<></>
                        }
                    </div>
                    <div id='menu-obj'>
                        <button id = 'navigate-btn' onClick={explanationHandler}>롤토체스 분석</button>
                        {isOpen?
                            <ul id='dropdown-menu' >
                                <li>
                                    <a id = 'navigate-btn' href='#trait-info-box'>
                                        특성과 증강체
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' href='#item-info-box'>
                                        유닛과 아이템
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' href='#augment-info-box'>
                                        유닛과 증강체
                                    </a>
                                </li>
                                <li>
                                    <a id = 'navigate-btn' href='#augment-info-box'>
                                        가장 승률 높은 덱
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

