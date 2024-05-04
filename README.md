# Personal Tutorial on Git and GitHub

### Introduction to Git and GitHub
Git is a Version Control System and GitHub is a website based on Git that provides
relevant service

We have central VCS(Version Control System) and Distributed VCS, the diff between them
is the manner of storge.
For central VCS, Files are stored in a server and have only one copy.
Fore distributed VCS, Files are stored in everyone's personal computer, and every one has an 
copy.

So, why do we need distributed VCS? Because it brings many advantages.
1. Files are easy to track and will not be missed, for central VCS, once the cetral Server breaks down,
all relevant files stored in the server will get lost
2. Distributed VCS help facilitate team work



### Frequently Used Operations in Git and Git Hub
1. Commit Your new code into Git and GitHub
    a. `git add <fliename>`  :: This will add your file into the staging status(before commit)
    b. `git commit -m '<the messgae you want to give>'`  ::This will commit your file into local git vcs, but not will commit into GitHub
    c. `git push`  ::This will make your file stored in the GitHub Cloud
    d. `git status`  ::This will show the file status

2. Undo your modified files
    before you add your modified file into the staging stage, you can undo your operaions
    `git checkout -- <filename>`

    if you have multiple modified files, you can undo by:
    `git checkout -- .`
    
3. Undo your committed files
    after you commit your files into the vcs, you can undo things followed by the next steps:
    a. find the commit code using `git log`
    b. `git revert <lognumber>`

4. Reset your file status into one status before
    find the lognumeer
    `git reset <lognumber>`



### Braches in Git 
1. Why do we need Branches?
    The Answer is obvious. When doing something experimental or doing some team work, like writing different 
    functions of a product, you need seperate works, so branches allow us to do seperate works and will not interfere
    other works

2. How to Create, show, delete, merge branches?
    `git branch`  This will show you all the current branches
    `git branch <branchname>` This will create a new branch 
    `git checkout <branchname>` This will switch to a branch
    `git merge <branchname>` This will merge your new branch into the master/main(under the main branch)
    `git checkout -b <branchname>` This will create a branch and switch to the new branch
    `git branch -d <branchname>` This will delete the bracnch

### HEAD
    HEAD is the commit number of the most recent committed file, and it is stored in hte .git/HEAD, and it is in constantly
    change, now I will list several usage of HEAD
1. difftool
    a. `git difftool <older  commitnumber1> <new commitnumber2>`
    b. `git difftool HEAD~1 HEAD~2`

2. detached HEAD
    in not main branch, you can checkout to older state, in this condition, HEAD becomes detached HEAD, it doesn't show 
    the latest commitcode

### .gitignore file
    You may be have some file and not want to commit it to the vcs, and you can create a gitignore file and puts the file name into it 
1. Create gitignore file
    `touch .gitignore`

2. Put the name you ignore into the gitnore file
    Copy-Paste
3. commit the .gitignore file

### Diff and Merge by using meld
    Meld is a tool for user. It provides good-looking using for difftool insetead of vim and it is convenient ot merge
    modified file if you modify the file both locally and in GitHub

1. You get the latest code version from github by using 
    `git pull`  


### Pull Request
    I will just describe the process of using Pull Request.
    Now we have two persons(A, B), and A is the owner of a repo, B is a active coder.
1. B fork the repo to his own repo, and modify relevant files
2. B pull request
3. A check the modified file and make comments
4. B revise the file
5. Repeat
6. A accept the pull request and merge the modified file to certain branch 


