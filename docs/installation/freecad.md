FreeCAD
==============================================================================

Installation on Windows
---------------------------------------------------------------------
1. Download FreeCAD from [freecadweb.org](https://www.freecadweb.org/downloads.php) or [wiki.freecad.org](https://wiki.freecad.org/Download)  
2. install the download or use a portable version of FreeCAD  
3. read [CfdOF-github](https://github.com/jaheyns/CfdOF) remarks and proceed the install of CfdOF Workbench with the FreeCAD Addon Manager described in the next chapter

If something is not working well, consider to download a [developer-version](https://github.com/FreeCAD/FreeCAD/releases/)  



Installation on Linux
---------------------------------------------------------------------
[FreeCAD installation wiki](https://www.freecadweb.org/wiki/Install_on_Unix)

This works also inside the Windows Subsystem for Linux, but is not necessary if your [FreeCAD Windows Installation](#installation-on-windows) is already running fine.  


### install from ppa
add an [apt-repository] to tell Linux where he finds the latest stable version of freecad: 

    sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
    sudo apt-get update

[apt-repository]: https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable


install freecad from packages 

    sudo apt-get install freecad
    sudo apt-get upgrade


### use daily builds
try [daily builds] when something went wrong  
https://wiki.freecadweb.org/Install_on_Unix#Daily_PPA_through_the_console  

    sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
    sudo apt-get update
    sudo apt-get install freecad-daily

[daily builds]: https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily



Examples & Tutorials
---------------------------------------------------------------------
### first 3D part

[tutorial1](https://www.freecadweb.org/wiki/Creating_a_simple_part_with_PartDesign)  

* chose "Part Design Workbench"
* Tasks
    * create Body
    * create Sketch
* Save




RESOURCES
======================================================================

[freecadweb.org - tutorials](https://www.freecadweb.org/wiki/Tutorials)  
