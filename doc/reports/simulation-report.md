
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

Physics
---------------------------------------------------------------------
<!-- which physical effects occur -->

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
<!-- simplifications of the 3D modell -->


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
### Global Residuals 

### Imbalances

### Yplus

### Monitor Point Stability


Analysis Type
---------------------------------------------------------------------
<!-- is this a transient simulation or indicate the residuals a transient behaviour -->


Numerical Confidence
---------------------------------------------------------------------
<!-- how exact do you expect the calculation results -->



Flow Analysis 
===============================================================================
<!-- show expected behaviour to increase the confidence in the simulation -->
<!-- show special and interesting flow features to get more insights -->

<!-- ![](cfd-reports/XXX_001_Rep/Figure001.png)  -->



actual state conclusions
===============================================================================
<!-- what have you learned so far -->
