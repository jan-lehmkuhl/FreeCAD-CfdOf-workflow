Push a local Repository to a GitLab Instance
======================================================================

If you want to share the repository on a gitlab or github instance, 
you create an empty project on gitlab and push the local created repository afterwards to gitlab. 


Create GitLab Project
------------------------------------------------------------

Log in to your GitLab instance, for example: [gitlab.hsrw.eu](https://gitlab.hsrw.eu). 
In this university GitLab you can log in with your university credentials.  


### Create an empty Project
Then create a new project. 
* Do not use a dummy/template and
* do not initialize it with a `README.md` 

At the end gitlab will propose you some commands to upload a repository. 
Here you should extract for [later usage](#add-new-remote-url) the remote URL of this repository, which should look similar to this: 

    https://gitlab.hsrw.eu/jan-lehmkuhl/dummy-1.git


### Share it
If you want other people to participate, 
set "Project visibility" to `Public` (Project -> Settings -> General -> Visibility)
or invite Users as `Developer` (Project -> Manage -> Members)



Push Local Repository
------------------------------------------------------------

    cd EXISTING_LOCAL_REPO


### Add new Remote URL
if the repo was already pushed to another remote rename origin, otherwise skip

    git remote rename origin old-origin


Use https for remote URL and 
create an [Project Acces Token](https://gitlab.hsrw.eu/help/user/project/settings/project_access_tokens) in GitLab to create a smooth access from the terminal. 
Create the token with role `Maintainer` and scope `api`. 
Then add the remote URL to your local repository and add the token credentials before your remote URL like this: 

    git remote add origin https://ACCESS_TOKEN_NAME:ACCESS_TOKEN@gitlab.hsrw.eu/MYUSER/MYREPO.git


The new url should now be printed by

    git remote --verbose


### Push Local Content
    git push --set-upstream origin --all



Check Success
------------------------------------------------------------

Now you should see your code in the GitLab WebGUI. 
