import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { RootState } from "..";

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
    effect:JSON;
    info:string;
}

export interface TraitState {
    traits:RiotTraitType[];
}

export interface RiotChampionType {
    apiName:string;
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

export interface BasicGameInfo {
    item:ItemState;
    champion:ChampionState;
    augment:AugmentState;
    trait:TraitState;
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
    }
}

export const fetchItems = createAsyncThunk(
    "item/fetchItems",
    async()=>{
        const response = await axios.get<{upper_items:RiotUpperItemType[], base_items:RiotBaseItemType[]}>("/api/items/");
        return response.data;
    }
)

export const fetchAugments = createAsyncThunk(
    "augment/fetchAugments",
    async()=>{
        const response = await axios.get<RiotAugmentType[]>("/api/augments/");
        return response.data;
    }
)

export const fetchTraits = createAsyncThunk(
    "trait/fetchTraits",
    async()=>{
        const response = await axios.get<RiotTraitType[]>("/api/traits/");
        return response.data;
    }
)

export const fetchTrait = createAsyncThunk(
    "trait/fetchTrait",
    async(id:number) => {
        const response = await axios.post<RiotTraitType>("/api/trait/",id)
        return response.data;
    }
)

export const fetchChampions = createAsyncThunk(
    "champion/fetchChampions",
    async()=>{
        const response = await axios.get<RiotChampionType[]>("/api/champions/");
        return response.data;
    }
)

export const riotAPI = createSlice({
    name:'riotAPIs',
    initialState,
    reducers:{
        
    },
    extraReducers: (builder) => {
        builder.addCase(fetchItems.fulfilled, (state, action)=>{
            state.item.upperItems = action.payload.upper_items;
            state.item.baseItems = action.payload.base_items;
        });
        builder.addCase(fetchItems.rejected, (state, action)=>{
            state.item = {
                upperItems:[],
                baseItems:[]
            }
        });

        builder.addCase(fetchAugments.fulfilled, (state, action)=>{
            state.augment.augments = action.payload;
        });
        builder.addCase(fetchItems.rejected, (state, action)=>{
            state.augment.augments = [];
        });

        builder.addCase(fetchTraits.fulfilled, (state, action)=>{
            state.trait.traits = action.payload;
        });
        builder.addCase(fetchItems.rejected, (state, action)=>{
            state.trait.traits = [];
        });

        builder.addCase(fetchChampions.fulfilled, (state, action)=>{
            state.champion.champions = action.payload;
        });
        builder.addCase(fetchChampions.rejected, (state, action)=>{
            state.champion.champions= [];
        });

    }

})

export const riotAPIActions = riotAPI.actions;
export const selectAPI = (state:RootState) => state.riotAPI;

export default riotAPI.reducer;