void setup() 
{
  Serial.begin(9600);

  Serial.println("client<|M|>Connect<|EOM|>");

  pinMode(13, OUTPUT);
}
void loop() 
{
    if (Serial.available() > 0) 
    {
      String recived = Serial.read();

      if (recived.indexOf("<|EOM|>") != -1)
      {
        Serial.println("client<|M|><|ACK|>");
        on_message_recived(recived);
      }
    }

    delay(1000);
    send_message("Hello PC!");
}

void send_message(String message)
{
  Serial.println("client<|M|>" + message + "<|EOM|>");
}
void on_message_recived(String message)
{
  Serial.println("Recived");
}