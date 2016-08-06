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
	@echo '   make status                         view file status in git            '
	@echo '   make diff                           view file differences in git       '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make publish                        generate using production settings '
	@echo '   make clean                          remove the generated files         '
	@echo '   make commit (or github)             upload the web site via gh-pages   '
	@echo '   make checkout_output                get output folder from github      '
	@echo '   make pull                           get latest changes from git        '
	@echo '   make serve (or live)                show command for live              '
	@echo '   make post (or new_post)             show command for post              '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

status: publish
	cd $(OUTPUTDIR) && $(GIT) status
	$(GIT) status

diff: publish
	cd $(OUTPUTDIR) && $(GIT) diff
	$(GIT) diff

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	@echo 'Run checkout_output to get the output directory back'

commit: github

github: publish
	@echo "Publishing to github w/datetime: $(NOW)"
	-cd $(OUTPUTDIR) && $(GIT_ADD) && $(GIT_COMMIT) && $(GIT_PUSH)
	-$(GIT_ADD) && $(GIT_COMMIT) && $(GIT_PUSH)

checkout_output: clean
	$(GIT) clone git@github.com:olinbg/olinbg.github.com.git $(OUTPUTDIR)

pull: 
	cd $(OUTPUTDIR) && $(GIT_PULL)
	$(GIT_PULL)

serve: live

live:
	@echo "py3 olinbg.py live"

post: new_post

new_post:
	@echo "py3 olinbg.py post {title} {slug} {category}"

.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github

# stopserver:
# 	$(BASEDIR)/develop_server.sh stop
# 	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

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

# ssh_upload: publish
# 	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

# dropbox_upload: publish
# 	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)