HowTo review CFD-calculation-results with Paraview
======================================================================

If 3D data is created, you can use [Paraview](../../installation/paraview.md) to review them. 



Open Paraview without State File
------------------------------------------------------------

### Windows
In Windows you open Paraview from "Windows Search" and you open the file `pv.foam` in the `case`-folder. 


### Linux
In native Linux you execute: 

    make paraview-no-state


### Data Preparation
Before you see the flow variables you have to do some preparation in Paraview:  

* if the results are calculated on multiple cores, the results must be decomposed,  
  select `Case Type: Decomposed Case` and click on `Apply`  
* the results have to be, marked as visible in the pipeline browser (eye in picture below),  
* the last timestep (even for a mesh) has to be selected from the dropdown menu,  
* a flow variable from the results (e.g. p, U, ...) must be selected.  

![](../../resources/paraview-first-settings.png)

afterwards you should see something like the pipe on the right side from the above picture.  
Now feel free to apply as many filters you like. 



Open Paraview with saved State File
------------------------------------------------------------

If you already have saved a state file like [paraview-state.pvsm](../../../post/paraview-state.pvsm) you can apply filters from previous sessions.  
This can easy be done from command line or by help of the [Makefile](../../../Makefile) with: 

    make paraview-run


It might be necessary to execute following makefile target in order to remove some hard coded file paths:  

    make paraview-state-preparation


At Windows you can use the File menu and `Load State ...`  



Automatic Picture Export
------------------------------------------------------------

If you stored a paraview state file and the [paraview-python installation](../../installation/paraview.python.md) is correct, 
the postprocessing by [scripts/paraview-export-all.py](../../../scripts/paraview-export-all.py) 
exports pictures from different layouts to [case/visualization/paraview](../../../case/visualization/paraview/renderView4.png). 
This can be started by:  

    make post


The needed state file is defined in the [Makefile](../../../makefile#L20) as variable `paraviewState` and
in [scripts/paraview-export-all.py](../../../scripts/paraview-export-all.py#L11).  



Check Success
------------------------------------------------------------

See if [case/visualization/paraview](../../../case/visualization/paraview/renderView4.png) contains all your Paraview Layouts.  
