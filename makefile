# $ make file=myFileName
compileRunClean: compile run clean

compile:
	g++ -std=c++17 -o $(file) $(file).cpp

run:
	./$(file)

clean:
	rm $(file)

clean-java:
	rm *.class