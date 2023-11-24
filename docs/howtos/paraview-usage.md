HowTo use Paraview
======================================================================

Open Paraview without State File
------------------------------------------------------------

In Windows you open Paraview from "Windows Search" and you open the file `pv.foam` in the `case`-folder. 
In native Linux you execute: 

    make paraview-no-state


Before you see the flow variables you have to do some preparation in Paraview:  

* if the results are calculated on multiple cores, the results must be decomposed,  
  select `Case Type: Decomposed Case` and click on `Apply`  
* the results have to be, marked as visible in the pipeline browser (eye in picture below),  
* the last timestep (even for a mesh) has to be selected from the dropdown menu,  
* a flow variable from the results (e.g. p, U, ...) must be selected.  

![](../resources/paraview-first-settings.png)

afterwards you should see something like the pipe on the right side from the above picture.  
Now feel free to apply as many filters you like. 



Open Paraview with saved State File
------------------------------------------------------------

If you already have saved a state file like [paraview-state.pvsm](../../post/paraview-state.pvsm) you can apply filters from previous sessions.  
This can easy be done from command line or by help of the [Makefile](../../Makefile) with: 

    make paraview

It might be necessary to execute following makefile target in order to remove some hard coded file paths:  

    make paraview-state-preparation
