Paraview Python
======================================================================

To run [Paraview Picture Export](../../scripts/paraview-export-all.py) you need to install a further Paraview version, which has the Python capabilities with `pvbatch` and `pvpython`. 
Paraview bundled with OpenFOAM misses the Python scripting. 



Download & Extract
------------------------------------------------------------

[Download](https://www.paraview.org/download/) the executables and extract with tar: 

    cd ~/bin/paraview
    tar -xf FILE


Use `osmesa` version vor headless machines without x-server like Docker, when you have no GUI.  



Make available in PATH
------------------------------------------------------------

Do not source everything in `*/paraview/bin`. 
This can lead to unexpected behaviour e.g. with `mpiexec`.  

    which mpiexec
    # /usr/bin/mpiexec

change `.bashrc` and source `$HOME/.local/bin` after OpenFOAM.  
Then create softlinks to the desired files

    cd ~/.local/bin
    ln s ~/bin/paraview/use/bin/paraview
    ln s ~/bin/paraview/use/bin/pvbatch
    ln s ~/bin/paraview/use/bin/pvpython


test version with: 

    cd
    paraview --version
    pvbatch  --version
    pvpython --version
    which paraview
    which pvbatch
    which pvpython
