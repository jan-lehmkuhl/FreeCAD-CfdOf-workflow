Paraview Python for Command Line Interface
======================================================================

pvbatch
------------------------------------------------------------

To run [Paraview Picture Export](../../scripts/paraview-export-all.py) under Linux you need Paraview Python capabilities with `pvbatch` and `pvpython`. 

    pvbatch --version
    pvpython --version


In Ubuntu 24.06 these tools are bundled already with the [OpenFOAM](openfoam.md) installation. 
These are shipped starting with Paraview version 5.11. 

    paraview --version


When these commands cannot be executed in the terminal, an [additional paraview](paraview.linux.manual.md) must be installed for Linux or WSL.  



Python Packages
------------------------------------------------------------

To execute some Python postprocessing in [paraview-export-all.py](../../scripts/paraview-export-all.py) from `make post` its necessary 
to use [Python3](https://www.python.org) with some packages.  

    python3 --version


Pandas and Matplotlib are needed and can be installed with

    # already installed in Ubuntu
    sudo apt install python3-matplotlib

    sudo apt install python3-pandas



Check Success
------------------------------------------------------------

If everything works fine the command: 

    make post


should look like this:  
~~~txt
$ make post
cd case ;  pvbatch ../scripts/paraview-export-all.py

Crete plots from postProcessing folder
==================================================
write plot for postProcessing/residuals/0/residuals.dat
write plot for postProcessing/probes/0/p

Crete ParaView visualizations
==================================================
load pv.foam
load paraview state: 
    /home/jan/workspace/cfd-lecture/example-wf/post/paraview-state.pvsm
in current working directory: 
    /home/jan/workspace/cfd-lecture/example-wf/case
Analyzing state file: ../post/paraview-state.pvsm
State file created with ParaView version: 5.11.2
WARNING: Found 915 Proxy elements without id attribute
This might cause compatibility issues with some ParaView versions
Found file references in state: {'\n        ', '\n      '}...
Attempt 1: Loading with DataPath mapping...
State loaded successfully with DataPath method
export Paraview-Views as image to path:
/home/jan/workspace/cfd-lecture/example-wf/case/visualization/paraview
Saved: 'LineChartView---Kinetic-Energy'
Saved: 'LineChartView---Velocity'
Saved: 'RenderView1'
Saved: 'RenderView2'
Saved: 'RenderView4'
~~~


and export postprocessing pictures to the folders `case/visualization/plots` and `case/visualization/paraview`  
For example:  

> ![case/visualization/paraview/renderView4.png](../../case/visualization/paraview/renderView4.png)  
