unsigned long highCounter = 0;
int pulse = 0;
int val = 0;
int lastPulse = LOW;
unsigned long oldMillis = 0;
  
void setup() {
 pinMode(2, INPUT);
 Serial.begin(9600);
 }
  
void loop() {
pulse = digitalRead(2);
if (pulse != lastPulse) {
  lastPulse = pulse;
  if (pulse == HIGH) highCounter++;
} 
  
// print and reset highCounter every seconds
if ( millis() - oldMillis >= 10000 )
{
  oldMillis = millis();
  val = highCounter * 6;
  if (highCounter > 1) 
  Serial.println(val);
  highCounter = 0;
}
}