.PHONY: run

IMGDIR := images
ALL_IMAGES := $(wildcard $(IMGDIR)/*) $(wildcard $(IMGDIR)/*/*)
ALL_FILES := main.py modules/ui_main.py modules/ui_cut_main.py modules/resources_rc.py $(ALL_IMAGES) $(VENV_TAG)
VENV_TAG := venv/install_tag
run: $(ALL_FILES)
	./venv/bin/python main.py

$(VENV_TAG): venv requirements.txt
	venv/bin/pip install -r requirements.txt
	touch $(VENV_TAG) 
venv:
	/usr/bin/python3 -m venv venv



modules/ui_main.py: $(VENV_TAG) main.ui
	./venv/bin/pyside6-uic main.ui --star-imports --from-imports > modules/ui_main.py

modules/ui_cut_main.py: $(VENV_TAG) cut_main.ui
	./venv/bin/pyside6-uic cut_main.ui --star-imports --from-imports > modules/ui_cut_main.py

modules/resources_rc.py: $(VENV_TAG) resources.qrc $(ALL_IMAGES)
	./venv/bin/pyside6-rcc resources.qrc -o modules/resources_rc.py
