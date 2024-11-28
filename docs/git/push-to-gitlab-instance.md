Push a local Repository to a GitLab Instance
======================================================================

If you want to share the repository on a gitlab or github instance, 
you create an empty project on gitlab and push the local created repository afterwards to gitlab. 


Create GitLab Project
------------------------------------------------------------

Log in to your GitLab instance, for example: [gitlab.hsrw.eu](https://gitlab.hsrw.eu). 
In this university GitLab you can log in with your university credentials.  

Then create a new project. 
Do not use a dummy/template or initialize it with a `README.md`. 
At the end gitlab will propose you some commands to upload a repository. 
Here you should extract for [later usage](#add-new-remote-url) the remote URL of this repository, which should look similar to this: 

    https://gitlab.hsrw.eu/jan-lehmkuhl/dummy-1.git



Local Preparation
------------------------------------------------------------

    cd EXISTING_LOCAL_REPO

if the repo was already pushed to another remote rename origin, otherwise skip

    git remote rename origin old-origin



Add new Remote URL
------------------------------------------------------------

#### Option 1: ssh Access
If your ssh access is configured use: 

    git remote add origin git@gitlab.com:NAME/GITLAB_REPO_NAME.git


#### Option 2: https with Token
Otherwise use https and create an [Project Acces Token](https://gitlab.hsrw.eu/help/user/project/settings/project_access_tokens) to create a smooth access from the terminal. 
Create the token with role `Maintainer` and scope `api`. 
Then add the remote URL to your local repository and add the token credentials before your remote URL like this: 

    git remote add origin https://ACCESS_TOKEN_NAME:ACCESS_TOKEN@gitlab.hsrw.eu/MYUSER/MYREPO.git



Push Content
------------------------------------------------------------

    git push --set-upstream origin --all



Check Success
------------------------------------------------------------

Now you should see your code in the GitLab WebGUI. 
