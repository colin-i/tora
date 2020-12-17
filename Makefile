all: init install

init:
	pip3 install -r requirements.txt

install:
	pip3 install --user .

uninstall:
	pip3 uninstall tora