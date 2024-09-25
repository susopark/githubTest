# githubTest

This is just a sketch to practice GitHub for the first time.

As I'm writing this, I'mn going to explain the basics of Git (not GitHub, GitLab or Bitbucket, which is the same concept but my projects are on the Internet to share it with the community). The one that already comes installed in MacOS or Linux (for Windows you have to download it from the Internet, such as, Git Bash).

1. Open the Terminal or CMD.

2. Create a directory and its files:
    - mkdir newDirectory //To make a new directory.
    - cd newDirectory //To enter a directory.
    - touch dataBaseQuery.sql dataProcessing.py dataVisualization.qvs //To create a new file.

3. To initiate Git:
    - git init

4. Save new changes (push):
    - git add dataBaseQuery.sql //To save changes from that file. 
    - git add . //To save changes from all the files in the directory (recommended).

5. Commit the changes to memory (commit):
    - git commit -m 'change description'

6. Case 1 - I delete one file and create another one and save those changes:
    - rm dataBaseQuery.sql //To remove or delete the file.
    - touch webScript.js
    - ls //To list all the elements of a directory.
    - git add .
    - git commit -m 'delete sql file and create a javascript file'

7. To visualize the saves (commit) versions we made so far:
    - git log   //Provides an hash code for each commit to invoke that version afterwards

8. Invoke other changes, saves or commits:
    - git checkout hascode

9. When we invoke an older change, we travel to the past. And this implies creating a new branches from the main branch, so the main branch progress may not be affected.

10. To hook a new repository from Local to GitHub:
    - git remote add origin https://github.com/susopark/githubTest.git 
    - git push -u origin master
    - //Or you can just create in the website or in GitHub Desktop
    - //You can visualize the master branch in GitHub and its commits

11. Creating a new branch in our directory:
    - git checkout -b new-branch //To create a new branch
    - git branch //To visualize all the branches
    - touch app.py
    - git add.
    - git commit -m 'add python file'
    - git log //You can see the changes are made in the new branch and not in the main branch,.

12. You can merge the new changes from the new branch to the main branch if you want to:
    - git push origin new-branch //To push the new branch to GitHub so the community may create new changes and then suggest a merge to your main branch if you want to, through a Pull Request in GitHub.
    - //And then you Merge the Pull Request in GitHub, in case you want it.

13. To Pull the changes you don't have in local from GitHub (you Push for the changes that GitHub doesn't have from your local):
    - git pull origin master
    - git log //To check that.

GitHub is ideal to collaborate with others in a project. You don't really need GitHub if you are just to save changes from a file.