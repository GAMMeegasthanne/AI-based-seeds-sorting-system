#include <Servo.h>

Servo servo;
int servoPin = 9;

void setup()
{
  servo.attach(servoPin);

  Serial.begin(9600);
}

void loop()
{
  servo.write(0);
  delay(1000);
  servo.write(80);
  delay(1000);
}
