# hello-world
This repository is for practicing the GitHub Flow.

Outline why developers use version control (e.g., tracking changes, collaboration, rollback, accountability).

Version control has several advantages for code development.  Every commit is saved, so if a mistake is made e.g. a file is deleted which is later required again, the original code is not lost.  Branching helps keep work on the project compartmentalized: different developers can make changes to different parts of the code without interfering with each other.  Branches also allow developers to work on the code without affecting the main branch, so users can continue to use the old code until the new code is ready to merge with it.  

Explain ways to use version control in a small Python project (e.g., commit often, meaningful messages, branches for features, pull requests for review).

A good workflow when implementing a new feature in a python project is to create a new branch in which to work.  Each change should be commited in the branch before starting on the new change, so that changes can be tracked or undone.  e.g. if you want to add an extra parameter to a function then all the files containing either the function implementation or function call should be modified and then the change should be commited with a descriptive message.  Other changes should not be made until this the commit has been made.  When the feature has been completed and tested, a pull request should be issued so that collaborators can decide whether they agree with the changes and if so, the branch can be merged into the original branch (probably main).  Finally, the branch should be deleted.
