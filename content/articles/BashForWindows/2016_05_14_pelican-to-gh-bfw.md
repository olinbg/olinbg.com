Title: Publish Pelican to GitHub from Bash for Windows
Date: 2016-05-14 06:37
Category: Bash For Windows
Slug: pelican-to-gh-bfw
Status: published

_(You probably want to review [my earlier post on setting up Python and Pelican]({filename}2016_05_06_pelican-python-bash.md), and if you haven't already, [set up ssh keys as well]({filename}2016_05_06_ssh-key-github-bfw.md))_

There are a number of places to publish a Pelican site, but I was immediately drawn to [GitHub Pages](https://pages.github.com/):

* Free to use
* Integrates with your existing Github account
* Natively supports static sites, like Jekyll and Pelican
* Easy to automate on the command line

The [documentation quickstart for Pelican](http://docs.getpelican.com/en/latest/quickstart.html) helps you get a site built.  But how do you publish this site up to github pages?

### Ensure the site builds and displays

Fire up Bash for Windows and change to your site directory.  Assuming you're using the makefile, run _make server_ to create your output directory and load it in your local browser.  For my site:

```
cd olinbg
make serve
(site is now running at http://localhost:8000)
```

If [the localhost link renders](http://localhost:8000), you're ready to upload.

### Create the repo

Start with the guide right on the [GitHub Pages](https://pages.github.com/) site.  From their current guide:

![Create a repo]({filename}/images/2016-05-14/repo.png)

### Initial push

Before you push all the content, copy your site content into the _username.github.io_ directory, then push the content.  In Bash for Windows (replace _username_ and _your_pelican_output_dir_):

```
cp -r output username.github.io
cd username.github.io
git add --all
git commit -m "Initial commit"
git push -u origin master
```

### Edit description

After pushing your first content, head over to your repo on github.  You'll see a github pages header where you can set a description and site address (should match your address from earlier):

![Edit]({filename}/images/2016-05-14/edit.png)

### Test the page

Now navigate to the actual page: _username.github.io_.  You should see your start Pelican content.

![Site]({filename}/images/2016-05-14/site.png)

### Adding a README

I wanted to ensure my github repo had a README added (standard practice).  Rather than ignore this in the output directory that's uploaded to github, I added this as file to copy in my pelicanconf.py:

```
mkdir content/files
touch content/files/README.md
(edit the README with content)
```

Now add the following to your pelican configuration:

```python
EXTRA_PATH_METADATA = {
    'files/README.md': {'path': 'README.md'},
}
```

### Uploading your 'content' directory

You can follow similar steps using git to upload your 'content' folder.  This is advisable so you have a working repo as you edit your site.  Instructions are more straightforward here - simply create a new repo for you source content, and follow the "Initial push" instructions above.
