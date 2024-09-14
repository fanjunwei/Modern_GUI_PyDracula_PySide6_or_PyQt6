.PHONY: run

IMGDIR := images
ALL_IMAGES := $(wildcard $(IMGDIR)/*) $(wildcard $(IMGDIR)/*/*)
ALL_FILES := main.py modules/ui_main.py modules/ui_cut_main.py modules/resources_rc.py $(ALL_IMAGES)

run: $(ALL_FILES)
	python main.py

modules/ui_main.py: main.ui
	pyside6-uic main.ui --star-imports --from-imports > modules/ui_main.py

modules/ui_cut_main.py: cut_main.ui
	pyside6-uic cut_main.ui --star-imports --from-imports > modules/ui_cut_main.py

modules/resources_rc.py: resources.qrc $(ALL_IMAGES)
	pyside6-rcc resources.qrc -o modules/resources_rc.py
