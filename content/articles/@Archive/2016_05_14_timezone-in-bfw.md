Title: Setting Timezone in Bash for Windows
Date: 2016-05-14 7:08
Category: Bash For Windows
Slug: timezone-in-bfw
Status: draft

Really quick and easy change, but one that didn't work correctly on my [initial Bash for Windows install]({filename}2016_05_06_pelican-python-bash.md) - timezone!

Initially I was getting UTC from _date_:

```
date "+%Y-%m-%d %H:%M:%S"
2016-05-14 11:11:00
```

A single link will allow Bash For Windows to pick up the right timezone.  In my case, I'm looking for EST (New York):

```
sudo ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
```

Running date again:

```
date "+%Y-%m-%d %H:%M:%S"
2016-05-14 07:12:21
```

To see the other timezones available:

```
cd /usr/share/zoneinfo
ls -l
```