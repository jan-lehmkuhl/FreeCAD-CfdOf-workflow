
OpenFOAM Installation on Windows
===============================================================================
[openfoam.org/download/windows](https://openfoam.org/download/windows/)

Option 1: Windows Subsystem for Linux" (WSL)
---------------------------------------------------------------------
A [Windows-10-installation] should be possible with the builtin "Windows Subsystem for Linux" (WSL) in Windows 10. Beside the [WSL-activation] and the graphical-output-forwarding with [Xming] the installation should be similar to the Linux installation.  
The hard-disks (e.g. C:) are mounted in the WSL at `/mnt/c`

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

then you can install

    sudo apt-get -y install openfoam7


change .bashrc
---------------------------------------------------------------------
after installation Ubuntu should know where he finds the OpenFOAM binaries. 

    gedit .bashrc

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


also you should be able to open `paraview` or `paraFoam` and the GUI should open

    paraview

