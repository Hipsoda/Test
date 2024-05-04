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
