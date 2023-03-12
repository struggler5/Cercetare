#include<Servo.h>

Servo serv;

int loc=0; //location of the tip of sevo
int led =8;
int buz = 9;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
    pinMode(led,OUTPUT); //led pin
    pinMode(buz,OUTPUT); //buz pin
    serv.attach(10);
}


void loop() {
  
  // put your main code here, to run repeated
  if(Serial.read() == '1'){
    digitalWrite(led,1);  
    digitalWrite(buz,0);  
  }
  else if(Serial.read() == '2'){
    digitalWrite(led,0);  
    digitalWrite(buz,1); 
  }
  else if(Serial.read() == '3'){
    digitalWrite(led,0);  
    digitalWrite(buz,0); 
    serv.write(180);
  }
  else if(Serial.read() == '4'){
    digitalWrite(led,0);  
    digitalWrite(buz,0); 
    serv.write(0);
  }
 

  
  
}
