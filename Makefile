VORL:=$(sort $(wildcard Vorlesung*.md))
TEXPARAMS = --number-sections --filter ./graphviz.py --toc --latex-engine=lualatex -t latex

ifeq ($(DEBUG), 1)
	TEXPARAMS+= -V classoption=draft
endif

all: MitschriebPlanGraph2015SS.pdf

MitschriebPlanGraph2015SS.pdf: header.md $(VORL) $(wildcard graphs/*.dot)
	pandoc $(TEXPARAMS) header.md $(VORL) -o MitschriebPlanGraph2015SS.pdf
