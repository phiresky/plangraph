%.pdf: %.tex


MD:=$(wildcard *.md)
VORL:=$(wildcard Vorlesung*.md)
PDF:=$(MD:%.md=%.pdf)
TEX:=$(MD:%.md=%.tex)

TEXPARAMS = --toc --latex-engine=lualatex -t latex -V classoption=draft
all: MitschriebPlanGraph2015SS.pdf #$(PDF)

%.pdf: %.md fixunicode.tex
	pandoc $(TEXPARAMS) header.md $*.md -o $*.pdf

MitschriebPlanGraph2015SS.pdf: $(MD)
	pandoc $(TEXPARAMS) header.md MitschriebPlanGraph2015SS.md $(VORL) -o MitschriebPlanGraph2015SS.pdf

$(TEX): %.tex: %.md fixunicode.tex
	pandoc --standalone $(TEXPARAMS) $*.md -o $*.tex

clean:
	rm $(PDF)

