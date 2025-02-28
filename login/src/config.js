const mongoose = require("mongoose");
const connect = mongoose.connect("mongodb://localhost:27017/login-data");

connect.then(()=>{
    console.log("Database connected Sucessfully");
})
.catch(()=>{
    console.log("Database cannot connected");
});

//schema bna hai aab
const LoginSchema = new mongoose.Schema({
    name:{
        type: String,
        required:true
    },
    password:{
        type: String,
        required:true
    }
});

const collection = new mongoose.model("users",LoginSchema);

module.exports = collection;

