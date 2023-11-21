Solve CFD case
======================================================================

If the [mesh is created](create-mesh.md) successfully the CFD solving process can start. 
Then the [setup must be exported](preprocessing-steps.md#export-to-case) to `case` and
you can start the calculation in WSL or Linux with: 

    make run

or using the exported `Allrun` for debugging:  

    cd case
    ./Allrun




### test success
If the calculation runs, there is a lot of terminal output. 
At the end there shoud be a success message like: 

    GAMG:  Solving for p, Initial residual = 1.2947568e-08, Final residual = 1.8387204e-09, No Iterations 1
    time step continuity errors : sum local = 1.1281226e-08, global = 3.6351064e-09, cumulative = -5.0078224e-06
    smoothSolver:  Solving for omega, Initial residual = 9.7324543e-06, Final residual = 5.9005793e-07, No Iterations 3
    smoothSolver:  Solving for k, Initial residual = 8.9986853e-05, Final residual = 5.6533897e-06, No Iterations 3
    ExecutionTime = 3.16 s  ClockTime = 3 s


    SIMPLE solution converged in 106 iterations

    End

    Finalising parallel run


In the folder `case/processor0/100` or `case/100` you find for the timestep `100` files with the values for pressure (`p`) or velocities (`U`). 

Afterwards use [Paraview](paraview-usage.md) for the detailed postprocessing. 




RESOURCES
------------------------------------------------------------

For a detailed review of the calculation process and read from the [OpenFOAM-documentation] the [OpenFOAM-User-Guide]. 

[OpenFOAM-documentation]:   https://cfd.direct/openfoam/documentation/  
[OpenFOAM-User-Guide]:      https://cfd.direct/openfoam/user-guide/  
