
This example contains everything to run a complete [OpenFOAM]-simulation, created by the [CFDOF-Plugin] within [FreeCAD]. 



First Run
=================================================================

The first run is to do a functional test of your personal setup and do the run without changes by the scripts.  


get files
------------------------------------------------------------
You can clone this example-repository directly from gitlab with the command line interface (CLI): 

    cd SOMEWHERE    # (e.g. /home/USER/simulations)
    git clone https://gitlab.com/schlupp/example-cfdof-workflow.git
    # creates a folder "example-cfdof-workflow" with all files inside

with a specified folder like `git clone <REPOSITORY> <FOLDER>` after the the previous command the repository files will be placed inside this folder.  

If you have no internet connection and a downloaded zip file you can extract the files in the GUI or in the CLI to a an arbitrary place: 

    unzip DOWNLOAD.zip -d ARBITRARYFOLDER


installation and troubleshooting
-----------------------------------------------------------
Detailed installation instructions for all operating systems are located in `docs/installation-instructions/*.md`. 
Especially set the CfdOF-Plugin Output Directory to `.`. 

    doc/installation-instructions/freecad-cfdof.md
    doc/installation-instructions/openfoam.md
    doc/installation-instructions/additional-tools.md

The most important linux commands are shown in this [linux-guide]. 
These are essential and you should try at least 60% and understand the meaning from all. 


start meshing and openfoam-solver
------------------------------------------------------------
If everything is setup properly you should be able to start the complete calculation from the root folder directly after downloading with: 

    cd example-cfdof-workflow
    make all

afterwards some results can be reviewed with paraview:

    make viewResults

Before the flow variables can be seen in Paraview:  
* the results have to be, marked as visible in the pipeline browser (eye in picture below),  
* if the results are calculated on multiple cores, the results must be decomposed,  
  select `Case Type: Decomposed Case` and click on `Apply`  
* the last timestep (even for a mesh) has to be selected from the dropdown menu,  
* a flow variable from the results (e.g. p, U, ...) must be selected.  

![](doc/resources/paraview-first-settings.png)

afterwards you should see something like the pipe on the right side from the above picture



Detailed Workflow
=================================================================

If everything is setup correctly you can start to look deeper in the scripts and do small changes to get familiar with your tools.  
Keep in mind: Do only small changes and verify the results after every change.  


Makefile - a dictionary for your possible cli tasks
-----------------------------------------------------------

Please use an editor to look into `./Makefile`. 
Here you find a list of tasks (in Makefiles they are called "targets") you can perform within this example. 

    gedit Makefile

all targets can be started with following command in the command line interface: 

    make TARGETNAME

Within the `Makefile` you find a list of targets and after each target with an indent the commands, which will be executed, when you call a specific target.  
~~~Makefile
TARGET1:
    target1-bash-command1
    target1-bash-command2

# non-executed comment for TARGET2  
TARGET2:
    target2-bash-command1
    target2-bash-command2
~~~

To know what you can do, you should read the `Makefile` in the root folder of this project. 
You should also know how the different targets work to understand the processes. 


.1. CFD Preprocessing: FreeCAD GUI preprocessing with CfdOF-Plugin
----------------------------------------------------------
With `freecad freecad-cfd.FCStd` or `make openfreecadgui` you can open freecad and loading directly the stored data in the linked freecad-file. 

    freecad freecad-cfd.FCStd


### Step 1: creating a geometry
This [FreeCAD-Tutorial] is a good start to get used to FreeCAD for creating 3D Models.  
[FreeCAD-Tutorial]: https://www.freecadweb.org/wiki/Creating_a_simple_part_with_PartDesign

Afterwards you should have opened FreeCAD and a body with a 3D-geometry. 


### Step 2: modifying the cfd setup
To do the CFD preprocessing switch to the CfdOF Workbench inside FreeCAD. 

#### creating the CFD-FreeCAD-Container
When you starting from scratch, you need to create the FreeCAD container which are shown afterwards in the tree at the level from `Body`: 
* mark the `geometry/Body` and then "**Create an analysis** container with a CFD solver" for this Body
* mark the `geometry/Body` and then "**Create a mesh** using cfMesh, snappyHexMesh or gmsh" for this Body

in this example these are already there


#### changing cfd setup
Now you can doubleclick on the different settings and change the values if needed.  
If not existing, for every Face has a boundary condition to be applied. 


### Step 3: export mesh and case settings to OpenFOAM text files
When the preprocessing is finished you export the mesh and cfd settings. 
* Doublecklick on `geometry/CFDAnalysis/Body001_Mesh` and execute the "Write mesh case"-Button inside the FreeCAD-Tasks
* Doublecklick on `geometry/CFDAnalysis/CfdSolver` and execute the "Write"-Button inside the FreeCAD-Tasks

These commands will write text files to the subfolders `meshCase` resp. `case` into the directory specified in the CfdOF-Plugin-Settings. 


.2. CFD meshing: create a mesh
----------------------------------------------------------
The geometry creation and meshing setup is already prepared in the previous section with Freecad.  
Therefore you can now create the mesh based on the text and stl-files in the folder `meshCase` with:

    cd meshCase
    ./Allmesh

or using the `Makefile` in the project root directory with the command: 

    make mesh

### review the meshing process & the mesh
Review the file `meshCase/Allmesh` for detailed information of the meshing process and read from the [OpenFOAM-documentation] the [OpenFOAM-User-Guide]. 
[Chapter-5] covers the meshing process.  

Then you should have a look in the created files, to get a feeling of the process. 
They are in the folder `meshCase/constant/polyMesh` and especially in the file `points`. 

Afterwards you should review the created mesh with in a 3D viewer: 

    make viewMesh


.3. CFD solving: starting the calculation
----------------------------------------------------------
with the created mesh in `meshCase` and the exported setup-files in the folder `case` you can start the calculation with: 

    cd case
    ./Allrun

or using the `Makefile` with

    make run

Review the file `meshCase/Allrun` for a detailed review of the calculation process and read from the [OpenFOAM-documentation] the [OpenFOAM-User-Guide]. 

Then you should explore folder structure in `case`.  
Before calculation starts three folders exists:  
~~~bash
├── case
│   ├── 0.org
│   ├── constant
│   └── system
~~~
the file structure is documented in [Chapter-4.1] from the User Guide.


.4. CFD postprocessing: Review the output
----------------------------------------------------------
Afterall now its time to review the computed fluid flow. 
This might be the last step of a long journey and you might be exhausted, but this is the most important part. 
Here you get your information you can use to answer questions. 
So **take your time and investigate the flow** before you start your next calculation. 

    make viewResults



Further Resources
=================================================================

### doc
in `./doc` are different additional information stored in Markdown (*.md) files.

### meshCase & case
in `./meshCase` and `./case` are the from FreeCAD exported setting files for OpenFOAM. The `Allmesh` resp. `Allrun` inside these folders should directly create the mesh resp. the calculation results inside these folders.  


[FreeCAD]:                  https://www.freecadweb.org/
[CFDOF-Plugin]:             https://github.com/jaheyns/CfdOF
[OpenFOAM]:                 https://openfoam.org/

[linux-guide]:              https://cfd.direct/openfoam/linux-guide/

[OpenFOAM-documentation]:   https://cfd.direct/openfoam/documentation/  
[OpenFOAM-User-Guide]:      https://cfd.direct/openfoam/user-guide/  
[Chapter-4.1]:              https://cfd.direct/openfoam/user-guide/v7-case-file-structure/#x16-1220004.1
[Chapter-5]:                https://cfd.direct/openfoam/user-guide/v7-mesh/#x23-1670005  