
OpenFOAM Installation
===============================================================================

In general it is not necessary for OpenFOAM to have a graphical user interface. 
OpenFOAM reads text files and writes the output to text files. 
So if you have access to these files, you can run your GUI-Programs like FreeCAD and Paraview nativly under Windows. 

OpenFOAM is a Linux Programm but there are several ways to run Linux under Windows or MacOS.
Before installing OpenFOAM install Linux by your prefered method:  
* [WSL](windows-subsystem-for-linux.md) (recommended for Windows)
* A virtual machine with Linux 
   (see [openfoam.org](https://openfoam.org/download/windows-vm/))  

Beside installing OpenFOAM in a System like WSL or Docker, FreeCAD needs also a [OpenFOAM Windows installation](freecad-cfdof.md#install-cfdof-dependencies) to have access to some template files.  



OpenFOAM Installation on Linux
===============================================================================

This instructions refers to a Ubuntu 24.04 LTS installation and is described in [OpenFOAM Ubuntu instructions](https://openfoam.org/download/)  
A clean linux operating system can be applied on an USB-Stick, without major performance issues.  

Further resources:  
[OpenFOAM Linux Guide](https://cfd.direct/openfoam/linux-guide/)  
[OpenFOAM Downloads](https://cfd.direct/openfoam/download/)  
[OpenFOAM.org source files](https://github.com/OpenFOAM/OpenFOAM-11)  



Package installation 
---------------------------------------------------------------------
First you have to add a online-repository and tell Ubuntu where he find additional software

    sudo sh -c "wget -O - https://dl.openfoam.org/gpg.key > /etc/apt/trusted.gpg.d/openfoam.asc"
    sudo add-apt-repository http://dl.openfoam.org/ubuntu
    sudo apt-get update

then you can install with following command. 
Linux will download the needed files from the previous defined repository. 

    sudo apt-get -y install openfoam11
    sudo apt-get -y install build-essential



Sourcing and changing .bashrc
---------------------------------------------------------------------
When you installed OpenFOAM the binaries are at your computer, but you only can start them, when you address them directly. 
For example: 

    /opt/openfoam13/platforms/linux64GccDPInt32Opt/bin/foamRun

To make your OpenFOAM installation available in your terminal session, you can execute: 

    source /opt/openfoam13/etc/bashrc

Then you can execute foamRun at every location in your terminal directly with: 

    foamRun


To make this sourcing permanent, you can add the `source ...` command into the `~/.bashrc` file. 
This will be loaded everytime you open a terminal. 

    nano ~/.bashrc


At best, the settings in FreeCAD-CfdOF are correct, and the paths to OpenFOAM are set directly in Allmesh and Allrun. 
Then the sourcing is not necessary, but sometimes it avoids errors. 



Testing
---------------------------------------------------------------------
Now you can test the installation in Linux (also delivered by WSL or Docker) by starting: 

    foamRun -help

~~~
user@machine:~/simulations$ foamRun -help

Usage: foamRun [OPTIONS]
options:
  -case <dir>       specify alternate case directory, default is the cwd
  -fileHandler <handler>
                    override the fileHandler
  -hostRoots <((host1 dir1) .. (hostN dirN))>
                    slave root directories (per host) for distributed running
  -libs '("lib1.so" ... "libN.so")'
                    pre-load libraries
  -noFunctionObjects
                    do not execute functionObjects
  -parallel         run in parallel
  -roots <(dir1 .. dirN)>
                    slave root directories for distributed running
  -solver <name>    Solver name
  -srcDoc           display source code in browser
  -doc              display application documentation in browser
  -help             print the usage

Using: OpenFOAM-11 (see https://openfoam.org)
Build: 11-e1fc8c682ae6
~~~


Now you can try to run the main example described in the [README](../../README.md) in the root folder of this repository. 
