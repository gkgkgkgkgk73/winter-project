import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { RootState } from "..";
import ItemInfo from "../../component/ItemInfo/ItemInfo";
import { stat } from "fs";
import { act } from "react-dom/test-utils";

export interface UserInfoType{
    id:string;
    iconImg:number;
    level:number;
    matchHistory:JSON;
    gameStat:JSON;
}


export interface DiceReqType{
    type:number,
    level:number,
    name:string
}
export interface DiceStatType{
    champion_name:string;
    stat:number;
}

export interface DiceStatInfo{
    diceStat:DiceStatType[];
    targetChampion:string;
}

export interface RiotUpperItemType{
    id:number;
    name:string;
    img:string;
    info:string;
    apiName:string;
    effect:JSON;
    baseItems:number[];
}

export interface RiotBaseItemType{
    id:number;
    name:string;
    img:string;
    info:string;
    apiName:string;
    effect:JSON;
}

export interface ItemState {
    upperItems:RiotUpperItemType[];
    baseItems:RiotBaseItemType[];
}

export interface RiotTraitType{
    name:string;
    apiName:string;
    img:string;
    id:number;
    effect:JSON;
    info:string;
}

export interface TraitState {
    traits:RiotTraitType[];
}

export interface RiotChampionType {
    apiName:string;
    id:number;
    variables:JSON;
    name:string;
    img:string;
    info:string;
    traits:number[];
    championStats:JSON;
    championCost:number;
}

export interface ChampionState {
    champions:RiotChampionType[];
}

export interface RiotAugmentType{
    apiName:string;
    info:string;
    img:string;
    id:number;
    name:string;
    effect:JSON;
}

export interface AugmentState {
    augments:RiotAugmentType[];
}

export interface AugmentRank {
    rank:number;
    augmentName:string;
    img:string;
    winRate:number;
    pickRate:number;
}

export interface BasicGameInfo {
    item:ItemState;
    champion:ChampionState;
    augment:AugmentState;
    trait:TraitState;
    augmentRank:AugmentRank[];
    userinfo:UserInfoType[];
    dicestat:DiceStatInfo;
}

const initialState:BasicGameInfo= {
    item:{
        upperItems:[],
        baseItems:[]
    },
    champion:{
        champions:[]
    },
    augment:{
        augments:[]
    },
    trait:{
        traits:[]
    },
    augmentRank:[],
    userinfo:[],
    dicestat:{
        diceStat:[],
        targetChampion:"",
    },

}

export const fetchItems = createAsyncThunk(
    "riotAPI/fetchItems",
    async()=>{
        const response = await axios.get<{upper_items:RiotUpperItemType[], base_items:RiotBaseItemType[]}>("/api/riotanalysisapp/item/");
        return response.data;
    }
)

export const fetchAugments = createAsyncThunk(
    "riotAPI/fetchAugments",
    async()=>{
        const response = await axios.get<RiotAugmentType[]>("/api/riotanalysisapp/augment/");
        return response.data;
    }
)

export const fetchAugmentsRank = createAsyncThunk(
    "augment/fetchAugmentsRank",
    async()=>{
        const response = await axios.get<AugmentRank[]>("/api/augmentstat/");
        return response.data;
    }
)

export const fetchTraits = createAsyncThunk(
    "riotAPI/fetchTraits",
    async()=>{
        const response = await axios.get<RiotTraitType[]>("/api/riotanalysisapp/trait/");
        return response.data;
    }
)

export const fetchTrait = createAsyncThunk(
    "riotAPI/fetchTrait",
    async(id:number) => {
        const response = await axios.post<RiotTraitType>(`/api/riotanalysisapp/trait/${id}`)
        return response.data;
    }
)

export const fetchChampions = createAsyncThunk(
    "riotAPI/fetchChampions",
    async()=>{
        const response = await axios.get<RiotChampionType[]>("/api/riotanalysisapp/champion/");
        return response.data;
    }
)

export const fetchUserInfo = createAsyncThunk("riotAPI/fetchUserInfo",
async(userid:string)=>{
    const response = await axios.post<UserInfoType>(`/api/riotanalysisapp/userinfo/${encodeURIComponent(userid)}`);
    console.log(response.data)
    return response.data;
})

export const fetchDiceStat = createAsyncThunk("riotAPI/fetchDiceStat",
    async(req:DiceReqType)=>{
        const response = await axios.post<DiceStatInfo>(`/api/riotanalysisapp/dicestat/`,req);
        console.log(response.data)
        return response.data;
    }
)

