Title: Python and Flask - Hello World
Date: 2016-08-07 09:14
Category: Python
Slug: python-and-flask-hello-world
Series: Python and Flask
Status: published

Python has a number of capable web frameworks, with [Django](https://www.djangoproject.com/) being the larger / "batteries included" option of the, and [Flask](http://flask.pocoo.org/) being the smaller / "assembly required" choice.  As with many projects in Python, I start with the [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/scenarios/web/).  Here are two quotes from the site on picking a web framework:

> The majority of new Python web applications today are built with Django.

and...

> Flask is default choice for any Python web application that isn’t a good fit for Django.

So from a quick start and learning perspective, I'm using Flask - purely a learning exercise.  I'm also going to use VS Code for the project so screenshots and info will be from there.  You can download VS Code for free [here](https://code.visualstudio.com/).

## Getting up and running

You'll want a python virtualenv before you start.  Since I'm running on an [Anaconda](https://docs.continuum.io/anaconda/) installation on windows, I'm going to install flask with a conda command, rather than pip.  Both are below:

Conda:
```
conda install flask
```

Pip:
```
pip install flask
```

Now that flask is installed, I loaded up a new folder for scripts in VS Code, and created a main.py with this block (straight from the Flask docs):

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
``` 

Screenshot:

![main.py](https://photos.smugmug.com/photos/i-xt677KF/1/O/i-xt677KF.png)

Once you run the program, you can navigate to the page in your browser:

![Hello World](https://photos.smugmug.com/photos/i-TfsSVB3/0/O/i-TfsSVB3.png)

And you'll see this in the console:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [07/Aug/2016 09:29:44] "GET / HTTP/1.1" 200 -
```

Basic Flask setup, done.  Next up, some tutorials.
