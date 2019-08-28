var express = require('express');
var app = express();
var http = require('http').Server(app);
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

var server = app.listen(3001, ()=>{
    console.log("app started on port 3001");
});

var io = require('socket.io').listen(server);

const { Kafka } = require('kafkajs')

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['kafka:9092']
})

//const producer = kafka.producer()
const consumer = kafka.consumer({ groupId: 'group1' })

const run = async () => {


    // Consuming
    await consumer.connect()
    await consumer.subscribe({ topic: 'media_stelle', fromBeginning: false })

    var cont=0

    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            cont++

            var latlng= message.value.toString().replace("\n","")

            console.log(cont, latlng)


            callSockets(io, latlng);


        },
    })
}

run().catch(console.error)


function callSockets(io, message){
    io.sockets.emit('update', message);}



//viene richiamata quando dal barchart si è cliccato su una barra, message rappresenta il nome dell'attività della barra
io.on('connection', function (socket) {
    socket.on('update2', function (message) {
        console.log("è stato cliccato su -> " + message)
        io.sockets.emit('update3',message) //al canale update3 è in ascolto googlemaps
    });

//viene richiamata quando da googlemaps si è cliccato su "vai alla top 15", message rappresenta il nome dell'attività del marker
    socket.on('update4', function (message) {
        console.log("è stato cliccato su -> " + message)
        io.sockets.emit('update5',message) //al canale update5 è in ascolto il barchart
    });



});












