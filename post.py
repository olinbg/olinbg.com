import sys
from datetime import datetime

TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Category: {category}
Slug: {slug}
Status: draft

(Fill in)
"""


def make_entry(title, slug, category):
    today = datetime.today()
    f_create = "content/articles/{}/{}_{:0>2}_{:0>2}_{}.md".format(
        category, today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
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


if __name__ == '__main__':

    if len(sys.argv) > 3:
        make_entry(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("No title given or category given")

