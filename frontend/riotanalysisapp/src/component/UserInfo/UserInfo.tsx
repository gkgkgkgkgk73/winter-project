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
        </div>
        :
        searched?
        <></>
        :
        <></>
    )
}

export default UserInfo;