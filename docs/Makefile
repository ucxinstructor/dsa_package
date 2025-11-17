# Makefile for Sphinx documentation

SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = source
BUILDDIR    = build

.PHONY: help apidoc html

# Default target: show help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Generate API docs from source
apidoc:
	@sphinx-apidoc -e -o "$(SOURCEDIR)" ../src/dsa

# Build HTML docs (depends on apidoc)
html: apidoc
	@$(SPHINXBUILD) -b html $(SPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)/html"
	@echo "Build finished. HTML pages are in $(BUILDDIR)/html."

# Catch-all: forward unknown targets to Sphinx
%:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)