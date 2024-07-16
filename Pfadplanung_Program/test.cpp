#include <MeMCore.h>

// Initialize motors
MeDCMotor motorLeft(M1);
MeDCMotor motorRight(M2);

// Function to move forward
void moveForward(int speed, int duration) {
  motorLeft.run(speed);
  motorRight.run(speed);
  delay(duration);
  stop();
}

// Function to move backward
void moveBackward(int speed, int duration) {
  motorLeft.run(-speed);
  motorRight.run(-speed);
  delay(duration);
  stop();
}

// Function to turn left
void turnLeft(int speed, int duration) {
  motorLeft.run(-speed);
  motorRight.run(speed);
  delay(duration);
  stop();
}

// Function to turn right
void turnRight(int speed, int duration) {
  motorLeft.run(speed);
  motorRight.run(-speed);
  delay(duration);
  stop();
}

// Function to stop the motors
void stop() {
  motorLeft.run(0);
  motorRight.run(0);
}

void setup() {
  // Set up serial communication for debugging
  Serial.begin(9600);
}

void loop() {
  // Example usage
  moveForward(100, 2000);  // Move forward at speed 100 for 2 seconds
  moveBackward(100, 2000); // Move backward at speed 100 for 2 seconds
  turnLeft(100, 1000);     // Turn left at speed 100 for 1 second
  turnRight(100, 1000);    // Turn right at speed 100 for 1 second
  
  // Ensure the mBot stops
  stop();

  // Wait for a while before repeating the actions
  delay(5000);
}
