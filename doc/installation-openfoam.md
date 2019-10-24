
A clean linux operating system can be applied on an USB-Stick. With some more work the installation should be also possible on every operating system. 


OpenFOAM Installation on Windows
===============================================================================

A Windows 10 installation should be possible with the builtin "Windows Subsystem for Linux" (WSL) in Windows 10 [Link](https://openfoam.org/download/windows-10/). Beside the WSL activation and the graphical output forwarding the installation should be similar to the Linux installation


OpenFOAM Installation on Linux
===============================================================================

This instructions refers to a Ubuntu 18.04 LTS installation and is described in [OpenFOAM Ubuntu instructions](https://openfoam.org/download/7-ubuntu/)  

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

