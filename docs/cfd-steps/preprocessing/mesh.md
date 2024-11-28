# Mesh


Step 2: creating/modifying the mesh setup
------------------------------------------------------------

To do the CFD preprocessing switch to the CfdOF Workbench inside FreeCAD. 

#### init: creating the CFD-FreeCAD-Container
When you starting from scratch, you need to create the FreeCAD `CFDAnalysis` container which is shown in the tree at the level of and below `Body`: 
* mark the `geometry/Body` and then "**Create an analysis** container with a CFD solver" for this Body
* mark the `geometry/Body` and then "**Create a mesh** using snappyHexMesh for this Body

in this example this container are already there


#### change
To change the mesh settings doubleclick on `CFDAnalysis/Body001_Mesh`. 
In the following popping up `Tasks` menu (the second register beside the model tree) you can change the basic values. 
Some values can also be changed in the properties menu below the model tree. 


#### export to meshCase
When you finished your work, execute the `Write mesh case`-Button inside the FreeCAD-Tasks. 
These command writes text files to the subfolders `meshCase` into the directory specified in the CfdOF-Plugin-Settings. 

These files can be executed afterwards with OpenFOAM to build the mesh. 
See [docs/create-mesh](../calculate-mesh.md) for further details.  
