Solve CFD case
======================================================================

If the [mesh is created](./calculate-mesh.md) successfully the CFD solving process can start. 
Then the [setup must be exported](../howtos/preprocessing-steps.md#export-to-case) to `case` and
you can start the calculation in WSL or Linux with: 

    make run

or using the exported `Allrun` for debugging:  

    cd case
    ./Allrun


Check Success
------------------------------------------------------------

### Terminal Output
If the calculation runs, there is a lot of terminal output. 
At the end there shoud be a success message like: 

~~~
GAMG:  Solving for p, Initial residual = 1.2947568e-08, Final residual = 1.8387204e-09, No Iterations 1
time step continuity errors : sum local = 1.1281226e-08, global = 3.6351064e-09, cumulative = -5.0078224e-06
smoothSolver:  Solving for omega, Initial residual = 9.7324543e-06, Final residual = 5.9005793e-07, No Iterations 3
smoothSolver:  Solving for k, Initial residual = 8.9986853e-05, Final residual = 5.6533897e-06, No Iterations 3
ExecutionTime = 3.16 s  ClockTime = 3 s


SIMPLE solution converged in 106 iterations

End

Finalising parallel run
~~~


### File Data
After the calculation you should see numerical values in files like [`case/processor0/100/U`](case/processor0/100/U), 
which is the data for the velocity in the 100 iteration.  

~~~c++
dimensions      [0 1 -1 0 0 0 0];

internalField   nonuniform List<vector> 
2275
(
(-0.0041313212 0.021062818 -3.0098098)
(0.043862117 -0.15867647 -3.2610956)
(0.013769403 0.10046274 -2.9954474)
(0.056011809 -0.089816178 -3.221244)
(-0.097244635 0.076614349 -3.2684462)
(0.034121441 0.1890505 -2.9816516)

...
~~~


### Review 3D data with Paraview
To analyze this data in a more convenient graphical way you should use Paraview. 
The details are described in this [HowTo](postprocessing-with-paraview.md). 

At best






RESOURCES
------------------------------------------------------------

For a detailed review of the calculation process and read from the [OpenFOAM-documentation] the [OpenFOAM-User-Guide]. 

[OpenFOAM-documentation]:   https://cfd.direct/openfoam/documentation/  
[OpenFOAM-User-Guide]:      https://cfd.direct/openfoam/user-guide/  
