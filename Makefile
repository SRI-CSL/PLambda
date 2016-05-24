ANTLR4=java -Xmx500M -cp "/usr/local/lib/antlr-4.5-complete.jar" org.antlr.v4.Tool


all:
	@echo 'To regenerate the antlr4 python code, do "make antlr4"'


antlr4:
	${ANTLR4} -Dlanguage=Python2 PLambda.g4 -visitor -o code



clean:
	rm -f code/*.pyc




