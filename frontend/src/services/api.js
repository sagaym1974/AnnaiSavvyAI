import axios from "axios";

const api = axios.create({

    baseURL: "http://127.0.0.1:8000/api",

    timeout: 30000,

    headers: {

        "Content-Type": "application/json"

    }

});

// ------------------------------------------------------
// Request Logger
// ------------------------------------------------------

api.interceptors.request.use(

    (config) => {

        console.log(

            "========================================"

        );

        console.log(

            "REQUEST"

        );

        console.log(

            "URL :",

            config.baseURL + config.url

        );

        console.log(

            "METHOD :",

            config.method

        );

        console.log(

            "========================================"

        );

        return config;

    },

    (error) => {

        console.error(

            error

        );

        return Promise.reject(error);

    }

);

// ------------------------------------------------------
// Response Logger
// ------------------------------------------------------

api.interceptors.response.use(

    (response) => {

        console.log(

            "========================================"

        );

        console.log(

            "SUCCESS"

        );

        console.log(

            response.data

        );

        console.log(

            "========================================"

        );

        return response;

    },

    (error) => {

        console.log(

            "========================================"

        );

        console.log(

            "API ERROR"

        );

        if (error.response) {

            console.log(

                error.response.status

            );

            console.log(

                error.response.data

            );

        }

        else {

            console.log(

                error.message

            );

        }

        console.log(

            "========================================"

        );

        return Promise.reject(error);

    }

);

export default api;