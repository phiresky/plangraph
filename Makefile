%.pdf: %.tex


MD:=$(wildcard *.md)
PDF:=$(MD:%.md=%.pdf)
TEX:=$(MD:%.md=%.tex)

TEXPARAMS = --include-before-body=fixunicode.tex --latex-engine=lualatex -t latex
all: $(PDF)
$(PDF): %.pdf: %.md
	pandoc $(TEXPARAMS) $*.md -o $*.pdf

$(TEX): %.tex: %.md
	pandoc --standalone $(TEXPARAMS) $*.md -o $*.tex

clean:
	rm $(PDF)

