cd src/java

actual=$(basename $1)

javac $actual
jar cfe ../../a.jar $(echo "$actual" | cut -d. -f1) ${actual%.java}.class

cd ../../