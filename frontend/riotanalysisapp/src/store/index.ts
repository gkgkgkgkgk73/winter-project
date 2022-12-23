import {configureStore } from "@reduxjs/toolkit";
// import riotAPIReducer from "./slices/riotAPI";
export const store = configureStore({
    reducer:{
        // riotAPI: riotAPIReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export type AppStore = typeof store;