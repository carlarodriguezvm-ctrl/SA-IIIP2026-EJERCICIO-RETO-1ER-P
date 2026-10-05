// Pines de los LEDs
const int led1 = 13;
const int led2 = 12;
const int led3 = 11;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  
  //APAGADOS TODOS
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    
    switch (comando) {
      // LED 1
      case 'a':
        digitalWrite(led1, HIGH);
        Serial.println("LED 1 ROJO encendido");
        break;
      case 'A':
        digitalWrite(led1, LOW);
        Serial.println("LED 1 ROJO apagado");
        break;
        
      // LED 2
      case 'b':
        digitalWrite(led2, HIGH);
        Serial.println("LED 2 AMARILLO encendido");
        break;
      case 'B':
        digitalWrite(led2, LOW);
        Serial.println("LED 2 AMARILLO apagado");
        break;
        
      // LED 3
      case 'c':
        digitalWrite(led3, HIGH);
        Serial.println("LED 3 AZUL encendido");
        break;
      case 'C':
        digitalWrite(led3, LOW);
        Serial.println("LED 3 AZUL apagado");
        break;
        
      // Comandos no reconocidos (ignora saltos de línea \n y \r)
      default:
        if (comando != '\n' && comando != '\r') {
          Serial.println("Valor no reconocido");
        }
        break;
    }
  }
}