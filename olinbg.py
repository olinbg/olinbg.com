import os
import shutil
import sys
import socketserver
import livereload
from datetime import datetime
from subprocess import call

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
STARTING_PATH = os.getcwd()
DEPLOY_PATH = os.path.abspath(STARTING_PATH + '/../output')
print("Deploy path: {}, Starting path: {}".format(DEPLOY_PATH, STARTING_PATH))

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

def main():
    command = sys.argv[1]
    if command == 'post':
        if len(sys.argv) != 5:
            print("Post with title, slug and category")
            exit()
        post(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == 'live':
        live()
    else:
        print("Invalid command")
        exit()

def post(title, slug, category):
    """Create a markdown post with title, slug, and category"""
    today = datetime.today()
    category = category.replace(" ", "")
    f_create = "content/articles/{}/{}_{:0>2}_{:0>2}_{}.md".format(
        category, today.year, today.month, today.day, slug)
    t = POST_TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month='{0:02d}'.format(today.month),
                                day='{0:02d}'.format(today.day),
                                hour=today.hour,
                                minute=today.minute,
                                category=category,
                                slug=slug)
    os.makedirs(os.path.dirname(f_create), exist_ok=True)
    with open(f_create, 'w') as w:
        w.write(t)
    print("Post created -> " + f_create)

def build():
    call(["make", "html"])

def live(port=8000):
    """Using livereload, run a local server that updates the browser"""
    build()
    server = livereload.Server()
    def live_build_ignore(s):
        return False
    server.watch('content/', build, ignore=live_build_ignore)
    server.watch('hyde/', build, ignore=live_build_ignore)
    server.serve(root=DEPLOY_PATH, liveport=35729, port=port)

main()