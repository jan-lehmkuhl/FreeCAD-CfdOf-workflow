

FreeCAD Installation
==============================================================================

on Linux
---------------------------------------------------------------------
[FreeCAD installation wiki](https://www.freecadweb.org/wiki/Install_on_Unix)

add an apt-repository to tell Linux where he finds the latest version and get freecad 0.18.x

    sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
    sudo apt-get update

install freecad from packages 

    sudo apt-get install freecad freecad-doc
    sudo apt-get upgrade



FreeCAD Installation on Windows
---------------------------------------------------------------------
this should also work, but I haven't tested it.  
[Download](https://freecadweb.org/downloads.php)  



CfdOF installation
==============================================================================
The CfdOF-Plugin can be installed in the FreeCAD-GUI with the AddOn-Manager.  
Please follow OS dependent instructions from the [CfdOF Readme](https://github.com/jaheyns/CfdOF)  

### Plot Workbench
-> File -> Tools -> Addon-Manager  
-> Install "Plot" Workbench link  
Restart FreeCAD  

### CfdOF Workbench
previous Restart of FreeCAD is important  
-> File -> Tools -> Addon-Manager  
-> Install "CfdOF" Workbench link  
Restart FreeCAD againg  



CfdOF Settings
==============================================================================
File -> Edit -> Preferences -> CFD

## refer to openfoam
Set OpenFOAM directory to: 

    /opt/openfoam6   (or maybe openfoam7)

Click on `Run dependency checker` and look in the output if its telling you something about missing openfoam files.  
gmsh is not necessary. 


## Set Output directory 
It is important to know where CfdOF will write your files. If this is a constant folder like `/tmp` you will always copy the files from here to your project. Therefore set the output directory to a relative path from the path where you start freecad like `.`. For this example following should be used:  

    .

## HiSA & cfMesh
These are additional software but in case of an error they can be avoided in the preprocessing.  

File -> Edit -> Preferences -> CFD  

Press "Install cfMesh" button  
Press "Install HiSA" button  



FreeCAD customization
==============================================================================

remove unnecessary workbenches
------------------------------------------------------------------------------
https://www.freecadweb.org/wiki/Interface_Customization  
Menu -> Tools -> Customize  
![Screenshot from 2019-08-30 21-46-09.png](:/f7a07e203ff04c5299b947629913b7ac)  



Examples & Tutorials
==============================================================================

first 3D part
---------------------------------------------------------------------

[tutorial1](https://www.freecadweb.org/wiki/Creating_a_simple_part_with_PartDesign)  

* chose "Part Design Workbench"
* Tasks
    * create Body
    * create Sketch
* Save


Docs
---------------------------------------------------------------------

https://www.freecadweb.org/wiki/Tutorials