export const riotAPI = createSlice({
    name:'riotAPI',
    initialState,
    reducers:{
        fetchAugmentsRank: (state, action: PayloadAction<AugmentRank[]>) => {
            state.augmentRank = action.payload
            console.log(state)
            return state
        },
        fetchAugments: (state, action: PayloadAction<RiotAugmentType[]>) => {
            console.log("1")
            state.augment.augments = action.payload
            return state
        },
        fetchItems: (state, action: PayloadAction<{upper_items:RiotUpperItemType[], base_items:RiotBaseItemType[]}>) => {
            state.item.upperItems = action.payload.upper_items;
            state.item.baseItems = action.payload.base_items;
            return state
        },
        fetchTraits: (state, action: PayloadAction<RiotTraitType[]>) => {
            state.trait.traits = action.payload
            return state
        },
        fetchChampions: (state, action: PayloadAction<RiotChampionType[]>) => {
            state.champion.champions = action.payload
            return state
        },
        fetchUserInfo:(state, action: PayloadAction<UserInfoType>) => {
            state.userinfo=[];
            state.userinfo.push(action.payload);
            return state
        },
        fetchDiceStat:(state, action: PayloadAction<DiceStatInfo>) => {
            state.dicestat = action.payload;
            return state
        },
        // fetchAugments: (state, action: PayloadAction<RiotAugmentType[]>) => {
		// 	console.log(action.payload)
        //     state.augment.augments = action.payload;
		// },
        // fetchTraits: (state, action: PayloadAction<RiotTraitType[]>) => {
		// 	console.log(action.payload)
        //     state.trait.traits = action.payload;
		// },
        // fetchChampions: (state, action: PayloadAction<RiotChampionType[]>) => {
		// 	console.log(action.payload)
        //     state.champion.champions = action.payload;
		// },
        // fetchItems: (state, action: PayloadAction<{upper_items:RiotUpperItemType[], base_items:RiotBaseItemType[]}>) => {
		// 	console.log(action.payload)
        //     state.item.upperItems = action.payload.upper_items;
        //     state.item.baseItems = action.payload.base_items;
		// },
    },
    extraReducers: (builder) => {
        builder.addCase(fetchItems.fulfilled, (state, action)=>{
            state.item.upperItems = action.payload.upper_items;
            state.item.baseItems = action.payload.base_items;
            console.log(state.item.upperItems)
            return state;
        });
        builder.addCase(fetchItems.rejected, (state, action)=>{
            state.item = {
                upperItems:[],
                baseItems:[]
            }
            console.log(action.error)
        });

        builder.addCase(fetchAugments.fulfilled, (state, action)=>{
            state.augment.augments = []
            state.augment.augments = action.payload;
            return state;
        });
        builder.addCase(fetchAugments.rejected, (state, action)=>{
            state.augment.augments = [];
            console.log(action.error)
        });

        builder.addCase(fetchTraits.fulfilled, (state, action)=>{
            state.trait.traits = []
            state.trait.traits = action.payload;
            return state;
        });
        builder.addCase(fetchTraits.rejected, (state, action)=>{
            state.trait.traits = [];
            console.log(action.error)
        });

        builder.addCase(fetchChampions.fulfilled, (state, action)=>{
            state.champion.champions = []
            state.champion.champions = action.payload;
            return state;
        });
        builder.addCase(fetchChampions.rejected, (state, action)=>{
            state.champion.champions= [];
            console.log(action.error)
        });

        builder.addCase(fetchUserInfo.fulfilled, (state, action)=>{
            state.userinfo = []
            state.userinfo.push(action.payload);
            return state;
        });
        builder.addCase(fetchUserInfo.rejected, (state, action)=>{
            state.userinfo= [];
            console.log(action.error)
        });


        builder.addCase(fetchDiceStat.fulfilled, (state, action)=>{
            state.dicestat = action.payload;
            return state;
        });
        builder.addCase(fetchDiceStat.rejected, (state, action)=>{
            state.dicestat= {diceStat:[], targetChampion:""};
            console.log(action.error)
        });
    }

})

export const riotAPIActions = riotAPI.actions;
export const selectaugment = (state:RootState) => state.riotAPI.augment;
export const selecttrait = (state:RootState) => state.riotAPI.trait;
export const selectchampion = (state:RootState) => state.riotAPI.champion;
export const selectupperitems = (state:RootState) => state.riotAPI.item.upperItems;
export const selectbaseitems = (state:RootState) => state.riotAPI.item.baseItems;
export const selectuserinfo = (state:RootState) => state.riotAPI.userinfo;
export const selectdicestat = (state:RootState) => state.riotAPI.dicestat;
export default riotAPI.reducer;