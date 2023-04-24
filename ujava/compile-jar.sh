#!/bin/bash
rm -f ujava.jar
jar cf src/ujava.jar src/*.java LICENSE GPLV3 VERSION README.md
cd src
javac -d . *.java
cd ..
mv src/ujava ./
mv src/ujava.jar ./
jar uf ./ujava.jar ./ujava
rm ujava/*.class
rmdir ujava
