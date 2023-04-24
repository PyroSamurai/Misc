#!/bin/bash
rm -f BMP24to16.jar
cd ..
jar cf BMP24to16/src/BMP24to16.jar BMP24to16/src/*.java BMP24to16/LICENSE
cd BMP24to16/src
javac *.java
jar ufe BMP24to16.jar Main *.class
cd ..
rm src/*.class
mv src/BMP24to16.jar BMP24to16.jar
chmod 707 BMP24to16.jar
