#include <DFRobotDFPlayerMini.h>
#include <SoftwareSerial.h>

int x; 
const byte rxPinDfplayer = 2;
const byte txPinDfplayer = 3;
const byte txPinLora = 10;
const byte rxPinLora = 11;
const int pinLed = 21;

SoftwareSerial lora(txPinLora, rxPinLora);
SoftwareSerial dfplayer(rxPinDfplayer, txPinDfplayer);
DFRobotDFPlayerMini myDFPlayer;

void setup() { 

	Serial.begin(9600); 
  dfplayer.begin(9600);
  lora.begin(9600);

	Serial.setTimeout(1); 
  myDFPlayer.begin(dfplayer);
  myDFPlayer.volume(60);
  myDFPlayer.play(1);
  myDFPlayer.read();
  
  pinMode(rxPinDfplayer, INPUT);
  pinMode(txPinDfplayer, OUTPUT);
  pinMode(pinLed, OUTPUT);
  digitalWrite(pinLed, LOW);

  delay(1000);
} 

void loop() { 
  while (!Serial.available()); 
  x = Serial.readString().toInt();
    if(x == 1){
      myDFPlayer.play(1);
      myDFPlayer.read();
      digitalWrite(pinLed, HIGH);
      delay(3000);
      digitalWrite(pinLed, LOW);
      lora.println("Data Dari Kamera"); 
      delay(1000);
    }if(x == 2){
      myDFPlayer.play(1);
      myDFPlayer.read();
      digitalWrite(pinLed, HIGH);
      delay(3000);
      digitalWrite(pinLed, LOW);
      lora.println("Data Dari Kamera"); 
      delay(1000);
    }else {
      digitalWrite(pinLed, LOW);
    }
} 
