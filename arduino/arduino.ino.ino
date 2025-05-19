// Arduino Sketch to Acquire EMG Data from 8 Channels

const int numChannels = 8;
int emgPins[numChannels] = {A0, A1, A2, A3, A4, A5, A6, A7}; // Analog pins for 8 EMG sensors

void setup() {
  Serial.begin(9600); // Start serial communication
  for (int i = 0; i < numChannels; i++) {
    pinMode(emgPins[i], INPUT);
  }
}

void loop() {
  unsigned long timestamp = millis(); // Timestamp in milliseconds
  Serial.print(timestamp);
  
  // Read all 8 channels and print values separated by commas
  for (int i = 0; i < numChannels; i++) {
    int value = analogRead(emgPins[i]);
    Serial.print(",");
    Serial.print(value);
  }
  
  Serial.println(); // Newline after each complete reading
  delay(50); // Sampling delay (adjust based on sensor/sample rate)
}
