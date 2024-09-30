Workflow for FreeCAD with CfdOF-Plugin and OpenFOAM
=================================================================

Welcome to my example to run a [OpenFOAM]-simulation, created by the [CFDOF-Plugin] within [FreeCAD]. 

This repository contains
* a [FreeCAD file](freecad-cfd.FCStd) which contains a simple CFD setup 
* the FreeCAD-exported OpenFOAM files to calculate: 
    * the mesh stored in folder `meshCase`  
    * the flow simulation stored in folder `case`  
      (compare [case folder docs](docs/howtos/case-folders.md))
* a [makefile](Makefile) to perform all basic tasks without remembering long commands 
  (see [Makefile docs](docs/howtos/makefiles.md))
* a lot of documentation in the `docs` folder  
* some scripts to simplify the postprocessing
    * a [python script](scripts/python-postprocessing.py) to plot residuals and monitor points.  
    * a [paraview script](scripts/paraview-export-all.py) to export all "layouts" from predefined [Paraview-State-file](post/paraview-state.pvsm) (compare [docs](docs/howtos/paraview-usage.md#open-paraview-with-saved-state-file)).  


The first run is to do a functional test of your personal cfd-installation and do an automatic run without changes.  



Get Files
------------------------------------------------------------

To do a cfd-simulation you need a cfd-setup. 
Therefore you clone (copy) this example-repository directly from GitLab with the command line interface (CLI): 

    cd <SOMEWHERE>    # (e.g. /home/USER/simulations)
    git clone https://github.com/jan-lehmkuhl/FreeCAD-CfdOf-workflow

This creates a folder "example-cfdof-workflow" with all files inside. 
With a specified folder like `git clone <REPOSITORY> <FOLDER>` after the the previous command the repository files will be placed inside this folder.  

If you have no internet connection and a downloaded zip file you can extract the files in the GUI or in the CLI to a an arbitrary place: 

    unzip <DOWNLOAD>.zip -d <ARBITRARYFOLDER>



Installation and Troubleshooting
------------------------------------------------------------

Detailed installation instructions for all operating systems are located in [`docs/installation/*.md`](docs/installation/README.md). 
Especially set the CfdOF-Plugin Output Directory to `.` or a good known place. 



Preprocessing
------------------------------------------------------------

If the installation is setup properly you should be able to calculate your own CFD calculations. 
Therefore you normally have to do the [preprocessing](docs/howtos/preprocessing-steps.md) and modify geometry, mesh and boundary conditions. 

When you have not yet successfully finished the [Postprocessing](#postprocessing) for this example, skip this part. 
Later you come back and redo this process starting from this step again and again. 
Do only small changes: 
* to keep a working CFD environment  
* to be able to draw solid conclusions (With to big steps you cannot). 

Keep in mind: **Do only small changes to the cfd setup** and verify the results after every change.  


**Define your project**
Before you start, think about your expectations of this cfd project. 
* Why are you doing this? 
* What did you want to know? 
* What assumptions can you tolerate without loosing the accuracy you need? 

If you did not answer these kind of project management questions before you start, you will be lost during the process and not succeed!



Meshing and Solving
------------------------------------------------------------

To execute the calculation start the process from the repository root folder. 
At Windows this should be also executed in [WSL](docs/installation-instructions/openfoam.md#option-1-windows-subsystem-for-linux-wsl) Linux:  

    cd example-cfdof-workflow
    make all

This includes: 
* [creating the mesh](docs/howtos/create-mesh.md) and 
* [solving the CFD case](docs/howtos/solve-cfd-case.md).  



Postprocessing
------------------------------------------------------------

After the calculation you should see the numerical values in file [`case/processor0/100/U`](case/processor0/100/U), 
which is the data for the velocity in the 100 iteration.  

~~~c++
dimensions      [0 1 -1 0 0 0 0];

internalField   nonuniform List<vector> 
2275
(
(-0.0041313212 0.021062818 -3.0098098)
(0.043862117 -0.15867647 -3.2610956)
(0.013769403 0.10046274 -2.9954474)
(0.056011809 -0.089816178 -3.221244)
(-0.097244635 0.076614349 -3.2684462)
(0.034121441 0.1890505 -2.9816516)

...
~~~

To analyze this data in a more convenient graphical way you should use Paraview. 
The details are described in this [HowTo](docs/howtos/paraview-usage.md) but
if everything is setup correct, you can open Paraview with: 

    make paraview


If you stored a paraview state file the postprocessing for [scripts/paraview-export-all.py](scripts/paraview-export-all.py), 
the pictures from different layouts are stored in [case/doc/paraview](case/doc/paraview/renderView1.png) after executing:  

    make post

The needed state file is defined in the [Makefile](Makefile#L20) as variable `paraviewState`. 


Afterall now its time to review the computed fluid flow. 
This might be the last step of a long journey and you might be exhausted, but this is the most important part. 
So **take your time and investigate the flow** before you start your [next calculation](#preprocessing). 



Further Resources
------------------------------------------------------------

in `./doc` are different additional information stored in Markdown (*.md) files.

[FreeCAD]:                  https://www.freecadweb.org/
[CFDOF-Plugin]:             https://github.com/jaheyns/CfdOF
[OpenFOAM]:                 https://openfoam.org/
