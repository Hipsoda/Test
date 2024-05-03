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
    a. git add <fliename>  :: This will add your file into the staging status(before commit)
    b. git commit -m '<the messgae you want to give>'  ::This will commit your file into local git vcs, but not will commit into GitHub
    c. git push  ::This will make your file stored in the GitHub Cloud
    d. git status  ::This will show the file status

2. Undo your uncommited files
    after you add your new file into staging staus, you can undo the operation by syntax below:
    git checkout <codenumber of file(which can be seen in the git log)>
    