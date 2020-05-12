
OpenFOAM Installation on Windows
===============================================================================
[openfoam.org/download/windows](https://openfoam.org/download/windows/)  
OpenFOAM is a Linux Programm but there are several ways to run it under Windows.  
In general it is not necessary for OpenFOAM to have a graphical user interface. OpenFOAM reads text files and writes the output to text files. So if you have access to these files, you can run your GUI-Programs like FreeCAD and Paraview nativly under Windows


Option 1: Windows Subsystem for Linux" (WSL)
---------------------------------------------------------------------
A [Windows-10-installation] should be possible with the builtin "Windows Subsystem for Linux" (WSL) in Windows 10. Beside the [WSL-activation] and the graphical-output-forwarding with [Xming] the installation should be very similar to the Linux installation described in this file in the next chapter.  

### Installation
1. read: [openfoam.org-help](https://openfoam.org/download/windows-10/)
2. Activate Windows Subsystem for Linux (WSL) like described in [WSL-activation] and 
    install your desired Distro from `Microsoft Store` within Windows 10.  
    At the end you have a terminal with Linux (WSL) running. 
3. Install OpenFOAM inside WSL described in the Linux-Installation-Chapter below  


### hard disc access
The hard-disks (e.g. `C:`, `D:`) are mounted in the WSL at `/mnt/c` and `/mnt/d`. To access these data change your directory (`cd`) to these folders:

    cd /mnt/c/YOURDIRECTORY


### Graphical output forwarding
[Xming] helps to present the Linux graphical output as Window under Windows. 
Download and install Xming from [Sourceforge](https://sourceforge.net/projects/xming/)  
After installing Xming should run in the windows tray. Then tell your WSL to output to a Display:

    export DISPLAY=:0.0

Afterwards you can start a GUI program.  

When you get an error message similar like following, your Linux don't find a place where to put the graphical output: 

    (gedit:1243): Gtk-WARNING **: 16:29:10.075: cannot open display: :0

If this don't work everything in Linux can be done without an grafical output.
Instead of using the graphical text editor `gedit` to change files, you can use terminal text editors like `nano` . In Nano you can save the file with `Ctrl+s` and end the session with `Ctrl+x`. 


[Windows-10-installation]: https://openfoam.org/download/windows-10/  
[WSL-activation]: https://docs.microsoft.com/en-gb/windows/wsl/install-win10  
[Xming]: https://de.wikipedia.org/wiki/Xming  


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

This instructions refers to a Ubuntu 18.04 LTS installation and is described in [OpenFOAM Ubuntu instructions](https://openfoam.org/download/7-ubuntu/)  
A clean linux operating system can be applied on an USB-Stick, without major performance issues.  

Further resources:  
[OpenFOAM Linux Guide](https://cfd.direct/openfoam/linux-guide/)  
[OpenFOAM Downloads](https://cfd.direct/openfoam/download/)  
[OpenFOAM.org source files](https://github.com/OpenFOAM/OpenFOAM-7)  


Package installation 
---------------------------------------------------------------------
First you have to add a online-repository and tell Ubuntu where he find additional software

    sudo sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
    sudo add-apt-repository http://dl.openfoam.org/ubuntu
    sudo apt-get update

then you can install with following command. Linux will download the needed files from the previous defined repository. 

    sudo apt-get -y install openfoam7


change .bashrc
---------------------------------------------------------------------
after installation Ubuntu should know where he finds the OpenFOAM binaries, so that you can call them from the terminal. 

    nano .bashrc

paste in the `.bashrc` textfile following line: 

    source /opt/openfoam7/etc/bashrc


testing
---------------------------------------------------------------------
Now you can test the installation by starting 

    simpleFoam

because there are no case-files there will be errors but you see an header like this:  

    user@machine:~/simulations$ simpleFoam 
    /*---------------------------------------------------------------------------*\
      =========                 |
      \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
       \\    /   O peration     | Website:  https://openfoam.org
        \\  /    A nd           | Version:  6
         \\/     M anipulation  |
    \*---------------------------------------------------------------------------*/


also you should be able to open `paraview` or `paraFoam` and the GUI should open, when you setup correctly the graphical forwarding

    paraview

