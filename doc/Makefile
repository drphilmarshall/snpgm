
all: details.pdf

clean:
	-rm -f *.aux *.log *.dvi *.blg *.out *.bbl details.pdf

# ----------------------------------------------------------------------------

details.pdf: details.tex commanddefs.tex
	pdflatex details.tex
	pdflatex details.tex
# 	bibtex details
# 	pdflatex details.tex
# 	pdflatex details.tex

# ----------------------------------------------------------------------------
