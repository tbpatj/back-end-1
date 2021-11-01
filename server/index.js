const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const SERVER_PORT = 4000;


app.get("/api/users", (req, res) => {
    //send back a list of our friends to the client
    let friends = ['Nitin', 'Eric', "Jeddy", "Cameron", "Riley"];
    res.status(200).send(friends);
})

app.get("/weather/:temperature", (req, res) => {

    //destructure temperature for readabilty and give it back to the user in the form of an html
    const {temperature} = req.params;
    const phrase = `<h3>It was ${temperature} today</h3>`;
    res.status(200).send(phrase);
});

//Run the server
app.listen(SERVER_PORT, () => console.log(`Server Booted on ${SERVER_PORT}`));


