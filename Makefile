ANTLR4=java -Xmx500M -cp "/usr/local/lib/antlr-4.5-complete.jar" org.antlr.v4.Tool


all:
	@echo 'To regenerate the antlr4 python code, do "make antlr4"'


antlr4:
	make -C plam/antlr4 antlr4


check:
	python -m tests.primitive_data
	python -m tests.drones


clean:
	make -C plam/antlr4 clean
	rm -f plam/*.pyc plam/*/*.pyc plam/*/*~




