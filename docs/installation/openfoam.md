
OpenFOAM Installation on Windows
===============================================================================
[openfoam.org/download/windows](https://openfoam.org/download/windows/)  
OpenFOAM is a Linux Programm but there are several ways to run it under Windows.  

In general it is not necessary for OpenFOAM to have a graphical user interface. 
OpenFOAM reads text files and writes the output to text files. 
So if you have access to these files, you can run your GUI-Programs like FreeCAD and Paraview nativly under Windows. 

Beside installing OpenFOAM in a System like WSL or Docker, FreeCAD needs also a [OpenFOAM Windows installation](freecad-cfdof.md#install-cfdof-dependencies) to have access to some template files.  



Option 1: Windows Subsystem for Linux" (WSL) (Recommended)
---------------------------------------------------------------------
A [Windows-10-installation] should be possible with the builtin "Windows Subsystem for Linux" (WSL) in Windows 10. 
Beside the [WSL-activation] the installation should be very similar to the Linux installation described in the [next chapter](#openfoam-installation-on-linux).  


### WSL Installation
1. read: [openfoam.org-help](https://openfoam.org/download/windows-10/)

2. Activate Windows Subsystem for Linux (WSL) like described in [WSL-activation].  
   For the first time you need Administrator rights in the Powershell to execute:  
   
        wsl --install

   Then restart

3. install your desired Distro from `Microsoft Store` or 
   use Ubuntu, which should be installed by default after restart. 
   At the end you can open Linux/WSL by typing e.g. "Ubuntu" in your Windows Search and get a terminal like:  
   > ![](../resources/wsl-ubuntu.png)  

4. Install OpenFOAM inside WSL described in the Linux-Installation-Chapter below  

[Windows-10-installation]: https://openfoam.org/download/windows-10/  
[WSL-activation]: https://learn.microsoft.com/en-gb/windows/wsl/install  


### hard disc access
The hard-disks (e.g. `C:`, `D:`) are mounted in the WSL at `/mnt/c` and `/mnt/d`. 
To access these data change your directory (`cd`) to these folders:

    cd /mnt/c/YOURDIRECTORY


Option 1b: Docker
---------------------------------------------------------------------
When installing FreeCAD with CfdOF-Plugin described in [docs](freecad-cfdof.md) in Windows, there will also be OpenFOAM installed in an Docker environment. 
The file downloaded and installed is specified in the download section within FreeCAD-CFD-Setting and points to [sourceforge](https://sourceforge.net/projects/openfoam/files/v2006/OpenCFD-OpenFOAM4WindowsInstaller-v2006.exe/download) 


Option 2: Virtual Machine
---------------------------------------------------------------------
https://openfoam.org/download/windows-vm/


Option 3: blueCFD-core
---------------------------------------------------------------------
[bluecfd-github](http://bluecfd.github.io/Core/)
This is based on [MinGW](http://www.mingw.org/) which is a minimalistic Linux enviroment for Windows. So you have also Unix-Bash, where you execute commands.  
Unfortunately blueCFD is stuck to openFOAM 8, but it's worth to test if the WSL is not working.  



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
Now you can test the installation in the WSL or Linux system by starting: 

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
