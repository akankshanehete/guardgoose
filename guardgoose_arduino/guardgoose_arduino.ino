#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <VL53L1X.h>


// PINS
#define RED_EYE_1 23
#define RED_EYE_2 19
#define HONK_BUZZER 14


// default I2C pins on ESP32: GPIO 22 (SCL) and GPIO 21 (SDA) -> for TOF
// additional I2C pins
#define SDA_BNO //INSERT
#define SCL_BNO //INSERT

// address of ToF sensor: 0x52
// address of BNO sensor: 0x28

Adafruit_BNO055 bno;
VL53L1X tof;

void setup() {
  
  pinMode(RED_EYE_1, OUTPUT); 
  pinMode (RED_EYE_2, OUTPUT);
  pinMode (HONK_BUZZER, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("hello");
  Wire.begin();

  /* set up bno sensor */
  if (!bno.begin()) {
    Serial.println("BNO IS LOOSE");
    while(1){};
  }
  //calibrate bno
  //  uint8_t system, gyro, accel, mag = 0;
  //  bno.getCalibration(&system, &gyro, &accel, &mag);

  /* set up time of flight sensor */
  tof.setTimeout(500);
  if (!tof.init()) {
    Serial.println("TOF IS LOOSE");
    while(1);
  }
  // short distance mode
  tof.setDistanceMode(VL53L1X::Short);
  tof.setMeasurementTimingBudget(20000);
  tof.startContinuous(50);
  // Serial.println("TOF GOOD");
}

float prev_xaccel, prev_yaccel, prev_zaccel =0;
float acceleration_threshold = 10; //CHANGE THIS
int prev_dist1, prev_dist2 = 500;

int dist_threshold = 200;
int avg_dist = 500;

bool device_on = false;
int appData = -1;

void loop() {  
  if (Serial.available() > 0) {
    appData = Serial.read();
    // Serial.println(appData);
  }
  if (appData == 1) {
    device_on = true;
    // Serial.println("DEVICE ON");
  } else if (appData == 0) {
    device_on = false;
    // Serial.println("DEVICE OFF");
  }

 if (device_on) {
    run_device();    
  } else {
    redEyesOn(false);
  }

}

void run_device() {
  /* Laptop has been moved */
  // if the laptop screen is physically tilted (movement is detected), then red eyes and honking
  imu::Vector<3> accel_value = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  int acc_mag = sqrt(sq(accel_value.x()) + sq(accel_value.y()) + sq(accel_value.z()));
  
  /* Serial.print("accel values: ");
  Serial.print(accel_value.x());
  Serial.print(", ");
  Serial.print(accel_value.y());
  Serial.print(", ");
  Serial.println(accel_value.z());

  /*prev_xaccel = accel_value.x();
  prev_yaccel = accel_value.y();
  prev_zaccel = accel_value.z();*/

  /* Someone is approaching the laptop */
  int distance = tof.read();
  // Serial.println(distance);
  if (tof.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
  /* Serial.print("distance (mm): ");
  Serial.println(distance); */

  avg_dist = (prev_dist1 + prev_dist2 + distance) / 3;
  prev_dist2 = prev_dist1;
  prev_dist1 = distance;

  /* check values and send alert if necessary */
  if (acc_mag>=acceleration_threshold){
    theftAlert();
  } else if (avg_dist < dist_threshold) {
    suspiciousAlert();
  } else {
    redEyesOn(false);
  }
  delay(1000);

}

void suspiciousAlert() {
  Serial.print(2);
  redEyesOn(true);
}

void theftAlert() {
  Serial.print(3);
  digitalWrite(HONK_BUZZER,HIGH);
  delay(1000);
  digitalWrite(HONK_BUZZER, LOW);
  redEyesOn(true);
}

void redEyesOn(bool on) {
  if (on) {
    digitalWrite(RED_EYE_1,HIGH);
    digitalWrite(RED_EYE_2,HIGH);
  }
  else {
    digitalWrite(RED_EYE_1,LOW);
    digitalWrite(RED_EYE_2,LOW);
  }
}
