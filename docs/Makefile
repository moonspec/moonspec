# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
ROOT_DIR	  := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = $(ROOT_DIR)/source
BUILDDIR      = $(ROOT_DIR)/build
HTMLDIR      = $(ROOT_DIR)/build/dirhtml
PUBDIR      = $(ROOT_DIR)/public
APIIN	      = $(realpath ../)
APIOUT        = $(ROOT_DIR)/source/apidoc/

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# Generate API docs
api:
	@rm -rf "${APIOUT}"; sphinx-apidoc -f -M -T -H "API documentation" -o "${APIOUT}" "${APIIN}" \
		"../moonspec/[!a][!p][!i]*" "../moonspec/main.py" "../setup*" "../example*" "../local*"
	@rm -f "${APIOUT}/moonspec.rst"

# Build stuff
documentation:
	rm -rf "${BUILDDIR}"
	rm -rf "${APIOUT}"
	@make api
	@make dirhtml
	@make man
	@make text
	rm -rf "${PUBDIR}"
	mkdir -p "${PUBDIR}"
	cp -r "${HTMLDIR}"/* "${PUBDIR}"
	echo 'moonspec.hub256.com' > "${PUBDIR}/CNAME"
	touch "${PUBDIR}/.nojekyll"


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
