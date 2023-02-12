#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver mod_1 = Adafruit_PWMServoDriver(0x40);
int zero_count = 0;
#define SERVOMIN  90 //độ dài xung tối thiểu; xung PPM
#define SERVOMAX  600

int topulse(int goc) //chuyển góc thành xung
{
  int xung = map(goc, 0, 180, SERVOMIN, SERVOMAX);
  return xung;
}

void setup() 
{
  Serial.begin(115200);

  mod_1.begin();
  mod_1.setOscillatorFrequency(27000000);
  mod_1.setPWMFreq(60);
  Zero_degree_set();

}

void loop() 
{
  
  while (zero_count = 0){
    Zero_degree_set();
  }
  zero_count += 1;

  
}
void Zero_degree_set(){
  for (int i = 0; i < 2; i++){
    mod_1.setPWM(i, 0, topulse(10));
    delay(100);
  }
}