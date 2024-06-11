#include <MeMCore.h>

MeDCMotor motorLeft(M1);
MeDCMotor motorRight(M2);

const int motorSpeed = 100;
const int turnSpeed = 150;


void setup(){
    motorLeft.run(-motorSpeed);
    motorRight.run(motorSpeed);
    delay(1000);

    motorLeft.run(0);
    motorRight.run(0);
    delay(500);
    
    motorLeft.run(-turnSpeed);
    motorRight.run(-turnSpeed);
    delay(300);
    
    motorLeft.run(0);
    motorRight.run(0);
}


void loop(){

    
}