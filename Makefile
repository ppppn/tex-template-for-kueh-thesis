#Makefile
A=Attachments
F=master_thesis
O=output
TMPDIR=temp
$O.pdf:${TMPDIR}/$F.dvi
	@dvipdfmx -o $O.pdf ${TMPDIR}/$F.dvi
${TMPDIR}/$F.dvi:${TMPDIR}/$F.tex
	@platex -kanji=utf8 -output-directory=${TMPDIR} ${TMPDIR}/$F.tex 
	@platex -kanji=utf8 -output-directory=${TMPDIR} ${TMPDIR}/$F.tex 
${TMPDIR}/$F.tex:$F.tex ${TMPDIR} $A/*.tex
	@./prepare_tex.py $F.tex ${TMPDIR}/$F.tex
pdf:$O.pdf
	@nohup evince $O.pdf > /dev/null 2>&1 &
clean:
	@rm -r $O.pdf ${TMPDIR} __pycache__
count:$F.tex
	@./counter.py $F.tex
${TMPDIR}:
	@mkdir ${TMPDIR}
	@ln -s ../Attachments ${TMPDIR}/
