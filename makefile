# $ make file=myFileName
compileRunClean: compile run clean

compile:
	g++ -o $(file) $(file).cpp

run:
	./$(file)

clean:
	rm $(file)