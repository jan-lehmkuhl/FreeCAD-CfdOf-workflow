OpenFOAM Usage in Docker/Podman Container
======================================================================

When using a different OS than Linux it might be a nice way to use Docker container to run OpenFOAM. 
Unfortunately the actual docker container does not support X11 and the rendering used for [Paraview with Python](paraview.python.md) does not work for automatic [postprocessing](../../README.md#postprocessing-results).  



Install Runtime
------------------------------------------------------------

First you have to install a container runtime like 
* [Docker Engine](https://docs.docker.com/engine/install)  
* [Podman](https://podman.io/docs/installation) as full open-source alternative  



Start the OpenFOAM Container
------------------------------------------------------------

The OpenFOAM Foundation provides OpenFOAM installations provided in containers to download at [hub.docker.com](https://hub.docker.com/u/openfoam).  
You can start the container inside the example-workflow root folder with: 

    cd example-cfdof-workflow
    docker run --user $(id -u):$(id -g) --volume $(pwd):/host --workdir /host -it openfoam/openfoam11-paraview510


When you do not want to enter the whole command every time you can add an alias to your profile. 
Change your `.zprofile` on MacOS or your `.bashrc` on Linux and enter following command: 

    alias docker-openfoam='docker run --user $(id -u):$(id -g) --volume $(pwd):/host --workdir /host -it openfoam/openfoam11-paraview510'

After restarting the terminal you can start the container with `docker-openfoam`. 




RESOURCES
======================================================================

[openfoam.com - Mac and Docker](https://www.openfoam.com/download/openfoam-installation-on-mac-using-docker)  
