#include <Keypad.h>
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

//Khai báo Servo
Adafruit_PWMServoDriver mod_1 = Adafruit_PWMServoDriver(0x40);
#define SERVOMIN 90  //độ dài xung tối thiểu; xung PPM
#define SERVOMAX 600

int servo_pin1;
int servo_pin2;

int servo_pin[16] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
int Servo_pos1[8] = { 0, 140, 63, 53, 48, 80, 100, 40 };
int Servo_pos2[8] = { 0, 40, 53, 63, 70, 90, 106, 148 };

int topulse(int goc) {  //chuyển góc thành xung
  int xung = map(goc, 0, 180, SERVOMIN, SERVOMAX);
  return xung;
}

void Zero_degree_set(int pos) {
  for (int i = 0; i < 16; i++) {
    delay(100);
    mod_1.setPWM(i, 0, topulse(pos));
  }
}

//Khai báo Keypad
const byte ROWS = 4;  //four rows
const byte COLS = 2;  //four columns
const byte led = 2;
char hexaKeys[ROWS][COLS] = {
  { '1', '5' },
  { '2', '6' },
  { '3', '7' },
  { '4', '8' }
};
byte rowPins[ROWS] = { 6, 5, 4, 3 };  //connect to the row pinouts of the keypad
byte colPins[COLS] = { 7, 8 };        //connect to the column pinouts of the keypad
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

// Các biến trong chương trình này
int val;
int dem = 0;
int status = 1;
char customKey;
String test = "";
String data = "hello";
int demR = 0, demL = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Connected to braille display device");

  mod_1.begin();
  mod_1.setOscillatorFrequency(27000000);
  mod_1.setPWMFreq(60);
  delay(100);
  Zero_degree_set(13);
  delay(3000);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    //String data = "b14";
    Serial.print(data);
    servo_pin_setup(data);
    delay(100);
    braille_display(data);
    delay(100);
    keypad_encode();
  }
}

void servo_pin_setup(String data) {
  data = data;
  if (data[0] == 'k') {
    servo_pin1 = servo_pin[0];
    servo_pin2 = servo_pin[1];
    Serial.print("Servo2: ");
    Serial.println(servo_pin2);
    Serial.print("Servo1: ");
    Serial.println(servo_pin1);
  } else if (data[0] == 'l') {
    servo_pin1 = servo_pin[2];
    servo_pin2 = servo_pin[3];
  } else if (data[0] == 'm') {
    servo_pin1 = servo_pin[4];
    servo_pin2 = servo_pin[5];
  } else if (data[0] == 'n') {
    servo_pin1 = servo_pin[6];
    servo_pin2 = servo_pin[7];
  } else if (data[0] == 'o') {
    servo_pin1 = servo_pin[8];
    servo_pin2 = servo_pin[9];
  } else if (data[0] == 'p') {
    servo_pin1 = servo_pin[10];
    servo_pin2 = servo_pin[11];
  } else if (data[0] == 'q') {
    servo_pin1 = servo_pin[12];
    servo_pin2 = servo_pin[13];
  } else if (data[0] == 'r') {
    servo_pin1 = servo_pin[14];
    servo_pin2 = servo_pin[15];
  }
}

void braille_display(String data) {
  data = data;
  int demR = 0, demL = 0;
  char text[data.length()];

  for (int i = 0; i < data.length(); i++) {
    text[i] = data[i];
  }

  //123
  int i = 1;
  if (((int)text[i] - 48) < 4) {
    if (text[i] == '1' && text[i + 1] != '2' && text[i + 1] != '3') {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[1]));

    } else if (text[i] == '1' && text[i + 1] == '2' && text[i + 2] != '3') {

      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[2]));

    } else if (text[i] == '1' && text[i + 1] == '2' && text[i + 2] == '3') {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[3]));

    } else if (text[i] == '2' && text[i + 1] == '3') {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[4]));

    } else if (text[i] == '3') {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[7]));

    } else if (text[i] == '1' && text[i + 1] == '3') {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[5]));

    } else if (text[i] == '2' && text[i + 1] != '3') {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[6]));

    } else {
      mod_1.setPWM(servo_pin1, 0, topulse(Servo_pos1[0]));
    }

    //456

    for (int i = 1; i < data.length(); i++) {
      if (((int)text[i] - 48) > 3) {
        demR += 1;
      }
      if (((int)text[i] - 48) < 4) {
        demL += 1;
      }
    }

    i = demL + 1;
    Serial.print("DemR: ");
    Serial.println(demR);
    Serial.print("DemL: ");
    Serial.println(demL);
    Serial.print("text[i]: ");
    Serial.println(text[i]);

    if (demR == 1) {
      if (text[i] == '4') {
        mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[1]));

      } else if (text[i] == '5') {
        mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[6]));

      } else if (text[i] == '6') {
        mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[7]));
      }
    } else if (demR == 2) {
      if (text[i] == '4' && text[i + 1] == '5') {
        mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[2]));

      } else if (text[i] == '5' && text[i + 1] == '6') {
        mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[4]));

      } else if (text[i] == '4' && text[i + 1] == '6') {
        mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[5]));
      }
    } else if (text[i] == '4' && text[i + 1] == '5' && text[i + 2] == '6') {
      mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[3]));

    } else {
      mod_1.setPWM(servo_pin2, 0, topulse(Servo_pos2[0]));
    }
  }
}

void keypad_encode() {
  customKey = customKeypad.getKey();

  if (customKey) {
    switch (customKey) {
      case '1':
        data = "DETECT";
        break;
      case '2':
        data = "LESSONS";
        break;
      case '3':
        data = "NEXT";
        break;
      case '4':
        data = "BACK";
        break;
      case '5':
        data = "RIGHT";
        break;
      case '6':
        data = "LEFT";
        break;
      case '7':
        data = "E";
        break;
      case '8':
        data = "OFF";
        break;
    }
    Serial.println(data);
  }
}
