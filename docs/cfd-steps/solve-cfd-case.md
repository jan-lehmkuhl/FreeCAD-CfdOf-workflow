Solve CFD case
======================================================================

If the [mesh is created](./calculate-mesh.md#check-success) successfully and 
the [cfd setup is exported](../cfd-steps/preprocessing/physics.md#export-to-case) to `case` and
you can start the calculation in WSL or Linux with: 

    make run

or using the exported `Allrun` for debugging:  

    cd case
    ./Allrun



Check Success
------------------------------------------------------------

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



### Terminal Output
If the calculation runs, there is a lot of terminal output like this:

~~~
Time = 104s

smoothSolver:  Solving for Ux, Initial residual = 4.74397840586177e-05, Final residual = 1.69050786710185e-06, No Iterations 1
smoothSolver:  Solving for Uy, Initial residual = 4.91532863986918e-06, Final residual = 2.06608592366315e-07, No Iterations 1
smoothSolver:  Solving for Uz, Initial residual = 1.31535485403069e-05, Final residual = 4.61323669256354e-07, No Iterations 1
GAMG:  Solving for p, Initial residual = 7.92658735485572e-05, Final residual = 7.88171574621083e-07, No Iterations 3
GAMG:  Solving for p, Initial residual = 5.27565498244524e-06, Final residual = 3.74618970721262e-08, No Iterations 5
GAMG:  Solving for p, Initial residual = 8.94237284801001e-07, Final residual = 7.94535403998561e-09, No Iterations 3
GAMG:  Solving for p, Initial residual = 1.98069772417531e-07, Final residual = 7.33365922014476e-09, No Iterations 1
GAMG:  Solving for p, Initial residual = 4.91520434506713e-08, Final residual = 3.49142778205117e-09, No Iterations 1
GAMG:  Solving for p, Initial residual = 1.36412472584184e-08, Final residual = 1.91547477719885e-09, No Iterations 1
time step continuity errors : sum local = 1.18168119044078e-08, global = 3.94524658101648e-09, cumulative = -8.2389760377603e-06
smoothSolver:  Solving for omega, Initial residual = 1.17170467937857e-05, Final residual = 7.17881163275539e-07, No Iterations 3
smoothSolver:  Solving for k, Initial residual = 0.000114718142147407, Final residual = 7.30263923125205e-06, No Iterations 3
ExecutionTime = 0.882937 s  ClockTime = 0 s

Time = 105s

smoothSolver:  Solving for Ux, Initial residual = 4.20339287251659e-05, Final residual = 1.53099910192529e-06, No Iterations 1
smoothSolver:  Solving for Uy, Initial residual = 4.33533932384135e-06, Final residual = 1.80942776290254e-07, No Iterations 1
smoothSolver:  Solving for Uz, Initial residual = 1.13613731228462e-05, Final residual = 3.95289674438012e-07, No Iterations 1
GAMG:  Solving for p, Initial residual = 7.24109233078376e-05, Final residual = 6.96745196694777e-07, No Iterations 3
GAMG:  Solving for p, Initial residual = 4.95537140722397e-06, Final residual = 3.10888901153037e-08, No Iterations 5
GAMG:  Solving for p, Initial residual = 8.47742987887319e-07, Final residual = 6.98565642454994e-09, No Iterations 3
GAMG:  Solving for p, Initial residual = 1.90608745703839e-07, Final residual = 6.930968542648e-09, No Iterations 1
GAMG:  Solving for p, Initial residual = 4.78718800670098e-08, Final residual = 3.30977241938437e-09, No Iterations 1
GAMG:  Solving for p, Initial residual = 1.32188901084151e-08, Final residual = 1.79077799691402e-09, No Iterations 1
time step continuity errors : sum local = 1.10471471465244e-08, global = 3.82170953760943e-09, cumulative = -8.23515432822269e-06
smoothSolver:  Solving for omega, Initial residual = 1.02681162435102e-05, Final residual = 6.23469624818677e-07, No Iterations 3
smoothSolver:  Solving for k, Initial residual = 9.99640850345639e-05, Final residual = 6.32345263217828e-06, No Iterations 3
ExecutionTime = 0.889866 s  ClockTime = 0 s


SIMPLE solution converged in 105 iterations

End

Finalising parallel run
~~~

#### Executing Iterations
If you see multiple timesteps (`Time = XXXs`) OpenFOAM tries to solve the cfd setup in multiple iterations or timesteps.  
This means the process works

#### Convergence
If you see at the end message like: `solution converged in X iterations` the simulation met the convergence criteria and stopped as intended. 
If not you have to search for problems in your mesh or physical setup. 
(See [troubleshooting/convergence-problems](../troubleshooting/convergence-problems.md))  



### Review Monitor Points & Residuals
see: 
* [postprocessing/residuals](postprocessing/residuals.md)  
* [postprocessing/probes](postprocessing/probes.md)



### Review 3D data with Paraview
To analyze this data in a more convenient graphical way you should use Paraview. 
The details are described in this [HowTo](postprocessing/3d-data-with-paraview.md). 




RESOURCES
------------------------------------------------------------

For a detailed review of the calculation process and read from the [OpenFOAM-documentation] the [OpenFOAM-User-Guide]. 

[OpenFOAM-documentation]:   https://cfd.direct/openfoam/documentation/  
[OpenFOAM-User-Guide]:      https://cfd.direct/openfoam/user-guide/  
