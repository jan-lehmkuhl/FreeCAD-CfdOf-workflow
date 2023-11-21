Preprocessing Steps in FreeCAD
======================================================================

When you start to build the cfd calculation for your project you have to perform following steps. 
I recommend to start with a new empty case, to be aware of all your changes. 



Step 1: creating/modifying a geometry
------------------------------------------------------------

Normally you start with an empty file or get some basic CAD files from your construction departement. 
Keep in mind: You do not model the pipe, **you model the volume inside the pipe**. 

This [FreeCAD-Tutorial] is a good start to get used to FreeCAD for creating 3D Models.  


Now open FreeCAD. 
At Windows use your "Windows Search"
At a native Linux you can open FreeCAD with `freecad freecad-cfd.FCStd` or `make open-freecad` and loading directly the already prepared data in the linked freecad-file. 

    freecad freecad-cfd.FCStd


On the left side in the model tree all content in this file is listed.  
![](docs/resources/freecad-combo-view.png)  
To toggle the visibility of specific entries you can mark some and hit the space bar. 
To getting to know each entry make all entries invisible (greyed out) and test what is appearing when you switch it to visible again. 



Step 2: creating/modifying the mesh setup
------------------------------------------------------------

To do the CFD preprocessing switch to the CfdOF Workbench inside FreeCAD. 

#### init: creating the CFD-FreeCAD-Container
When you starting from scratch, you need to create the FreeCAD `CFDAnalysis` container which is shown in the tree at the level of and below `Body`: 
* mark the `geometry/Body` and then "**Create an analysis** container with a CFD solver" for this Body
* mark the `geometry/Body` and then "**Create a mesh** using cfMesh, snappyHexMesh or gmsh" for this Body

in this example this container are already there

#### change
To change the mesh settings doubleclick on `CFDAnalysis/Body001_Mesh`. 
In the following popping up `Tasks` menu (the second register beside the model tree) you can change the basic values. 
Some values can also be changed in the properties menu below the model tree. 

#### export to meshCase
When you finished your work, execute the `Write mesh case`-Button inside the FreeCAD-Tasks. 
These command writes text files to the subfolders `meshCase` into the directory specified in the CfdOF-Plugin-Settings. 

These files can be executed afterwards with OpenFOAM to build the mesh. 
See [docs/create-mesh](create-mesh.md) for further details.  




Step 3: creating/modifying the cfd setup
------------------------------------------------------------

The initialization was already done by the mesh creation process. 

Therefore you can doubleclick on the different settings and change the values if needed. 
Also you can change values in the properties windows. 
If not existing, for every Face has a boundary condition to be applied. 

#### export to case
When the preprocessing is finished you export the mesh and cfd settings. 
Doublecklick on `CFDAnalysis/CfdSolver` and execute the `Write`-Button inside the FreeCAD-Tasks

These commands will write text files to the subfolder `case` into the directory specified in the CfdOF-Plugin-Settings, similar to `meshCase`. 
Then you should explore folder structure in `case`.  
Before calculation starts three folders exists:  
~~~bash
├── case
│   ├── 0
│   ├── constant
│   └── system
~~~
the file structure is documented in [Chapter-4.1] from the User Guide.




RESOURCES
------------------------------------------------------------

[FreeCAD-Tutorial]:         https://www.freecadweb.org/wiki/Creating_a_simple_part_with_PartDesign 
[Chapter-4.1]:              https://cfd.direct/openfoam/user-guide/v7-case-file-structure/#x16-1220004.1
