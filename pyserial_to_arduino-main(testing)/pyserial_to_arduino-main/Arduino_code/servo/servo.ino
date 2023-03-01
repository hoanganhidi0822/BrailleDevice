#include <Servo.h>

Servo myservo;
int Servopin = 11;
int val;

int Spos[8] = { 0, 138, 50, 40, 50, 65, 70, 80 };

int demR = 0, demL = 0;

void setup() {
  Serial.begin(115200);
  myservo.attach(Servopin);
  myservo.write(0);
}

void loop() {
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
        myservo.write(Spos[1]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[1]);
      } else if (text[i] == '1' && text[i + 1] == '2' && text[i + 2] != '3') {

        myservo.write(Spos[2]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[2]);
      } else if (text[i] == '1' && text[i + 1] == '2' && text[i + 2] == '3') {
        myservo.write(Spos[3]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[3]);
      } else if (text[i] == '2' && text[i + 1] == '3') {
        myservo.write(Spos[4]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[4]);
      } else if (text[i] == '3') {
        myservo.write(Spos[7]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[7]);
      } else if (text[i] == '1' && text[i + 1] == '3') {
        myservo.write(Spos[5]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[5]);
      } else if (text[i] == '2' && text[i + 1] != '3') {
        myservo.write(Spos[6]);
        Serial.print("Goc servo1: ");
        Serial.print(Spos[6]);
      } else {
        myservo.write(Spos[0]);
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
        Serial.print("__Goc servo2: ");
        Serial.print(Spos[1]);
      } else if (text[i] == '5') {
        Serial.print("__Goc servo2: ");
        Serial.print(Spos[6]);
      } else if (text[i] == '6') {
        Serial.print("__Goc servo2: ");
        Serial.print(Spos[7]);
      }
    } else if (demR == 2) {
      if (text[i] == '4' && text[i + 1] == '5') {
        Serial.print("__Goc servo2: ");
        Serial.print(Spos[2]);

      } else if (text[i] == '5' && text[i + 1] == '6') {
        Serial.print("__Goc servo2: ");
        Serial.print(Spos[4]);
      } else if (text[i] == '4' && text[i + 1] == '6') {
        //Serial.write("  Goc servo2: ");
        //Serial.write(Spos[5]);
        Serial.print("__Goc servo2: ");
        Serial.print(Spos[5]);
      }
    } else if (text[i] == '4' && text[i + 1] == '5' && text[i + 2] == '6') {
      Serial.print("__Goc servo2: ");
      Serial.print(Spos[3]);
    } else {
      Serial.print("__Goc servo2: ");
      Serial.print(Spos[0]);
    }
  }
}