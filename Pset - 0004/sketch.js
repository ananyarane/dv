
function setup()
{
  createCanvas(400,400);
  strokeWeight(2);
  noFill();
}

var x=400,y=400,u=65,g=9.8,t,pi=3.14,th=pi/4,t=0;
var px,py;
function draw()
{
  clear()
  x = u*cos(th)*t;
  y = 400-(u*sin(th)*t - 0.5*g*t*t);
  ellipse(x,y,10,10);
  t = t + 0.2;

}