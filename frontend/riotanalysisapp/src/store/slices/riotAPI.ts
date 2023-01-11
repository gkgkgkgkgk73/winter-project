import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { RootState } from "..";
import ItemInfo from "../../component/ItemInfo/ItemInfo";
import { stat } from "fs";

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
        });

        builder.addCase(fetchAugments.fulfilled, (state, action)=>{
            state.augment.augments = []
            state.augment.augments = action.payload;
            return state;
        });
        builder.addCase(fetchAugments.rejected, (state, action)=>{
            state.augment.augments = [];
        });

        builder.addCase(fetchTraits.fulfilled, (state, action)=>{
            state.trait.traits = []
            state.trait.traits = action.payload;
            return state;
        });
        builder.addCase(fetchTraits.rejected, (state, action)=>{
            state.trait.traits = [];
        });

        builder.addCase(fetchChampions.fulfilled, (state, action)=>{
            state.champion.champions = []
            state.champion.champions = action.payload;
            return state;
        });
        builder.addCase(fetchChampions.rejected, (state, action)=>{
            state.champion.champions= [];
        });

    }

})

export const riotAPIActions = riotAPI.actions;
export const selectaugment = (state:RootState) => state.riotAPI.augment;
export const selecttrait = (state:RootState) => state.riotAPI.trait;
export const selectchampion = (state:RootState) => state.riotAPI.champion;
export const selectupperitems = (state:RootState) => state.riotAPI.item.upperItems;
export const selectbaseitems = (state:RootState) => state.riotAPI.item.baseItems;

export default riotAPI.reducer;