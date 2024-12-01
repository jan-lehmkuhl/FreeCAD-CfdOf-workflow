Create Physics/CFDSolver Setup
======================================================================

The initialization of the `CFDAnalysis` container should already be done in the [mesh creation process](mesh.md#creating-the-cfd-freecad-container). 


Adapt CFD Setup
------------------------------------------------------------

Open the CFDAnalysis container, review the different settings and change the values if needed. 
Also you can change values in the properties windows. 

For a new setup you need to apply boundary condition for every face. 
The other values can be kept for the first try. 



export to case
------------------------------------------------------------

When the preprocessing is finished you export cfd settings. 
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



Check Success
------------------------------------------------------------

### Export Path
Check if the files are exported to the folder you expect. 

* delete the old `case`-folder
* [Write case setup](#export-to-case) again
* check if `case` is created where you expect


### Run
* [Now run the simulation](../solve-cfd-case.md) and check the success. 




RESOURCES
------------------------------------------------------------

[Chapter-4.1]:              https://cfd.direct/openfoam/user-guide/v7-case-file-structure/#x16-1220004.1
