import React from 'react';
import './Header.css';
import { useNavigate } from 'react-router-dom';
function Header(){
    const navigate = useNavigate();
    const onClickExplanationHandler = () => {
        navigate('/');
    }
    const onClickDecInfoHandler = () => {
        navigate('/DecInfo');
    }
    const onClickAugmentsHandler = () => {
        navigate('/Augments');
    }
    const onClickSuggestionHandler = () => {
        navigate('/Suggestion');
    }
    return (
        <div className='header'>
            <div className='logo'>
                <text>롤체 정보</text>
            </div>
            <div className='page-list'>
                <button id = 'navigate-btn' onClick={onClickExplanationHandler}>롤토체스 설명</button>
                <button id = 'navigate-btn' onClick={onClickDecInfoHandler}>롤토체스 순위 덱 알아보기</button>
                <button id = 'navigate-btn' onClick={onClickAugmentsHandler}>롤토체스 승률 높은 증강체 알아보기</button>
                <button id = 'navigate-btn' onClick={onClickSuggestionHandler}>건의사항</button>
            </div>
        </div>
    );
}

export default Header;