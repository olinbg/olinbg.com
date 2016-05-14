Title: Helpful Pelican Settings
Date: 2016-05-12 22:52
Category: Pelican
Slug: helpful-pelican-settings
Status: published

Pelican (the static site generator that powers this site) has a number of useful settings that can change how sites are generated and displayed.  A few of these I didn't find right away - they might've been missing from pelican-quickstart or not obviously documented.  In no particular order:

### EXTRA_PATH_METADATA

```python
# Values used on this site
EXTRA_PATH_METADATA = {
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/README.md': {'path': 'README.md'},
}
```

This setting allows you to copy either paths or files directly into your output directory in Pelican.  This solves an important problem when using static hosting on sites like github pages: maintaining repository files as your site generates.

In the example above, the _CNAME_, _README_ and _.nojekyll_ configuration files are copied into the top output directory.  I can then commit those on uplaod to gh-pages.

### ARTICLE_URL and ARTICLE_SAVE_AS

```python
# Values used on this site
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
```

I wasn't as pleased with the output format of the default pelican setup, which dumps posts into the top-level directory.  The example formats the posts into a 'posts' directory using _ARTICLE_URL_, keeping the top-level cleaner.  You could also add YYYYMMDD or tags into the post path here, and _SAVE_AS_ variant can change the location of the output file.

### DELETE_OUTPUT_DIRECTORY and OUTPUT_RETENTION

```python
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", ".gitignore"]
```

To ensure a clean build before publishing, you can use _DELETE_OUTPUT_DIRECTORY_.  However, this was wiping out my .git directory each time.  I tracked down the _OUTPUT_RETENTION_ setting, that ensures on delete the files / paths listed stay intact.

### FEED_ALL_RSS

```python
FEED_ALL_RSS = 'feeds/all.rss.xml'
```

The Pelican install by default had only enabled an ATOM feed, but not RSS.  The _FEED_ALL_RSS_ setting does what it says, generating the feed in the path provided.
