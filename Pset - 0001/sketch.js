function setup() {
  createCanvas(400, 400);
	background(220);
	noFill();
	strokeWeight(2);
}
var r = false, x = 0, y =200
function draw() {
	clear();
	ellipse(x,y,100,100);
	if (x == width-50)
	{
		r = true
	}
	if ( x == 50)
	{
		r = false
	}
	if ( r == false)
		x = x + 2;
	else
		x = x - 2;
	
}