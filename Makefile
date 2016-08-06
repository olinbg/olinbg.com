PY?=python3
PELICAN?=pelican
GIT?=git
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/../output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

NOW=`date +'%Y-%m-%d %H:%M:%S'`
GIT_ADD=$(GIT) add --all
GIT_COMMIT=$(GIT) commit -m "Site update: $(NOW)"
GIT_PUSH=$(GIT) push -u origin master
GIT_PULL=$(GIT) pull

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_PAGES_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make diff (or status)               view file differences in git       '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

status: diff
diff:
	cd $(OUTPUTDIR) && $(GIT) status
	$(GIT) status

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

commit: github

github: publish
	@echo "Publishing to github w/datetime: $(NOW)"
	-cd $(OUTPUTDIR) && $(GIT_ADD) && $(GIT_COMMIT) && $(GIT_PUSH)
	-$(GIT_ADD) && $(GIT_COMMIT) && $(GIT_PUSH)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	@echo 'Run checkout_output to get the output directory back'

checkout_output: clean
	$(GIT) clone git@github.com:olinbg/olinbg.github.com.git $(OUTPUTDIR)

pull: 
	cd $(OUTPUTDIR) && $(GIT_PULL)
	$(GIT_PULL)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve: live

live:
	@echo "Add livereload support from python"

post: new_post

new_post:
	@echo "Add new post support from python"

# serve:
# ifdef PORT
# 	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
# else
# 	cd $(OUTPUTDIR) && $(PY) -m pelican.server
# endif

# serve-global:
# ifdef SERVER
# 	cd $(OUTPUTDIR) && $(PY) -m pelican.server 80 $(SERVER)
# else
# 	cd $(OUTPUTDIR) && $(PY) -m pelican.server 80 0.0.0.0
# endif


# devserver:
# ifdef PORT
# 	$(BASEDIR)/develop_server.sh restart $(PORT)
# else
# 	$(BASEDIR)/develop_server.sh restart
# endif

stopserver:
	$(BASEDIR)/develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
