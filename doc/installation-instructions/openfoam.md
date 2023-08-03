
OpenFOAM Installation on Windows
===============================================================================
[openfoam.org/download/windows](https://openfoam.org/download/windows/)  
OpenFOAM is a Linux Programm but there are several ways to run it under Windows.  
In general it is not necessary for OpenFOAM to have a graphical user interface. 
OpenFOAM reads text files and writes the output to text files. 
So if you have access to these files, you can run your GUI-Programs like FreeCAD and Paraview nativly under Windows. 

Beside installing OpenFOAM in a System like WSL or Docker, FreeCAD needs also a [OpenFOAM Windows installation](freecad-cfdof.md#install-cfdof-dependencies) to have access to some template files.  



Option 1: Windows Subsystem for Linux" (WSL)
---------------------------------------------------------------------
A [Windows-10-installation] should be possible with the builtin "Windows Subsystem for Linux" (WSL) in Windows 10. 
Beside the [WSL-activation] the installation should be very similar to the Linux installation described in the [next chapter](#openfoam-installation-on-linux).  


### Installation
1. read: [openfoam.org-help](https://openfoam.org/download/windows-10/)
2. Activate Windows Subsystem for Linux (WSL) like described in [WSL-activation]  
   you need Administrator rights in the Powershell to execute.  
3. install your desired Distro from `Microsoft Store` within Windows 10.  
   At the end you have a terminal with Linux (WSL) running. 
4. Install OpenFOAM inside WSL described in the Linux-Installation-Chapter below  

[Windows-10-installation]: https://openfoam.org/download/windows-10/  
[WSL-activation]: https://docs.microsoft.com/en-gb/windows/wsl/install-win10  


### hard disc access
The hard-disks (e.g. `C:`, `D:`) are mounted in the WSL at `/mnt/c` and `/mnt/d`. 
To access these data change your directory (`cd`) to these folders:

    cd /mnt/c/YOURDIRECTORY


### Graphical output forwarding
[VcXsrv] or [Xming] helping to present the Linux graphical output as Window under Windows. 
This is not necessary but might be nice. 

[VcXsrv]: https://sourceforge.net/projects/vcxsrv/
[Xming]:  https://de.wikipedia.org/wiki/Xming  



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
Unfortunately blueCFD is stuck to openFOAM 5, but it's worth to test if the WSL is not working.  



OpenFOAM Installation on Linux
===============================================================================

This instructions refers to a Ubuntu 20.04 LTS installation and is described in [OpenFOAM Ubuntu instructions](https://openfoam.org/download/)  
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


change .bashrc
---------------------------------------------------------------------
after installation Ubuntu should know where he finds the OpenFOAM binaries, so that you can call them from the terminal.  
open a texteditor with: 

    nano ~/.bashrc
    or
    code ~/.bashrc

paste in the `.bashrc` textfile following line: 

~~~bash
source /opt/openfoam11/etc/bashrc
~~~


testing
---------------------------------------------------------------------
Now you can test the installation in the WSL or Linux system by starting: 

    simpleFoam

because there are no case-files, where you run `simpleFoam`, there will be errors but you see an header like this:  

~~~
user@machine:~/simulations$ simpleFoam 
/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  11
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
~~~

also you should be able to execute `paraview` or `paraFoam` and a GUI should open, when you setup correctly the graphical forwarding

    paraview
    paraFoam

Now you can try to run the main example described in the [README](../../README.md) in the root folder of this repository. 
