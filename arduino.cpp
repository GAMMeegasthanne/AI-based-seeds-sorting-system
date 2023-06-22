const int ledPin = 13;  // Pin connected to the LED

void setup() {
  pinMode(ledPin, OUTPUT);  // Set the LED pin as output
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available()) {  // Check if data is available to read
    char command = Serial.read();  // Read the incoming command
    if (command == '0') {
      digitalWrite(ledPin, LOW);  // Turn off the LED
    } else if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
    }
  }
}
