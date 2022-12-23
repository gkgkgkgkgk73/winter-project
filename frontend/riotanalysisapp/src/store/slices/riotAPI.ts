import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { RootState } from "..";

export interface RiotItemType{
    id:number;
}

export interface ItemState {
    item:RiotItemType[];
}

const initialItemState: ItemState ={
    item:[],
}

// const initailState: = {
// }

export const fetchItems = createAsyncThunk(
    "item/fetchItems",
    async()=>{
        const response = await axios.get<RiotItemType[]>("/api/items/");
        return response.data;
    }
)

// export const riotAPI = createSlice({
//     name:'riotAPIs',
//     initialState,
//     reducers:{
        
//     },
//     extraReducers: (builder) => {
//         builder.addCase(fetchItems.fulfilled, (state, action)=>{
//             state.item = action.payload;
//         });
//         builder.addCase(fetchItems.rejected, (state, action)=>{
//             state.item = null
//         });

//     }

// })

// export const riotAPIActions = riotAPI.actions;
// export const selectAPI = (state:RootState) => state.riotAPI;

// export default riotAPI.reducer;