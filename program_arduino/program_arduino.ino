#include <DFRobotDFPlayerMini.h>
#include <SoftwareSerial.h>

int x; 
const byte rxPinDfplayer  = 2;
const byte txPinDfplayer  = 3;
const byte txPinLora      = 10;
const byte rxPinLora      = 11;
const int pinLedKuning    = 4;
const int pinLedMerah     = 12;
const int pinLedBiru      = 8;
const int pinLedHijau     = 13;

SoftwareSerial lora(txPinLora, rxPinLora);
SoftwareSerial dfplayer(rxPinDfplayer, txPinDfplayer);
DFRobotDFPlayerMini myDFPlayer;

void setup() { 

	Serial.begin(9600); 
  dfplayer.begin(9600);
  lora.begin(9600);
	Serial.setTimeout(1); 
  myDFPlayer.begin(dfplayer);
  // myDFPlayer.volume(40);
  // myDFPlayer.play(2);
  // myDFPlayer.read();

  pinMode(rxPinDfplayer, INPUT);
  pinMode(txPinDfplayer, OUTPUT);
  pinMode(pinLedKuning, OUTPUT);
  pinMode(pinLedMerah, OUTPUT);
  pinMode(pinLedHijau, OUTPUT);
  pinMode(pinLedBiru, OUTPUT);

  digitalWrite(pinLedKuning, HIGH);
  digitalWrite(pinLedMerah, HIGH);
  digitalWrite(pinLedHijau, HIGH);
  digitalWrite(pinLedBiru, HIGH);
  delay(1000);
} 

void loop() { 
  digitalWrite(pinLedKuning, LOW);
  digitalWrite(pinLedHijau, HIGH);
  while (!Serial.available()); 
  x = Serial.readString().toInt();
    if(x == 1){
      myDFPlayer.play(2);
      myDFPlayer.read();
      digitalWrite(pinLedHijau, LOW);
      digitalWrite(pinLedKuning, HIGH);
      lora.println("Data Dari Kamera");
      delay(6000);
      digitalWrite(pinLedHijau, LOW);
      digitalWrite(pinLedKuning, LOW);
    }
} 
