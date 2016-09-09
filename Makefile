ANTLR4=java -Xmx500M -cp "/usr/local/lib/antlr-4.5-complete.jar" org.antlr.v4.Tool


all:
	@echo 'To regenerate the antlr4 python code, do "make antlr4"'


antlr4:
	make -C plambda/antlr4 antlr4


check:
	python -O -m tests.language

#local editable install for developing
develop: 
	pip install -e .


dist: clean antlr4
	python setup.py bdist_wheel

# If you need to push your project again,
# change the version number in plambda/eval/PLambda.py,
# otherwise the server will give you an error. 

testpublish: dist
	python setup.py register -r https://testpypi.python.org/pypi
	python setup.py sdist upload -r https://testpypi.python.org/pypi

testinstall:
	pip install -i https://testpypi.python.org/pypi plambda

publish: dist
	python setup.py register -r https://pypi.python.org/pypi
	python setup.py sdist upload -r https://pypi.python.org/pypi

install:
	pip install plambda

clean:
	make -C plambda/antlr4 clean
	rm -f tests/*.pyc plambda/*.pyc plambda/*/*.pyc plambda/*/*~


