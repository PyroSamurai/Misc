@ECHO OFF
DEL ujava.jar
jar cf src\ujava.jar src\*.java LICENSE GPLV3 VERSION "README.md"
CD src
javac -d . *.java
CD ..
MOVE src\ujava ujava
MOVE src\ujava.jar ujava.jar
jar uf ujava.jar ujava
DEL ujava\*.class
RMDIR ujava
