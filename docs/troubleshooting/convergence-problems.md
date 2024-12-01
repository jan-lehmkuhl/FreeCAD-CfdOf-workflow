---
id: 3f31e8e9-b57a-4607-bea0-e16b1b66d7ea
created: 2024-12-01 12:21
keywords: 
  - #permanent-note
---


Troubleshooting Convergence Problems
======================================================================

If your simulation is [running but not converging](../cfd-steps/solve-cfd-case.md#convergence), you have to look deaper in your mesh and physical setup. 
This means you have to do more postprocessing. 

* First look at the [residuals](../cfd-steps/postprocessing/residuals.md)  
    * are the first steps looking good
    * when is the simulation starting to crash
* Then look at the [monitor points](../cfd-steps/postprocessing/probes.md)
    * what do you expect and what do you see? 
* Then [postprocessing with Paraview](../cfd-steps/postprocessing/paraview.open-3d-data.md). 
    * Start with early timesteps. Here is the chance bigger that the simulation is not yet completly fucked up. 
      For this set "CFDSolver/Steady Write Intervall" to `1`. Then you can look in the first iteration results. 


Problems might be: 
* bad mesh cells
* boundary conditions, which might not fit to the problem
* ... (a lot more stuff)




RESOURCES
======================================================================
