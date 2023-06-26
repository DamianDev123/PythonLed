var x,y = 0;
var socket = io();
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  rect(x,y,100)
  socket.emit('newPos', 0);
}
socket.on('UpdatedKeys', function (msg) {
    x+=msg['x']
    y+=msg['y']
})