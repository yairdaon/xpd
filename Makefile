pdf: 
	pdflatex tex/xpd.tex
	mv xpd.* tex

clean:
	rm -rvf xpd.aux xpd.log xpd.pdf

push:
	git push https://github.com/yairdaon/xpd.git
	
