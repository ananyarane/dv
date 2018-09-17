function setup() {
  createCanvas(500,500);
  background(220);
  noFill();
  strokeWeight(2);
}
var r = false, x = 0, y =200, speed =25
function draw() 
{
  clear();
  ellipse(x,y,100,100);
  if (x > width-50)
  {
    r = 3
    if (speed > 0)
      speed = speed - 2
    else
      speed = 0
  }
  if ( x < 50)
  {
    r = 1
    if (speed > 0)
      speed = speed - 2
    else
      speed = 0
  }
  if ( r == 1)
  {
    if (speed > 0)
      x = x + speed;
    else
      speed = 0
  }
  if (r == 3)
  {
    if (speed > 0)
      x = x - speed;
    else
      speed = 0
  }
  if (speed < 0)
  {
    speed = 0
  }
}