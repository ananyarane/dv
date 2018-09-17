var img;
function preload() {
  img = loadImage('turtle.jpg');
}
var x, y;
function setup() {
  // Top-left corner of the img is at (0, 0)
  // Width and height are the img's original width and height
  x = 0;
  y =0;
  createCanvas(400,400);
  background(220);
  image(img,x,y,50,50);
  // noLoop();
}


function draw()
{
clear();
  image(img, x,y,50,50);
}

function keyPressed()
{
 
    
  if (keyCode === LEFT_ARROW)
    x = x - 5;
  else if (keyCode === RIGHT_ARROW)
    x = x + 5;
  else if (keyCode === UP_ARROW)
    y = y - 5;
  else if (keyCode === DOWN_ARROW)
    y = y+ 5;
  } 

