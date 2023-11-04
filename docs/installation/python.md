
Standard Python
======================================================================

To execute [Python Postprocessing](../../scripts/python-postprocessing.py) from `make post` its necessary to install [Python](https://www.python.org) if its not yet present.  

    python --version

    sudo apt update
    sudo apt-get install python3


## Pandas and Matplotlib
Additionally some packages inside Python are used

    python3 -m pip install matplotlib
    python3 -m pip install pandas

~~~bash
# for matplotlib
Requirement already satisfied: matplotlib in /usr/lib/python3/dist-packages (3.5.1)

# for pandas
Requirement already satisfied: pandas in /usr/lib/python3/dist-packages (1.3.5)
~~~




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
