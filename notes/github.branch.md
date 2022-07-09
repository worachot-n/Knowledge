---
id: 92owytnfb5vckjwappljady
title: Branch
desc: ''
updated: 1655308234162
created: 1655306185388
---
1. Check your current branch **git branch**
2. Make a new branch **git branch < BRANCH-NAME >** (no spaces)
   1. Alternative combine the next with one using: **git checkout -b < BRANCH-NAME >**
3. Switch to your new branch **git switch < BRANCH-NAME >**
4. Then repeat your workflow above WITH A NEW FILE until you get to step 11.3, the **git push**

---

1. At this point you're on < BRANCH-NAME >, you're staged (**git add < YOUR NEW FILE >**), committed (**git commit -m < YOUR COMMIT MESSAGE >"**) and are ready to push your branch to the remote.
2. To push the branch to the remote reflects your local repo branches and all, push the branch with: **git push origin < BRANCH-NAME >**
3. Now the branch is on github ready for the PR process andd to be merged.
4. Before requesting a merge or after getting feedback you want to make some final revisions to the code, for this all you need to do is:
   1. Make sure you're on the feature branch **git branch**
   2. Make your changes
   3. Stage them **git add < FILE NAME >**
   4. Commit them **git commit -m "< YOUR COMMIT MESSAGE >"**
   5. Push them **git push**
5. Merge on Github or you can always merge locally by
   1. Return to "production" branch (master/main) with **git switch master**
   2. Then merge **git merge < BRANCH-NAME >**
6. If merging on the remote repo (Github) You'll want to update your local copy of "Production" with **git pull**
7. If you're done with that branch and have no further use for it, tidy uo with git branch -d < BRANCH-NAME >
8. You'll want to have an updated work tree (this is very easy to see in the Git Graph Extension) so also run **git fetch --prune** to prune the tree of deleted branches.
