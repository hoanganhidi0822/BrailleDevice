#include <Keypad.h>

const byte ROWS = 4;  //four rows
const byte COLS = 2;  //four columns
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
  { '5', '1' },
  { '6', '2' },
  { '7', '3' },
  { '8', '4' },
};
byte rowPins[ROWS] = { 6, 7, 8, 9 };  //connect to the row pinouts of the keypad
byte colPins[COLS] = { 5, 2 };        //connect to the column pinouts of the keypad

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

String data = "hello";
char customKey;

void setup() {
  Serial.begin(115200);
}

void loop() {
  //keypad_encode();
  test();
}

void test() {
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
    Serial.println(customKey);
  }
}
