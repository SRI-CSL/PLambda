all:
	@echo ''
	@echo 'Here are the targets:'
	@echo ''
	@echo 'To regenerate the antlr4 (antlr4.8 python3) code :  "make antlr"'
	@echo 'To develop                                       :  "make develop"'
	@echo 'To test                                          :  "make check"'
	@echo 'To install                                       :  "make install"'
	@echo 'To publish                                       :  "make publish"'
	@echo ''
	@echo 'To turn README.rst 2 html                        :  "make zippity"'
	@echo ''
	@echo 'then upload the zip file to https://pypi.python.org/pypi'
	@echo ''
	@echo 'To pylint                                        :  "make lint"'
	@echo ''


antlr:
	make -C plambda/antlr4 antlr4_8


check:
	python -O -m tests.language

#local editable install for developing
develop:
	pip install -e .


dist: clean antlr4
	python setup.py bdist_wheel

# If you need to push your project again,
# change the version number in plambda/version.py,
# otherwise the server will give you an error.

# requires an appropriate .pypirc file
publish: dist
	python3 -m twine upload --repository pypi dist/*

install:
	pip install plambda

zippity:
	rm -rf doczip*; mkdir doczip;
	cat README.rst | pandoc -f rst > doczip/index.html
	zip -r -j doczip.zip doczip

clean:
	make -C plambda/antlr4 clean
	rm -f tests/*.pyc plambda/*.pyc plambda/*/*.pyc plambda/*/*~

spotless:
	rm -rf doczip doczip.zip build dist



PYLINT = $(shell which pylint)

lint:
ifeq ($(PYLINT),)
	$(error lint target requires pylint)
endif
# for detecting more than just errors:
	@ $(PYLINT) --rcfile=.pylintrc plambda/*.py plambda/actors/*.py plambda/eval/*.py plambda/util/*.py plambda/visitor/*.py tests/drones/*.py
#	@ $(PYLINT) -E plambda/*.py plambda/*/*.py
