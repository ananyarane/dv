function setup()
{
  createCanvas(800,800);
  strokeWeight(2);
  noFill();
}
var x=0,x1,y;
function draw()
{

  translate(200,200);


    x1 = 100*cos(x*PI/3600)+100;
    y = 100*sin(x*PI/3600)+100;
    clear();
    x = x+10;
    ellipse(x1,y,20,20);
}