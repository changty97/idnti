PROJ_DIR=$(CURDIR)
VENV?=venv
PYTHON=$(CURDIR)/$(VENV_BIN)/python

ifeq ($(OS), Windows_NT)
	VENV_BIN=$(VENV)/Scripts
	SYSTEM_PYTHON?="$(shell py.exe -3 -c "import sys; print(sys.prefix.replace('\\\\\\\\','/'))")/python.exe"
	space:=$(subst ,, )
	PYTHON:=$(subst $(space),\\ ,$(PYTHON))
else
	VENV_BIN=$(VENV)/bin
	SYSTEM_PYTHON?=$(shell which python3)
endif

VIRTUAL_ENV=$(SYSTEM_PYTHON) -m venv
PIP=$(PYTHON) -m pip
PYLINT=$(VENV_BIN)/pylint

venv: requirements.txt
	test -d $(VENV) || $(VIRTUAL_ENV) $(VENV)
	. $(VENV_BIN)/activate
	test -n "$(NO_PIP_INSTALL)" || $(PIP) install -U pip
	test -n "$(NO_PIP_INSTALL)" || $(PIP) install -Ur requirements.txt

lint: venv
	$(PYLINT) --rcfile=.pylintrc -r n $(PROJ_DIR)

clean:
	rm -rf venv
