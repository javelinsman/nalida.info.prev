var express = require('express')
var http = require('http')
var path = require('path')

var app = express()
app.use(express.static('html'))
app.use(express.static('css'))
app.use(express.static('js'))
app.use('/static', express.static('static'))

http.createServer(app).listen(55007, '172.31.10.167')

app.get('/', (req, res) => {
    console.log('GET /')
    res.sendFile(path.join(__dirname, '/html/index.html'));
});

console.log('nalida.info running')
