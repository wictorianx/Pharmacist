#include <SoftwareSerial.h>
SoftwareSerial miBT(10,11);
 
void setup() {
  Serial.begin(9600);
  miBT.begin(38400);
 
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
}
 
void loop(){
  if (miBT.available()>0) {
 
    byte input=miBT.read();
 
    if(input == 'B'){          //FORWARD ---- 
        digitalWrite(6, HIGH);
        digitalWrite(5, LOW);
        digitalWrite(4, LOW);
        digitalWrite(3, HIGH);
    }
  }
}