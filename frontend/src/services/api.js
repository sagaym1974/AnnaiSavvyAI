import axios from "axios";

const API_URL =
    import.meta.env.VITE_API_URL ||
    "https://annaisavvyai.onrender.com/api";

const api = axios.create({

    baseURL: API_URL,

    timeout: 30000,

    headers: {

        "Content-Type": "application/json"

    }

});

api.interceptors.request.use(

    (config) => {

        console.log("REQUEST", config.baseURL + config.url);

        return config;

    },

    (error) => Promise.reject(error)

);

api.interceptors.response.use(

    (response) => response,

    (error) => Promise.reject(error)

);

export default api;