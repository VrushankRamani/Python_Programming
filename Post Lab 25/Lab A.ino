void setup() {
  Serial.begin(9600);   
}

void loop() {
  if (Serial.available()) {
    
    String msg = Serial.readStringUntil('\n');
    
    // Print back to PC
    Serial.print("Arduino received: ");
    Serial.println(msg);
  }
}