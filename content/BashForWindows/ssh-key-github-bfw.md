Title: Generating SSH Keys for Github on Bash for Windows
Date: 2016-05-06 06:56
Category: BashForWindows

If you'd rather not share SSH keys between your standard Windows installation and Bash for Windows, you can use the built-in key generator from Ubuntu to generate your ssh keys.

```
ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (path): <type>
Enter passphrase (empty for no passphrase): <type>
Enter same passphrase again:
Your identification has been saved
```

You'll have both a public and private key in your home directory.  If you want to upload your public key elsewhere, first dump it to the console (assuming you used the default path):

```
cat ~/.ssh/id_rsa.pub
```

You'll see:

```
ssh-rsa <key text>
```

Select everything before your machine name on the last line and press Ctrl+C to copy.  Open [your profile settings](https://github.com/settings/profile) on GitHub, navigate to "SSH and GPG Keys", and paste in your ssh-rsa key:

![SSH settings in GitHub]({filename}/images/2016-05-06/github.png)

You'll get a notification that the key hasn't been used yet.  Clone a repo, and you're good to go.
