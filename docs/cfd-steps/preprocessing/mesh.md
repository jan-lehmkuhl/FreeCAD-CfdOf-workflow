Creating the Mesh Setup
======================================================================

After creating the [geometry](geometry.md) in FreeCAD, 
you switch to the CfdOF Workbench, to create the mesh settings. 



Creating the CFD-FreeCAD-Container
------------------------------------------------------------

When you starting from scratch, you need to create a `CFDAnalysis` container. 
After creation it is shown in the tree at the level of the geometry bodies. 



Creating the Mesh Setup
------------------------------------------------------------

This CFDAnalysis needs also a mesh. 
* mark the [Geometry/Body you prepared](geometry.md) and then execute "CFD mesh** from the toolbar

In the following popping up `Tasks` menu (the second register beside the model tree) you can change the basic values. 
* choose snappyHexMesh in the opening menu
* choose "Base element size" 6 times smaller than the finest geometry elements. 
* press "Search" button to specify a point inside your geometry


### change an existing Setup
To change the mesh settings doubleclick on `CFDAnalysis/Body001_Mesh`. 
Some values can also be changed in the properties menu below the model tree. 



export to meshCase
------------------------------------------------------------

When you finished your work, execute the `Write mesh case`-Button inside the FreeCAD-Tasks. 
These command writes text files to the subfolders `meshCase` into the directory specified in the CfdOF-Plugin-Settings. 



Check Success
------------------------------------------------------------
Now its time to execute and review your mesh. 


### Export Path
Check if the files are exported to the folder you expect. 

* delete the old `meshCase`-folder
* [Write mesh case](#export-to-meshcase) again
* check if `meshCase` is created where you expect


### Run & Review
Now you should try to execute this files with OpenFOAM to build and review the mesh. 
(See [docs/create-mesh](../calculate-mesh.md)).  
