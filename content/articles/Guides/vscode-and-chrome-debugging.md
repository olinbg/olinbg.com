Title: VSCode and Google Chrome Debugging
Date: 2018-02-11 12:25
Category: Guides
Slug: vscode-and-chrome-debugging
Status: draft

Rapidly building applications is best with an editor and VM / app / browser that updates automatically after changes to source.  This is easy to achieve with certain setups (Java IDEs and hot swapping for example), but I've never found a great setup for this when working on web frameworks.  I'm diving into more Angular 2+ development lately, and can highly recommend [VSCode](https://code.visualstudio.com/) as a swiss-army knife for Angular.

However, the one area I found challenging to setup was direct Chrome debugging when working with TypeScript and Angular - setting breakpoints in VSCode and stopping at that line of code when visiting the right page, for example.  It's doable, just not as intuitive as you might expect.  To get started, you need the following:

* VSCode (tested on version 1.15)
* Node and npm (make sure they work standalone!)
* Google Chrome
* A project to test with (I used the angular starter [here](https://github.com/gdi2290/angular-starter))



The Github page is [here](https://github.com/beetbox/beets).

I contributed the [beets-spotify](https://github.com/olinbg/beets-spotify) plugin to generate Spotify playlists from tracks in a Beets library.
