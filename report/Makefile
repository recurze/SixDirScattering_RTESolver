all: report.pdf

report.pdf: report.tex
	pdflatex report.tex 2>/dev/null; pdflatex report.tex

.PHONY: clean

clean:
	rm report.{aux,log,out,toc,pdf}
