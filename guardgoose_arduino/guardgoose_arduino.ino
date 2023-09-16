#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>

// PINS
#define RED_EYE_1 23
#define RED_EYE_2 19
#define HONK_BUZZER 33


// default I2C pins on ESP32: GPIO 22 (SCL) and GPIO 21 (SDA) -> for TOF
// additional I2C pins
#define SDA_BNO //INSERT
#define SCL_BNO //INSERT

// address of ToF sensor: 0x52
// address of BNO sensor: 0x28

Adafruit_BNO055 bno;
void setup() {
  
  pinMode(RED_EYE_1, OUTPUT); 
  pinMode (RED_EYE_2, OUTPUT);
  pinMode (HONK_BUZZER, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("hello");
  Wire.begin();
  if (!bno.begin()){
    Serial.println("BNO IS LOOSE");
    while(1){};
  }

//calibrate bno
//  uint8_t system, gyro, accel, mag = 0;
//  bno.getCalibration(&system, &gyro, &accel, &mag);
}
float prev_xaccel, prev_yaccel, prev_zaccel =0;
float acceleration_threshold = 0.9; //CHANGE THIS
void loop() {
  // put your main code here, to run repeatedly:
  imu::Vector<3> accel_value = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  
  Serial.print("accel values:");
  Serial.print(accel_value.x());
  Serial.print(", ");
  Serial.print(accel_value.y());
  Serial.print(", ");
  Serial.println(accel_value.z());
  if (accel_value.x()>=prev_xaccel){
  digitalWrite(HONK_BUZZER,HIGH);
  delay(1000);
  digitalWrite(HONK_BUZZER, LOW);
  }
  prev_xaccel = accel_value.x();
  prev_yaccel = accel_value.y();
  prev_zaccel = accel_value.z();
  delay(1000);
// if the laptop screen is physically tilted (movement is detected), then red eyes and honking
}
