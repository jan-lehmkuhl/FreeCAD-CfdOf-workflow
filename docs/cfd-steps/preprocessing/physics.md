# Physics


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

[Chapter-4.1]:              https://cfd.direct/openfoam/user-guide/v7-case-file-structure/#x16-1220004.1
