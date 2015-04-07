pdf: 
	pdflatex tex/xpd.tex
	mv xpd.* tex

clean:
	rm -rvf xpd.aux xpd.log xpd.pdf