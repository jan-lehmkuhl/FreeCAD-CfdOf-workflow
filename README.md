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
    * a [paraview script](scripts/paraview-export-all.py) to export all "layouts" from predefined [Paraview-State-file](post/paraview-state.pvsm) (compare [docs](docs/cfd-steps/postprocessing/3d-data-with-paraview.md#open-paraview-with-saved-state-file)).  


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



Running the Example
------------------------------------------------------------

If the installation is setup properly you should be able to calculate this CFD calculation. 
The actual [OpenFOAM-case-files](docs/howtos/case-folders.md) of this example are already exported from FreeCAD-CfdOF-Plugin and tracked in git.  

If the [Postprocessing](#postprocessing-results) for the actual state was successful, 
you may change the [preprocessing in FreeCAD](docs/cfd-steps/preprocessing/README.md) 
and modify geometry, mesh and boundary conditions. 
Then you export from FreeCAD to the [case folder](docs/howtos/case-folders.md) and 
you can run the calculation (see [CFD-Steps](docs/cfd-steps/README.md)) with only one command:  

    cd example-cfdof-workflow
    make


At Windows this should be also executed in [WSL](docs/installation-instructions/openfoam.md#option-1-windows-subsystem-for-linux-wsl).  



Postprocessing Results
------------------------------------------------------------

As final calculation results you should get some postprocessing pictures which are located in the folder `case/visualization/paraview` and `case/visualization/plots`. 
For example:  

> ![case/visualization/plots/residuals.png](case/visualization/plots/residuals.png)  
> ![case/visualization/paraview/renderView4.png](case/visualization/paraview/renderView4.png)  




Further Resources
------------------------------------------------------------

Please review the detailed documentation in folder `./docs`.



[FreeCAD]:                  https://www.freecadweb.org/
[CFDOF-Plugin]:             https://github.com/jaheyns/CfdOF
[OpenFOAM]:                 https://openfoam.org/
