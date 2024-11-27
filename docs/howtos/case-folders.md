OpenFOAM Case Files & Folders
======================================================================

In general FreeCAD don't performs the CFD calculation. 
The FreeCAD-CFDOF-Plugin writes/exports the setup-data, which can be processed by OpenFOAM. 
For the mesh this data is written by default in the folder `meshCase` and for the cfd calculations this data is written in `case`. 

To make this example more robust the cfd-setup is already exported to these two folders. 
But if you want, you can delete them and recreate them from within FreeCAD. 
