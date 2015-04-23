%.pdf: %.tex


MD:=$(wildcard *.md)
PDF:=$(MD:%.md=%.pdf)
TEX:=$(MD:%.md=%.tex)

TEXPARAMS = --latex-engine=lualatex -t latex
all: $(PDF)
$(PDF): %.pdf: %.md fixunicode.tex
	pandoc $(TEXPARAMS) $*.md -o $*.pdf

$(TEX): %.tex: %.md fixunicode.tex
	pandoc --standalone $(TEXPARAMS) $*.md -o $*.tex

clean:
	rm $(PDF)

