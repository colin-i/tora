
pint='pip'
ifneq (, $(shell which pip3 ))
	pint='pip3'
endif

all: init install

init:
	${pint} install -r requirements.txt

install:
	${pint} install --user .

uninstall:
	${pint} uninstall tora