Residuals
======================================================================

Residuals are the most popular monitor points and give you a first guess of your numerical errors. 
Residuals are the deviation for different variables (mass, velocity, pressure, etc.) between numerical iteration loops. 
If they are low the calculation is no longer changing during the calculation progress. 



OpenFOAM Setup
------------------------------------------------------------

Per default the residuals are not plotted. 
Therefore you have to tell OpenFOAM explicit to write them to the `case`-Folder. 
To do so insert following lines in `./system/controlDict` inside the `case` folder: 
~~~
functions
{
    #includeFunc residuals 
};
~~~

To integrate more variables to the residual output, use the function `foamGet` to place an additional file in your `system` folder, which tells OpenFOAM to write the residuals.  

    cd case
    foamGet residuals

This copies the default `residuals` file to the `system` folder in `case`. 
The same results can be achieved by using following: 

    cd case
    cp /opt/openfoam7/etc/caseDicts/postProcessing/numerical/residuals  ./system

Now you can place extra variables in the `residuals` file, to track more variables like `k` and `omega`. 
For this purpose add these variables behind `U` in following line: 
~~~
fields (p U k omega);
~~~



Check Success and Review
------------------------------------------------------------

### view residuals on file level
When you start again your calculation, you can see an additional folder `./postProcessing/residuals/0/` with the `residuals*.dat` in plain text inside. 
Every line displays the residuals of a specific time step for a specific variable. 
~~~
# Residuals     
# Time          	p               	Ux              	Uy              	Uz
1               	1.00000000e+00	3.64764311e-01	4.02177205e-02	4.47276887e-02
2               	5.34931089e-01	2.71486281e-01	1.35722759e-02	1.40211659e-02
3               	2.81635512e-01	2.40206271e-01	1.34506585e-02	1.76641824e-02
~~~


### foammonitor
to get an nice picture you can use the `foamMonitor`, which plots within the Linux environment a picture. 
As option you have to specify the residuals-file. 

    foamMonitor -l FILE

https://cfd.direct/openfoam/user-guide/v7-graphs-monitoring/


### Using the Example-WF
A plot should also be created in `case/visualization/plots` after `make post`. 
(see [installation/python](../../installation/python.md))  




RESOURCES
======================================================================

Please refer to:  
https://cfd.direct/openfoam/user-guide/v7-post-processing-cli  
https://cfd.direct/openfoam/user-guide/v7-graphs-monitoring/  
