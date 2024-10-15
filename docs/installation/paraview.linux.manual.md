Manual Paraview Installation in Linux
======================================================================

This should only be necessary, when the [Python in Paraview](paraview.python.md) is not working.  



Download & Extract
------------------------------------------------------------

[Download](https://www.paraview.org/download/) the Linux executable and extract with tar inside WSL: 

    cd 
    mkdir bin
    cd bin
    tar --extract --file FILE


Use `osmesa` version for headless machines without x-server like Docker, when you have no GUI.  



Make pvbatch and pvpython available in PATH
------------------------------------------------------------

"pvbatch" from the downloaded paraview must be available from command line. 
Often the it refers to the OpenFOAM version which has no build-in python.  

Change `.bashrc` and source `$HOME/.local/bin` after OpenFOAM. 
Open a new terminal and test the order (`~/.local/bin` at the top) with:  

    echo $PATH | tr : '\n'


Then create softlinks to the desired files

    cd ~/.local/bin

    ln -s ~/bin/ParaView-XXXXX/bin/pvbatch
    ln -s ~/bin/ParaView-XXXXX/bin/pvpython


test installation version with following commands, which should refer to your new ParaView version: 

    cd
    pvbatch  --version
    pvpython --version
    which pvbatch
    which pvpython


Do not source everything in `*/paraview/bin`. 
This can lead to unexpected behaviour e.g. with `mpiexec`.  
