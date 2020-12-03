
<!-- one simulation-study report with the cfd related content -->



Task List
===============================================================================

- [ ] geometry 
    - [ ] import
    - [ ] simplification
- [ ] mesh
    - [ ] first mesh
    - [ ] good quality mesh
    - [ ] mesh study
    - [ ] final mesh refinement
- [ ] setup
    - [ ] set conditions
    - [ ] define monitor points
- [ ] analysis
    - [ ] first post-analysis
    - [ ] define default-analysis
    - [ ] convergence behaviour
    - [ ] final post-analysis
- [ ] geometry optimization
- [ ] write report


Reality Description
===============================================================================

Geometry
---------------------------------------------------------------------
<!-- description of the geometry features and their size -->
<!-- use real world pictures not simplified CAD data -->


Physics
---------------------------------------------------------------------
<!-- which physical effects occur -->
<!-- make sketches to describe special effects (you need less words) -->

| used materials    | used place    | density   | dyn. viscosity|
| ----------------- | ------------- | --------- | ------------- |
| material 1        |               | xx [kg/m³]| xx [kg/m/s]   |


| thermodynamic value   | occurring range   |
| --------------------- | ----------------- |
| pressure              | xxx [Pa] 
| velocities            | xxx [m/s]
| temperature           | xxx [C]



Model & Numerics
===============================================================================

Geometry
---------------------------------------------------------------------
<!-- simplifications of the 3D model -->
<!-- show pictures of the CAD model -->


Mesh
---------------------------------------------------------------------

### Final Mesh Metrics

| Mesh                      | Value     |
| ---------------------     | --------- |
| number of hexahedra:      | 0 
| number of prisms:         | 0 
| number of wedges:         | 0 
| number of pyramids:       | 0 
| number of tet wedges:     | 0 
| number of tetrahedra:     | 0 
| number of polyhedra:      | 0 
| max skewness              | XXX
| min y+ (runXXX)           | XXX 
| max y+ (runXXX)           | XXX 
<!-- not used mesh elements can be deleted -->


### Final Mesh Specific Features
<!-- show pictures of meshing from important geometry features -->


### Mesh Study
<!-- create mesh study and define error -->


Physical Modeling
---------------------------------------------------------------------
<!-- which special physical models are applied -->
<!-- e.g. bouyancy, energy transport, material models, ... -->

| Domain    | Setting               | Value             | checked       |
| --------- | --------------------- | ----------------- | ------------- |
| Fluid     | Buoyancy              | Non               |               |
| Inlet1    | Mass Flow / Vel       | XXX [m/s]         |               |
| Outlet1   | Pressure-BC           | 0 Pa              |               |


Numerics 
---------------------------------------------------------------------

| setting               | occuring range    |
| --------------------- | ----------------- |
| reference pressure    | xxx [Pa]
| turbulence model      | SST
| residual target       | 


Convergence
---------------------------------------------------------------------
<!-- show plots for all subtopics for at least the used runs in the postprocessing -->

### Global Residuals 

### Imbalances

### Yplus

### Monitor Point Stability


Analysis Type
---------------------------------------------------------------------
<!-- is this a transient simulation or indicate the residuals and monitor points a transient behaviour -->


Numerical Confidence
---------------------------------------------------------------------
<!-- how exact, do you think, are the calculation results -->



Flow Analysis 
===============================================================================
<!-- show expected behaviour to increase the confidence in the simulation -->
<!-- show special and interesting flow features to get more insights -->
<!-- describe for every picture what you see and you want to be seen by the reader  -->
<!-- what is your conclusion of the picture -->

<!-- ![](cfd-reports/XXX_001_Rep/Figure001.png)  -->



actual state conclusions
===============================================================================
<!-- what have you learned so far -->
