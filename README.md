# sup

Nanoblog CLI interface to GitHub Pages. WIP.

Setup (currently .env in the same folder, wip):
```
SUP_BRANCH=master
SUP_POSTS=_posts
SUP_REPO=myreponame
SUP_TOKEN=5473c3c11111111bc3f1588e2eba90fb00000000
SUP_TZ=Africa/Johannesburg
```

`SUP_REPO` and `SUP_TOKEN` are required. The rest have sensible defaults.

Examples:
```
sup 9pm: this thing happened @inthehood #happening
sup yesterday at 11am: i had a thought @ideabox
sup this is my current line of thinking
sup keep this somewhere https://datashaman.com @bookmarks #memes
sup "tomorrow at 12pm: this is a future post

with a body that will be included in the post. #longform-nano"
```
