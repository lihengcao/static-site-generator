---
title: First Entry!
date: 2023-04-24
---

# Hi
Just seeing how Jekyll works (:

# First Experience
I just started using Jekyll, and I've already encountered one of the quirks. I follow the instructions to get a dummy file to show up on the blog, but no posts showed up on the homepage. After some investgation, I found out that the Jekyll "build" process ignores dates that are in the future. Not sure what timezone or date or whatever environmental variables the GH building process uses, but I guess my blog post ended up being in the future. This was confirmed when I checked the logs:
```
Skipping: _posts/2023-04-24-first-post.md has a future date
```

Whatever! I change the config to allow future posts to be displayed, and now my first post shows up!
