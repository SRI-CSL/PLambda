ANTLR4=java -Xmx500M -cp "/usr/local/lib/antlr-4.5-complete.jar" org.antlr.v4.Tool


all:
	@echo ''
	@echo 'Here are the targets:'
	@echo ''
	@echo 'To regenerate the antlr4 python code :  "make antlr4"'
	@echo 'To develop                           :  "make develop"'
	@echo 'To test                              :  "make check"'
	@echo 'To test install                      :  "make testinstall"'
	@echo 'To install                           :  "make install"'
	@echo 'To test publish                      :  "make testpublish"'
	@echo 'To publish                           :  "make publish"'
	@echo ''
	@echo 'To turn README.rst 2 html            :  "make zippity"'
	@echo ''
	@echo 'then upload the zip file to https://pypi.python.org/pypi'
	@echo ''
	@echo 'To pylint                            :  "make lint"'
	@echo ''


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

zippity:
	rm -rf doczip*; mkdir doczip;
	cat README.md | pandoc -f rst > doczip/index.html
	zip -r -j doczip.zip doczip

clean:
	make -C plambda/antlr4 clean
	rm -f tests/*.pyc plambda/*.pyc plambda/*/*.pyc plambda/*/*~


PYLINT = $(shell which pylint)

lint:
ifeq ($(PYLINT),)
	$(error lint target requires pylint)
endif
# for detecting more than just errors:
	@ $(PYLINT) --rcfile=.pylintrc plambda/*.py plambda/actors/*.py plambda/eval/*.py plambda/util/*.py plambda/visitor/*.py
#	@ $(PYLINT) -E plambda/*.py plambda/*/*.py
