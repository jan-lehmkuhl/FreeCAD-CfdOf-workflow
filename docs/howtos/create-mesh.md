Create Mesh with OpenFOAM
======================================================================

After [exporting the mesh-setup](preprocessing-steps.md#step-2-creatingmodifying-the-mesh-setup) from FreeCAD to [`meshCase`](case-folders.md) or using the default files in this repository 
you can calculate the mesh from the terminal.  

    cd example-wf
    make mesh


If you need to do more debugging and get a better understanding use: 

    cd meshCase
    ./Allmesh



## test success
these commands should create a lot terminal output with the final lines:

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
    Reading surf from "mesh_outside.stl" ...
    Writing surf to "mesh_outside.stl" ...
    Scaling points by (1000 1000 1000)
    End

Beside others the file `meshCase/constant/polyMesh/points` should be created and hold a lot of points. 


## review the meshing process & the mesh
Review the file `meshCase/Allmesh` for detailed information of the meshing process and read from the [OpenFOAM-documentation] the [OpenFOAM-User-Guide]. 
[Chapter-5] covers the meshing process.  

Then you should have a look in the created files, to get a feeling of the process. 
They are in the folder `meshCase/constant/polyMesh` and especially in the file `points`. 

Afterwards you should review the created mesh within the 3D viewer [Paraview](paraview-usage.md). 
At Windows start from the Search and in Linux execute: 

    make view-mesh



RESOURCES
------------------------------------------------------------

[Chapter-5]:                https://cfd.direct/openfoam/user-guide/v7-mesh/#x23-1670005  
