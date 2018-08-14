var x;
var y;
function setup()
{
  createCanvas(640,400);
  w = new Sketch();
}

function draw()
{
  background(51);
  w.walk();
  w.display();
  strokeWeight(5)
}

function Sketch()
{

  this.x = width/2;
  this.y = height/2;
}

this.walk = function()
{
  this.x = this.x + random(-10,10);
  this.y  = this.y + random(-10,10);
}

this.display = function()
{
  fill(255);
  ellipse(this.x,this.y,48,48);
}
