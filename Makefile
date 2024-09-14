.PHONY: run

IMGDIR := images
ALL_IMAGES := $(wildcard $(IMGDIR)/*) $(wildcard $(IMGDIR)/*/*)
ALL_FILES := main.py modules/ui_main.py modules/ui_cut_main.py modules/resources_rc.py $(ALL_IMAGES) $(VENV_TAG)
VENV_TAG := venv/install_tag
PYTHON := ./venv/bin/python
UIC := ./venv/bin/pyside6-uic
RCC := ./venv/bin/pyside6-rcc

run: $(ALL_FILES)
	$(PYTHON) main.py

$(VENV_TAG): venv requirements.txt
	venv/bin/pip install -r requirements.txt
	touch $(VENV_TAG)

venv:
	/usr/bin/python3 -m venv venv

modules/ui_main.py: $(VENV_TAG) main.ui
	$(UIC) main.ui --star-imports --from-imports > modules/ui_main.py

modules/ui_cut_main.py: $(VENV_TAG) cut_main.ui
	$(UIC) cut_main.ui --star-imports --from-imports > modules/ui_cut_main.py

modules/resources_rc.py: $(VENV_TAG) resources.qrc $(ALL_IMAGES)
	$(RCC) resources.qrc -o modules/resources_rc.py
