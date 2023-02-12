#include <Keypad.h>
#include <Servo.h>

const byte ROWS = 4;  //four rows
const byte COLS = 2;  //four columns
const byte led = 2;
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
  { '1', '5' },
  { '2', '6' },
  { '3', '7' },
  { '4', '8' }
};
byte rowPins[ROWS] = { 6, 5, 4, 3 };  //connect to the row pinouts of the keypad
byte colPins[COLS] = { 7, 8 };        //connect to the column pinouts of the keypad

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

String data = "hello";
char customKey;
/////////////////////////////////////////////////////////////////////////////////////////////////

Servo servo1;
Servo servo2;


int val;

int Spos[8] = { 145, 120, 95, 87, 73, 55, 40, 25 };
int Spos1[8] = { 118, 0, 60, 68, 79, 42, 24, 98 };
//int Spos[8] = { 0, 40, 70, 79, 90, 115, 130, 145 };

int demR = 0, demL = 0;

void setup() {
  Serial.begin(115200);
  
  servo1.attach(10);
  servo1.write(0);
  
  servo2.attach(11);
  servo2.write(0);
}


void loop() {
  controlServo();
  keypad_encode();
}

void controlServo() {
  int demR = 0, demL = 0;


  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');
    // String data = "1";
    char text[data.length()];

    for (int i = 0; i < data.length(); i++) {
      text[i] = data[i];
    }

    int i = 0;
    //123
    if (((int)text[i] - 48) < 4) {
      if (text[i] == '1' && text[i + 1] != '2' && text[i + 1] != '3') {
        servo1.write(Spos[1]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[1]);
      } else if (text[i] == '1' && text[i + 1] == '2' && text[i + 2] != '3') {

        servo1.write(Spos[2]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[2]);
      } else if (text[i] == '1' && text[i + 1] == '2' && text[i + 2] == '3') {
        servo1.write(Spos[3]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[3]);
      } else if (text[i] == '2' && text[i + 1] == '3') {
        servo1.write(Spos[4]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[4]);
      } else if (text[i] == '3') {
        servo1.write(Spos[7]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[7]);
      } else if (text[i] == '1' && text[i + 1] == '3') {
        servo1.write(Spos[5]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[5]);
      } else if (text[i] == '2' && text[i + 1] != '3') {
        servo1.write(Spos[6]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[6]);
      } else {
        servo1.write(Spos[0]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[0]);
      }
    }

    //456

    for (int i = 0; i < data.length(); i++) {
      if (((int)text[i] - 48) > 3) {
        demR += 1;
      }
      if (((int)text[i] - 48) < 4) {
        demL += 1;
      }
    }

    i = demL;

    //Serial.print("________Dem: ");
    //Serial.print(demR);

    if (demR == 1) {
      if (text[i] == '4') {
        servo2.write(Spos1[1]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos1[1]);
      } else if (text[i] == '5') {
        servo2.write(Spos1[1]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos1[6]);
      } else if (text[i] == '6') {
        servo2.write(Spos1[1]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos1[7]);
      }
    } else if (demR == 2) {
      if (text[i] == '4' && text[i + 1] == '5') {
        servo2.write(Spos1[1]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos1[2]);

      } else if (text[i] == '5' && text[i + 1] == '6') {
        servo2.write(Spos1[1]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos1[4]);
      } else if (text[i] == '4' && text[i + 1] == '6') {
        //Serial.write("  Goc servo2: ");
        //Serial.write(Spos[5]);
        servo2.write(Spos1[1]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos1[5]);
      }
    } else if (text[i] == '4' && text[i + 1] == '5' && text[i + 2] == '6') {
      servo2.write(Spos1[1]);
      Serial.print("__Goc servo2: ");
      Serial.print(Spos1[3]);
    } else {
      servo2.write(Spos1[1]);
      Serial.print("__Goc servo2: ");
      Serial.print(Spos1[0]);
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
        data = "EXPLAIN";
        break;
      case '8':
        data = "OFF";
        break;
    }
    Serial.println(data);
  }
}