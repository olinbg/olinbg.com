Title: Uninstall and Reinstall Bash for Windows
Date: 2016-07-31 07:51
Category: BashForWindows
Slug: uninstall-reinstall-bfw

After the most recent update for Bash for Windows, a fairly major change went into effect: you're now logged in with a "user" level account rather than "root".  This has major benefits, and works much more like any other Linux/Unix install that you'd run locally.

## Early Adopters Used *root*, not *user*

Some of the original components that I had installed under root were now not manageable by the user account - notably the Python 2.7 and 3.4 installs.  Switching back and forth to root was possible, but onerous.  Here's the command to change the default login for the Linux Sub-system (LXSS) run in PowerShell:

```
PS C:\Windows\System32\WindowsPowerShell\v1.0> lxrun
Performs administrative operations on the LX subsystem

...
    /setdefaultuser - Configures the subsystem user that bash will be launched as. If the user does not exist it will be created.
        Optional arguments:
            username - Supply the username
```

This didn't seem sustainable long-term, and I preferred to start "fresh" with a user-mode Ubuntu image from the start.  So I did some digging on uninstalling and reinstalling the LXSS.

## Uninstalling Bash for Windows

First some links:

The initial GitHub issue: [Reinstalling clean image #4](https://github.com/Microsoft/BashOnWindows/issues/4)
The Lxss command reference: [Command Reference](https://msdn.microsoft.com/en-us/commandline/wsl/reference?f=255&MSPPError=-2147217396)
User support documentation within Bash for Windows: [User Support](https://msdn.microsoft.com/en-us/commandline/wsl/user_support)

After reviewing, the key commands to execute were first to uninstall completely (instead of just removing the user install), and then reinstalling.

First, the uninstall:

```
PS C:\Windows\System32\WindowsPowerShell\v1.0> lxrun /uninstall /full
This will uninstall Ubuntu on Windows.
This will remove the Ubuntu environment as well as any modifications, new applications, and user data.
Type "y" to continue: y
Uninstalling...
```

You can confirm the directory has been removed by trying to open the path ```%USERPROFILE%\AppData\Local\Lxss``` - it should fail.

## Re-installing Bash for Windows

The reinstall was very simple - simply run a similar Lxss command:

```
PS C:\Windows\System32\WindowsPowerShell\v1.0> lxrun /install
-- Beta feature --
This will install Ubuntu on Windows, distributed by Canonical
and licensed under its terms available here:
https://aka.ms/uowterms

Type "y" to continue: y
Downloading from the Windows Store... 100%
Extracting filesystem, this will take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: <user>
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Installation successful!
PS C:\Windows\System32\WindowsPowerShell\v1.0>
```

In my case, most files were mounted in a C: folder, so I just need to reconfigure Python and other installs.  To see those steps, check out [this post]({filename}2016_05_06_pelican-python-bash.md).