int a = 0;

void setup()
{
  Serial.begin(115200);
  analogReadResolution(12);
}

void loop()
{
  for(int i=0; i<5; i++){
    a=a+analogRead(34);
  }
  Serial.println(a/5);
  delayMicroseconds(200);
  a=0;
}
