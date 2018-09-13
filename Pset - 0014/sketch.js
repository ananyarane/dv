var input, button, greeting;

function setup() {
  createCanvas(400, 400);
  fill(0);
  input = createInput();
  input.position(20, 65);

  button = createButton('submit');
  button.position(input.x + input.width, 65);
  button.mousePressed(factorial);

  greeting = createElement('h2', 'Enter a number');
  greeting.position(20, 5);

  textAlign(CENTER);
  textSize(50);
}
function factorial() {

  var n = parseInt(input.value());
  var f = 1;
  for (var i = 1; i <= n; i++) {
    f = f * i;
  }
  print(f);
  strokeWeight(2);
  fill(0);
  text(f, 200, 200);
}