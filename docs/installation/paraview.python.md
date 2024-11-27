Paraview Python for Command Line Interface
======================================================================

To run [Paraview Picture Export](../../scripts/paraview-export-all.py) under Linux you need Paraview Python capabilities with `pvbatch` and `pvpython`. 

    pvbatch --version
    pvpython --version


In Ubuntu 24.06 these tools are bundled already with the [OpenFOAM](openfoam.md) installation. 
These are shipped starting with Paraview version 5.11. 

    paraview --version


When these commands cannot be executed in the terminal, an [additional paraview](paraview.linux.manual.md) must be installed for Linux or WSL.  



Check
------------------------------------------------------------

If everything works fine the command: 

    make post


should look like this:  
~~~txt
$ make post 
cd case ;  ../scripts/python-postprocessing.py
write plot for postProcessing/residuals/0/residuals.dat
write plot for postProcessing/probes/0/p
cd case ;  pvbatch ../scripts/paraview-export-all.py
load pv.foam and paraview state
execute picture export
save renderView: 1
save renderView: 2
save renderView: 3
save renderView: 4
~~~


and export postprocessing pictures to the folder `case/visualization/paraview`  
For example:  

> ![case/visualization/paraview/renderView4.png](../../case/visualization/paraview/renderView4.png)  
