var x = 150
var y = 150
var socket = io();
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  rect(x,y,100)
}
socket.on('UpdatedKeys', function (msg) {
    x+=msg[0]
    y+=msg[1]
})