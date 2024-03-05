  
//Importamos librerias necesarias para OLED
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHTesp.h"

//Definimos las medidad en pixeles de ancho y alto de la pantalla
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

//Crear el objeto para manejar la pantalla 
Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

//Creamos variable del sensor  especificamos el pin
int sensorPin = 13;
//Declaramos sensor
DHTesp sensor;



void setup() {
  
//configurar el sensor 
  sensor.setup(sensorPin, DHTesp::DHT11);
  Serial.begin(115200);
  //Iniciamos la pantalla OLED
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  //limpiar pantalla
  oled.clearDisplay();
  //Tamaño de letra
  oled.setTextSize(2);
  //Color de la letra
  oled.setTextColor(WHITE);;
  //Colocamos en punto x,y especifico
  oled.setCursor(0,2);
  //Escribimos un texto
  oled.println("Hola GDS0552");
  //Mostrar en pantalla
  oled.display();
  delay(2000);


}

void loop() {
  //limpiar pantalla
  oled.clearDisplay();
  //Declaro variable de temperatura y humedad 
  TempAndHumidity data = sensor.getTempAndHumidity();
  //Tamaño de letra
  oled.setTextSize(1);
  //Color de la letra
  oled.setTextColor(WHITE);
  //Colocamos en punto x,y especifico
  oled.setCursor(0,2);
  //Escribimos un texto
  oled.println("TEMPERATURA: "+String(data.temperature,1)+" °C");
   oled.setCursor(0,12);
  //Escribimos un texto
  oled.println("HUMEDAD: "+String(data.humidity,1)+" %");
  //Mostrar en pantalla
  oled.display();
  delay(2000);

  oled.clearDisplay();

  if(data.temperature <= 50){
  oled.setCursor(0,2);
  oled.println("TEMPERATURA NORMAL");
  //Mostrar en pantalla
  oled.display();
  }
  else{
  oled.setCursor(0,2);
  oled.println("TEMPERATURA ALTA");
  //Mostrar en pantalla
  oled.display();
  }

  delay(2000); // this speeds up the simulation
  oled.clearDisplay();
}

