/**
 * Noise3D. 
 * 
 * Using 3D noise to create simple animated texture. 
 * Here, the third dimension ('z') is treated as time. 
 */
 
float increment = 0.01;
// The noise function's 3rd argument, a global variable that increments once per cycle
float zoff = 0.0;  
// We will increment zoff differently than xoff and yoff
float zincrement = 0.02; 

float detail = 0.4;
boolean stopped =  false;


color blue = color(65, 105, 225, 60);
color beach = color(238, 214, 175);
color green = color(34, 140, 34); //34, 139, 34
color darkgreen = color(34, 100, 34);
color mountain = color(139, 137, 137);
color snow = color(255, 240, 255);

void setup() {
  size(800, 550);
  frameRate(30);
}

void draw() {
  
  // Optional: adjust noise detail here
  // noiseDetail(8,0.65f);
  
  loadPixels();

  float xoff = 0.0; // Start xoff at 0
  
  noiseDetail(9, detail);
  
  // For every x,y coordinate in a 2D space, calculate a noise value and produce a brightness value
  for (int x = 0; x < width; x++) {
    xoff += increment;   // Increment xoff 
    float yoff = 0.0;   // For every xoff, start yoff at 0
    for (int y = 0; y < height; y++) {
      yoff += increment; // Increment yoff
      
      // Calculate noise and scale by 255
      float bright = noise(xoff,yoff,zoff)*255;
      //print(str(bright) + "\n");
      
      if(bright <= 50) {
        pixels[x+y*width] = snow;
      } else if (bright > 50 && bright <= 60) {
        pixels[x+y*width] = mountain;
      } else if (bright > 60 && bright <= 90) {
        pixels[x+y*width] = darkgreen;
      } else if (bright > 90 && bright <= 115) {
        pixels[x+y*width] = green;
      } else if (bright > 115 && bright <= 120) {
        pixels[x+y*width] = beach;
      } else {
        pixels[x+y*width] = blue;
      }

      // Try using this line instead
      //float bright = random(0,255);
      
      // Set each pixel onscreen to a grayscale value
      //pixels[x+y*width] = color(bright,bright,bright);
    }
  }
  updatePixels();
  
  zoff += zincrement; // Increment zoff
  
}

void keyPressed(){
  if (key == ' ' && !stopped){
    noLoop();
    stopped = true;
  } else if (key == ' ' && stopped){
    loop();
    stopped = false;
  }
}
