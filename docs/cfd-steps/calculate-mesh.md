Create Mesh with OpenFOAM
======================================================================

After [exporting the mesh-setup](./preprocessing-with-freecad.md#step-2-creatingmodifying-the-mesh-setup) from FreeCAD to [`meshCase`](../howtos/case-folders.md) or using the default files in this repository 
you can calculate the mesh from the terminal.  

    cd example-wf
    make mesh


If you need to do more debugging and get a better understanding use: 

    cd meshCase
    ./Allmesh



Check success
------------------------------------------------------------

Before proceeding with your [CFD calculation steps](README.md) you have to ensure your mesh is like you intended. 

Review the file [`meshCase/Allmesh`](../../meshCase/Allmesh) for detailed information of the meshing process and read from the OpenFOAM-documentation the [OpenFOAM-User-Guide]. 
[Chapter-5] covers the meshing process.  


### Files
Beside other mesh files in `meshCase/constant/polyMesh` the file `/points` should be created and hold a lot of points starting with:  
~~~c
/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  11
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       vectorField;
    location    "constant/polyMesh";
    object      points;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


5070
(
(-0.0149083645198597 0.127307961058098 -0.374999970197678)
(-0.00457262334461692 0.12523419947695 -0.374999970197678)
(0.0045726255418188 0.125234199684642 -0.374999970197678)
(0.0149083659988574 0.12730796143784 -0.374999970197678)
(-0.0257948828526149 0.132235872650146 -0.375)
(-0.0149924533599494 0.134891927642467 -0.374999989124785)
(-0.00494433333059355 0.134850183691428 -0.374999986583457)
(0.00494433433183149 0.134850183887776 -0.374999984151432)
(0.0149924537769227 0.134891928328992 -0.374999981902291)
...
~~~


### Review the mesh in 3D

Afterwards you should review the created mesh within the 3D viewer [Paraview](./postprocessing-with-paraview.md). 
At Windows start from the Search and in Linux execute: 

    make view-mesh




RESOURCES
------------------------------------------------------------

[OpenFOAM-User-Guide]:      https://cfd.direct/openfoam/user-guide/  
[Chapter-5]:                https://cfd.direct/openfoam/user-guide/v7-mesh/#x23-1670005  
