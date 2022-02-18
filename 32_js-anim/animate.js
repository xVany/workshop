// Team HR :: Han Zhang, Raymond Yeung
// SoftDev
// K32: More Moving Parts
// 2022-02-17

//access canvas and buttons via DOM
var c = document.getElementById("playground")
var dotButton = document.getElementById("buttonCircle")
var stopButton = document.getElementById("buttonStop")
var screenSaver = document.getElementById("screensaver")
var image = new Image();

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d")

//set fill color to team color
ctx.fillStyle = "red"

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth, c.height)
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  console.log(requestID)
  console.log("drawDot invoked...")
  if (growing === true) {
    radius++;
    if (radius === ((c.clientHeight / 2) - 1)) {
      growing = false;
    }
  } 
  else {
    radius --
    if (radius === 1) {
      growing = true;
    }
  }
  // YOUR CODE HERE

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,

    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()

   */
  if (requestID) {
    window.cancelAnimationFrame(requestID)
  }

  ctx.clearRect(0, 0, c.clientWidth, c.height)
  ctx.beginPath();
  ctx.arc(c.clientWidth / 2, c.clientHeight / 2, radius, 0, 2 * Math.PI);
  ctx.fillStyle = "red";
  ctx.fill();
  ctx.stroke();
  requestID = window.requestAnimationFrame(drawDot);
  
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...");
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
  // YOUR CODE HERE
  /*
    ...to
    Stop the animation

    You will need
    window.cancelAnimationFrame()
  */
};

var x;
var y;
image.src = 'logo_dvd.jpg';
var xgrow = true;
var ygrow = true;

//var screen = function() {
var screen = () => {
  console.log("screensaver invoked...");
  console.log (requestID);
  if (requestID) {
    window.cancelAnimationFrame(requestID)
  }

  ctx.clearRect(0, 0, c.clientWidth, c.height);
  ctx.drawImage(image, x, y, 100, 50);

  if (xgrow === true) {
    x++;}
  else {
    x--;}

  if (ygrow === true) {
    y++;}
  else {
    y--;}

  if (x >= (c.clientWidth - 100)) {
    xgrow = false;
  }

  if (x <= 0) {
    xgrow = true;
  }

  if (y >= (c.clientHeight - 50)) {
    ygrow = false;;
  }

  if (y <= 0) {
    ygrow = true;
  }

  requestID = window.requestAnimationFrame(screen);
}

var randomCoord = () => {
  x = Math.random() * (c.clientWidth - 100);
  y = Math.random() * (c.clientHeight - 50);
}

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
screenSaver.addEventListener( "click", screen);
screenSaver.addEventListener( "click", randomCoord);
