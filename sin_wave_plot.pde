float x = 0;

void setup()
{
  size (400,400);
  noFill();
  strokeWeight(2);
  
}

void draw()
{
  translate(0,200);
  float y = 50*-(sin(10*x));
  point(500*x,y);
  x = x+(2*PI/3600);
}
