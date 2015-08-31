%.pdf: %.tex


MD:=$(wildcard *.md)
VORL:=$(sort $(wildcard Vorlesung*.md))
PDF:=$(MD:%.md=%.pdf)
TEX:=$(MD:%.md=%.tex)
TEXPARAMS = --number-sections --filter ./graphviz.py --toc --latex-engine=lualatex -t latex

ifeq ($(DEBUG), 1)
	TEXPARAMS+= -V classoption=draft
endif

all: MitschriebPlanGraph2015SS.pdf #$(PDF)

%.pdf: %.md fixunicode.tex
	pandoc $(TEXPARAMS) header.md $*.md -o $*.pdf

MitschriebPlanGraph2015SS.pdf: $(MD) $(wildcard graphs/*.dot)
	pandoc $(TEXPARAMS) header.md $(VORL) -o MitschriebPlanGraph2015SS.pdf

$(TEX): %.tex: %.md fixunicode.tex
	pandoc --standalone $(TEXPARAMS) $*.md -o $*.tex

clean:
	rm -rf $(PDF)
	rm -rf *_dot.pdf

