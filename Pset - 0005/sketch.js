function setup() {
  createCanvas(600, 400);
	background(220);
	noFill();
	strokeWeight(2);
}
var r = false,l = false , x = 50, x1 = 600 - 50, y =200;
function draw() {
	clear();
	ellipse(x1,y,100,100);
	ellipse(x,y,100,100);
	if (x == width-50)
	{
		r = true
		l = false
	}
	
		
	if ( x == 50)
	{
		r = false
		l = true
	}
	if ( r == false)
	{
		x = x + 2;
		x1 = x1 - 2;
	}
	else
	{
		x = x - 2;
		x1 = x1 + 2;
	}
}