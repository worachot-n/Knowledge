---
id: fwkslo2dbabvf61mqdybl1x
title: Init
desc: ''
updated: 1655302340364
created: 1655282389157
---

0. Have git install
1. Make an empty repo on github: <https://github.com/new>
2. open your CLI
   1. recommend git bash in windows: <https://git-scm.com/downloads>
   2. Linux: anything should work
   3. MacOS: Terminal, iTerm2, etc.
3. Navigate to where you want your repo placed using the CLI commands:
   1. cd, pwd, ls
4. Pull the repo down to your machine:
   1. git clone < URL >
   2. git status
   3. git branch
5. Now we're ready to get started!
   1. from here on we can use VSCode to open the repo directory or continue with VIM in the CLI
6. Make a document README.md
7. Add some content to it then save it
8. Check the repo status git status
9. Changes have been made from the snapshot we want to publish those to production. How?
   1. git add README.md
   2. git commit -m "< MY COMMIT MESSAGE >"
   3. git push
   4. check remote (what does remove v.s. local mean?)
10. You're done thats basically the personal workflow.
