

**CFD-Project**
************************************************  
|                   |                                  |
| ----------------- | -------------------------------- |
| **Project Title** | xxx
| project start     | xxx.2018
| project end       | ongoing
| active stakeholder| xxx
| cfd engineer      | Jan Lehmkuhl
| design engineer   | xxx
| checked by        | xxx
<br>  

<!-- example picture for quick project identification -->
![](doc/images/XXX.png) 



Management-Summary
===============================================================================

Background
---------------------------------------------------------------------
<!-- 
* which information is needed to understand the project goals
* this should be understand by every friend or manager
 -->


Goals
---------------------------------------------------------------------
<!-- 
* which goal should be reached within this project
  * maximum 400 characters
  * bulletpoints with max 10 words
  * more explanations belong to the background
* more than one goal should be avoided
  * multiple goals are complex to reach 
* goals are about knowledge to achieve
  * e.g. optimize the flow in something, understand the physics from something
  * this is not about simulations
    * simulations are the howto-tools to reach your goals and 
    * simulations are explained later in the report
 -->


Major Work Packages
---------------------------------------------------------------------
<!-- 
* maximum 700 characters
    * detailed explanations later
* which simulations are/will be used to achieve your goals
* which special information should each study (group of similar simulations) deliver to reach the project goals
* which numbers are calculated in the postprocessing
 -->


Issues which jeopardize the project 
---------------------------------------------------------------------
<!-- 
* where are not yet solved issues or problems which can threaten the project outcome
* e.g. numerics in study 1 are bad, you don't know yet to apply special model features, ...
 -->


Results
---------------------------------------------------------------------
<!-- 
* which goals or partial goals are reached at this moment
* can be devided in parts for every study
 -->


Project-Forecast
---------------------------------------------------------------------
<!-- 
* next steps and timeframe
* whats your plan for the next week
 -->



Available Resources
===============================================================================

Timeframe
---------------------------------------------------------------------
<!-- 
* deadlines
* dependent projects
* necessary completed projects
 -->


Human Resources
---------------------------------------------------------------------
<!-- 
* full time project? 
* estimated hours per week
 -->


Calculation Enviroment
---------------------------------------------------------------------
<!-- 
* Short description of the hard- and software used to create the analysis. 
* The objective of this section is: 
  * to ensure reproducible results for the case of later reruns 
  * to be aware of the possible simulations delivered in a specified time 
 -->

### Hardware
<!-- 
|          |                                                                                        |
| -------- | ------------------------------------------------------------------ |
| Machine  | 
| System   | Host: <br> Kernel: <br> Distro:  <br> Desktop: 
| CPU      | COUNT x Name <br> Cache:  <br> Max. clock speed: XXXX MHz 
| Memory   | Manufacturer: <br> Type: <br>  Speed: XXXX MHz <br> Size: XX x XX GB 
| Graphics | Card: <br> Display Server: <br> Driver: 
 -->


### Software
<!-- 
| Task              | Programm                                          |
| ----------------- | ------------------------------------------------- |
| CAD               | 
| stl               | 
| background mesh   | OpenFoam X.x
| mesh              | OpenFoam X.x
| solver            | OpenFoam X.x
| paraview          | paraview X.X.X 
| R version         | X.X.X (20xx-xx-xx)
 -->



Simulation Study 1
===============================================================================
<!-- 
* collection of simulations which share similar geometry and settings
* together these simulation study leads to specific conclusions
* e.g. test of geometry changes
* a second study might be a simulation to determine specific boundary conditions for a first study
* describe which conclusions will be desirable from each study
 -->


Reality Description
---------------------------------------------------------------------

### Geometry
<!-- 
* description of the geometry features and their size
* use real world pictures not simplified CAD data
 -->


### Physics
<!-- 
* which physical effects occur
* make sketches to describe special effects (you need less words)

| used materials    | used place    | density   | dyn. viscosity|
| ----------------- | ------------- | --------- | ------------- |
| material 1        |               | xx [kg/m³]| xx [kg/m/s]   |


| thermodynamic value   | occurring range   |
| --------------------- | ----------------- |
| pressure              | xxx [Pa] 
| velocities            | xxx [m/s]
| temperature           | xxx [C]

 -->


Model & Numerics
---------------------------------------------------------------------

### Geometry
<!-- 
* simplifications of the 3D model
* show pictures of the CAD model
 -->


### Mesh
<!-- 
* description of the general meshing approach
 -->

#### Mesh Study
<!-- 
* create mesh study and define error 
* use values of interest from Flow Analysis part
-->

#### Final Mesh Metrics
<!-- 
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
 -->
<!-- not used mesh elements can be deleted -->

#### Final Mesh Specific Features
<!-- 
* show pictures of meshing from important geometry features
* is there a specific fokus (mesh refinements at place X)
* are special features applied (boundary layers, ...)
 -->


### Physical Modeling
<!-- 
* which special physical models are applied
* e.g. bouyancy, energy transport, material models, ...

| Domain    | Setting               | Value             | checked       |
| --------- | --------------------- | ----------------- | ------------- |
| Fluid     | Buoyancy              | Non               |               |
| Inlet1    | Mass Flow / Vel       | XXX [m/s]         |               |
| Outlet1   | Pressure-BC           | 0 Pa              |               |
 -->


### Numerics 
<!-- 
| setting               | occuring range    |
| --------------------- | ----------------- |
| reference pressure    | xxx [Pa]
| turbulence model      | SST
| residual target       | 
 -->


### Convergence
<!-- 
* show plots for all subtopics for at least the used runs in the postprocessing
 -->

#### Global Residuals 

#### Imbalances

#### Yplus
<!-- only on relevant faces -->

#### Monitor Point Stability


### Analysis Type
<!-- 
* is this a transient simulation or indicate the residuals and monitor points a transient behaviour
 -->


### Numerical Confidence
<!-- 
* how exact, do you think, are the calculation results
* how big are the changes in the result, when you change the setup
 -->



Flow Analysis 
---------------------------------------------------------------------
<!-- 
* show expected behaviour to increase the confidence in the simulation
* show special and interesting flow features to get more insights
* describe for every picture what you see and you want to be seen by the reader 
* what is your conclusion of the picture
* break the results down to single numbers, e.g.: 
    * (average) velocities (at specific points of interest)
    * pressure values
* this should be the biggest part in this report

![](cfd-reports/XXX_001_Rep/Figure001.png) 
 -->


actual study conclusions
---------------------------------------------------------------------
<!-- 
* what have you learned so far in this study 
* the overall conclusions should be placed in "Results" in the Management Summary
 -->
