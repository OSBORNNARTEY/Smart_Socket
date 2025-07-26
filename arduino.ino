// Pins
const int analogInPin = A0;
const int relayPin = 7;
const int led1 = 2;
const int led2 = 3;
const int led3 = 4;
const int led4 = 5;
const int modeLED = 9;

// State variables
int sensorValue = 0;
bool manualMode = false;  // true = manual mode, false = automatic
unsigned long lastSensorReadTime = 0;
const unsigned long sensorInterval = 100; // non-blocking delay

void setup() {
  Serial.begin(9600);

  // Set pin modes
  pinMode(relayPin, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(modeLED, OUTPUT);

  // Initial state
  digitalWrite(relayPin, HIGH); // Relay OFF
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
}

void loop() {
  digitalWrite(modeLED, manualMode ? HIGH : LOW); // ON in manual mode
  // ====== Check for serial input first ======
  while (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == 'U') {
      manualMode = true;
      Serial.println("Switched to MANUAL mode.");
    } 
    else if (cmd == 'u') {
      manualMode = false;
      Serial.println("Switched to AUTOMATIC mode.");
    } 
    else if (manualMode) {
      if (cmd == 'A') {
        digitalWrite(relayPin, HIGH);
        Serial.println("Relay turned ON (manual).");
      } 
      else if (cmd == 'a') {
        digitalWrite(relayPin, LOW);
        Serial.println("Relay turned OFF (manual).");
      }
    }
  }

  // ====== AUTOMATIC MODE LOOP ======
  if (!manualMode) {
    unsigned long currentTime = millis();
    if (currentTime - lastSensorReadTime >= sensorInterval) {
      lastSensorReadTime = currentTime;

      sensorValue = analogRead(analogInPin);
      Serial.print("Water Sensor Reading: ");
      Serial.println(sensorValue);

      if (sensorValue >= 350) {
        digitalWrite(relayPin, LOW);
        digitalWrite(led1, HIGH);
        digitalWrite(led2, HIGH);
        digitalWrite(led3, HIGH);
        digitalWrite(led4, HIGH);
      } 
      else if (sensorValue >= 300 && sensorValue <= 349) {
        digitalWrite(relayPin, LOW);
        digitalWrite(led1, HIGH);
        digitalWrite(led2, HIGH);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);
      } 
      else if (sensorValue >= 20 && sensorValue <= 299) {
        digitalWrite(relayPin, HIGH);
        digitalWrite(led1, HIGH);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);
      } 
      else {
        digitalWrite(relayPin, HIGH);
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);
      }
    }
  }

  // In manual mode, nothing happens here unless a command is sent.
}
