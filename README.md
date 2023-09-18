# Guard 🪿 Goose
When you think GoOsE you think PROTECTIVE, SCARY, AND LOUD. What better than having your own personal Guard Goose?
Guard Goose watches over your study space for you, while you take a much-deserved lil’ break, with 3 key features:

1) Easy to control app to turn on and off the Guard Goose.
2) Suspicious Surroundings Detection: If someone goes up close to your computer, the Guard Goose will activate its red laser eyes warning the thief to stay away 💥 You will also get a notification on the app.
3) Motion Detection: If someone goes so far to move your laptop, not only will Guard Goose activate its laser lights, it will also start honking, letting everyone around know that we have a thief on our hands. You will AGAIN get a notification on the app.

It effortlessly attaches to the back of your upright laptop as a cute, unassuming little study buddy (until, of course, it’s not).

Guard Goose offers you peace of mind by autonomously ensuring the security of their personal belongings during study sessions,
particularly in situations when no one else can watch it for you or you feel too anxious to ask others.

We used a time of flight sensor to detect when someone (aka the intruder) stays suspiciously close to your laptop and belongings. 
A 9 DOF absolute orientation sensor was used to detect when your laptop is moved. For both sensors, analog data was read from an
ESP32 microcontroller using Arduino. We wrote functions in C++ to clean and analyze sensor data from both sensors, and used serial 
communication to pass information from the Arduino to the Python-based app. 3D goose parts were created using CAD software, and then 3D printed. 
They formed the perfect enclosure for our hardware components, and were glued around the circuitry to form the goose body and head. We built 
the frontend of our user interactive application using HTML and CSS, while the backend was built in python on Taipy.
