from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer
import livereload
from datetime import datetime

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

POST_TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Category: {category}
Slug: {slug}
Status: draft

(Fill in)
"""

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican content -o output -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    # clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    # project.rsync_project(
    #     remote_dir=dest_path,
    #     exclude=".DS_Store",
    #     local_dir=DEPLOY_PATH.rstrip('/') + '/',
    #     delete=True,
    #     extra_opts='-c',
    # )

def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))

def post(title, slug, category):
    """Create a markdown post with title, slug, and category"""
    today = datetime.today()
    f_create = "content/articles/{}/{}_{:0>2}_{:0>2}_{}.md".format(
        category, today.year, today.month, today.day, slug)
    t = POST_TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                category=category,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("Post created -> " + f_create)

def github():
    """First publish, then update both repos with the latest changes"""
    publish()
    now = datetime.today()
    print("Publishing to github w/datetime: {}".format(now))
    local("git --git-dir=output/.git --work-tree=output add --all")
    with settings(warn_only=True):
        local("git --git-dir=output/.git --work-tree=output commit -m \"Site update: {}\"".format(now))
    local("git --git-dir=output/.git --work-tree=output push -u origin master")
    local("git add --all")
    local("git commit -m \"Site update: {}\"".format(now))
    local("git push -u origin master")

def checkout_output():
    """Clone the output diretory from github"""
    local("rm -rf output/")
    local("git clone git@github.com:olinbg/olinbg.github.com.git output")

def live(port=8000):
    """Using livereload, run a local server that updates the browser"""
    build()
    server = livereload.Server()
    def live_build_ignore(s):
        return False
    server.watch('content/', build, ignore=live_build_ignore)
    server.serve(root='output', liveport=35729, port=port)
