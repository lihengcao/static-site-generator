---
title: Getting Jekyll to Work Locally
date: 2023-05-03
---
Having GitHub handle the build/deployment of this blog was cool. However, I realized that relying entirely on GH means that I'd have a slow turnaround when developing, not to mention clogging up my commit history and not learning the basics of how Jekyll works. 

Some of the things I tried include:
1. Reverse engineering the GH Actions
    1. Couldn't fully figure out the commands. Probably something to do with the environment.
    1. Didn't give me any clues on what to do next.
1. Jekyll devcontainer
    1. *Technically* runs fine, but the output doesn't match what GH does. Doesn't match is an understatement: The entire blog was just "Hi," which was matches one of my files, but it didn't have a title nor the singular post. 
    1. This had output, but it just looked different, so I suspected that GH does something special to make it look different. 

I then tried adding the `github-pages` ruby gem to get the styling to work, but I encountered another error. The output was generating fine, but vscode was no longer offering to show me the preview. There waas also an error in the terminal. Of course there was a [helpful stackoverflow link](https://stackoverflow.com/questions/69890412/bundler-failed-to-load-command-jekyll/), and that was that. 

I also changed some of the boilerplate title and footers.

Pretty funny how my initial posts on this blog were about setting up the blog and the "challenges" I faced when doing it. 

## Command to run
(mainly so I don't forget)
```
bundle exec jekyll serve
```