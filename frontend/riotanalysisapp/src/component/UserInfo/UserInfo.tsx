import React, { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { UserInfoType, fetchUserInfo, selectuserinfo } from '../../store/slices/riotAPI';
import './UserInfo.css';
import { AppDispatch } from '../../store';
import { useSelector } from 'react-redux';

//페이지 나갈 때 찾았던 유저 정보 지워버리기 꼭

function UserInfo() {

    const dispatch = useDispatch<AppDispatch>();
    const userInfo = useSelector(selectuserinfo);
    const [ready, setReady] = useState<boolean>(false);
    const [searched, setSearched] = useState<boolean>(false);
    const [id,setID] = useState<string>("");

    const searchIDHandler = ()=>{
        //search 처리 함수
        dispatch(fetchUserInfo(id))
        setSearched(true)
        setReady(false)
    }

    useEffect(()=>{
        if(userInfo[0].id!==""){
            setReady(true)
            setSearched(true)
        }
    })

    useEffect(()=>{
        if(searched){
            dispatch(fetchUserInfo(id));
            setReady(false);
        }
    },[searched])

    useEffect(()=>{
        setReady(true);
    },[userInfo])

    return(
        (searched && ready)?
        <div>
            <p>{userInfo[0].id}</p>
        </div>
        :
        searched?
        <div>
            <p>loading...</p>
        </div>
        :
        <div>
        <form onSubmit={searchIDHandler}>
            <input id='search-id-window' value={id} placeholder='소환사 이름을 입력하세요.' onChange={(e)=>setID(e.target.value)}></input>
            <button type='submit'>검색</button>
        </form>
        </div>
    )
}

export default UserInfo;