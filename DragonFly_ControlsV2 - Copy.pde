import cc.arduino.*;
import org.firmata.*;

import org.gamecontrolplus.gui.*;
import org.gamecontrolplus.*;
import net.java.games.input.*; 
import processing.net.*; 

Client myClient;
ControlIO control;
Configuration config;
ControlDevice gpad;

//ControlButton R1;

ControlSlider Lx;
ControlSlider Ly;
ControlSlider Rx;
ControlSlider Ry;

int val = 0;
String[] badVals = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
void setup() { 
  size(200, 200); 
  
  control = ControlIO.getInstance(this);
  
  gpad = control.getDevice("Controller (XBOX 360 For Windows)");
  
  if (gpad == null) {
    println("No suitable device configured");
    System.exit(-1);
  }
  myClient = new Client(this, "192.168.137.94", 9999);
  
  //R1 = gpad.getButton(5);
  Lx = gpad.getSlider(Y);
  Ly = gpad.getSlider(X);
  Rx = gpad.getSlider("X Rotation");
  Ry = gpad.getSlider("Y Rotation");
  //RandL2 = gpad.getSlider("Z Axis");
  } 


void draw() {
  int[] vals = new int[4];
  int LxVAL = int(map(Lx.getValue(), -1, 1, 20, 0));
  vals[0] = LxVAL;
  int LyVAL = int(map(Ly.getValue(), -1, 1, 99, 0));
  vals[1] = LyVAL;
  int RxVAL = int(map(Rx.getValue(), -1, 1, 20, 0));
  vals[2] = RxVAL;
  int RyVAL = int(map(Ry.getValue(), -1, 1, 20, 0));
  vals[3] = RyVAL;

  
  String joinedVals = join(nf(vals, 2), " ");

  myClient.write(joinedVals);
  println(joinedVals);
}