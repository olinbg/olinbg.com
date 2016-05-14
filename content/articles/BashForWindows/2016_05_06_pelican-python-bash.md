Title: Python and Pelican on Bash for Windows
Date: 2016-05-06 18:40
Category: BashForWindows
Slug: pelican-python-bash

This site is up and running after setting up [Bash for Ubuntu for Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about) and [Pelican](http://blog.getpelican.com/).  There are a few issues on Bash for Windows right now, but seeing Ubuntu's command-line capabilities on Windows 10 is eye-opening for long-time Windows users.

## Installing Bash for Windows

You'll need [Windows Insider](https://insider.windows.com/) enabled on Windows 10 64-bit, and also [developer features](https://msdn.microsoft.com/en-us/windows/uwp/get-started/enable-your-device-for-development) set for Windows updates.

[This post on StackOverflow](http://stackoverflow.com/questions/36352627/how-to-enable-bash-in-windows-10-developer-preview) was also helpful.

You should now have the right Windows build (at least 14316):

![About]({filename}/images/2016-05-06/about.png)

![Windows Build]({filename}/images/2016-05-06/build.png)

The Bash subsystem installation is straightforward.  I followed Microsoft's guide [here](https://blogs.msdn.microsoft.com/commandline/2016/04/06/bash-on-ubuntu-on-windows-download-now-3/), on the Windows Command Line blog.

Fire up Bash, and you've got a blinking cursor.

## Installing Python

The Python installation is far less involved, though you'll need to install directly (sudo apt-get) rather than using a virtual environment.  This is due to an issue around symlinks in Bash for Windows (details are [here](https://github.com/Microsoft/BashOnWindows/issues/201)).  **UPDATE** - looks like the fix is in the latest build, give it a shot!


The following command gets python and pip up and running.

```
sudo apt-get install python3-pip
```

Similar for git:

```
sudo apt-get install git
```

The magic of Bash for windows - no Cygwin installation required here.

## Installing Pelican

If you're interested in Pelican, the installation should also be easy with python:

```
sudo pip install pelican markdown six
```

However, *this didn't work in Bash for Windows*, again due to issues around filesystem errors and links ([this StackOverflow](http://stackoverflow.com/questions/36842969/python-3-pip-packages-install-on-ubuntu-on-windows-failing-with-errno-22) got closest to my issue).

What ended up working is running each of the install commands individually, because the packaging step at the end is failing.  It's a major hack, but got me up and running for now.  If this isn't addressed in the next developer build, I'll file an issue for it.

Once Pelican is up and running, I recommend the [documentation quickstart](http://docs.getpelican.com/en/latest/quickstart.html) as a first step.
