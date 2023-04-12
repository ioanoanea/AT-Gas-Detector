const int lpin = 13;
const int spin = A2;
const int limit = 200;
int sval = 0; // sensor read value - default 0

void setup() {
  Serial.begin(9600);
  pinMode(lpin, OUTPUT); // output pin connected to led
  pinMode(spin, INPUT); // input pin connected to sensor
}

void loop() {
  sval = analogRead(spin);
  if (sval >= limit) {
    digitalWrite(lpin, HIGH);
  } else {
    digitalWrite(lpin, LOW);
  }
  Serial.println(sval);
}
