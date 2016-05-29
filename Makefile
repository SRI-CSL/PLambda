ANTLR4=java -Xmx500M -cp "/usr/local/lib/antlr-4.5-complete.jar" org.antlr.v4.Tool


all:
	@echo 'To regenerate the antlr4 python code, do "make antlr4"'


antlr4:
	make -C src/antlr4 antlr4


check:
	python -m tests.primitive_data


clean:
	make -C src/antlr4 clean
	rm -f src/*.pyc src/*/*.pyc src/*/*~




