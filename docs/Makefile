# Minimal Sphinx Makefile

SPHINXBUILD   = sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = docs/build
APIDOCSRC     = ../src/dsa
APIDOCOUT     = docs/source

.PHONY: help clean apidoc html

help:
	@echo "make clean     – remove all generated files"
	@echo "make apidoc    – regenerate .rst API docs"
	@echo "make html      – build HTML docs"

clean:
	rm -rf $(BUILDDIR)/*
	rm -f $(SOURCEDIR)/*.rst~
	rm -f $(SOURCEDIR)/*~ 
	# remove apidoc-generated module rst files
	rm -f $(SOURCEDIR)/dsa.*.rst
	rm -f $(SOURCEDIR)/modules.rst

apidoc:
	sphinx-apidoc -f -o $(APIDOCOUT) $(APIDOCSRC)

html: clean apidoc
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)
	@echo "Build finished. HTML in $(BUILDDIR)/html"
