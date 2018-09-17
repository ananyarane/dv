
var input, input1, button1, greeting;

function setup() {
  createCanvas(400, 400);
  fill(0);
  strokeWeight(2);
  input = createInput();
  input1 = createInput();
  input.position(20, 65);
  input1.position(150,65);

  button1 = createButton('submit');
  button1.position(input1.x + input1.width, 65);
  button1.mousePressed(projectile);

  greeting = createElement('h2', 'Enter u and theta');
  greeting.position(20, 5);

  textAlign(CENTER);
  textSize(50);
  noLoop();
}

var x=400,y=400,g=9.8,pi=3.14,t=0,u,th;
var px,py;

function projectile()
{
  u = parseInt(input.value());
  th = parseInt(input1.value());
  th = th * (3.14/180);
  loop();
}

function draw()
{
  clear();
  x = u*cos(th)*t;
  y = 400-(u*sin(th)*t - 0.5*g*t*t);
  ellipse(x,y,20,20);
  t = t + 0.2;

}