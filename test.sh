ant clean 
ant 
java -jar ./result/decaf.jar -l 2 test.decaf > test.tac
java -jar ./TestCases/S3/tac.jar test.tac
