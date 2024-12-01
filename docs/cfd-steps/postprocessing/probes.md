---
id: 49febff1-e31b-4be9-aa2a-23bc26c9e69a
created: 2024-12-01 13:15
keywords: 
  - #permanent-note
---


Probes (or Monitor Points)
======================================================================

Setup in OpenFOAM
------------------------------------------------------------

To insert probes on special positions you proceed like the [residuals](residuals.md). 
Add following to `./system/controlDict`: 

~~~Cpp
functions
{
    #includeFunc  probes
}
~~~

add the `probes` file 

    foamGet probes

and modify the location in the `probes` file. 
The position is set for x,y,z-coordinate in the unit [m].  

~~~Cpp
fields (p U);
points
(
    (0 0 0)
    (0 1.0 0)
);
~~~



Check Success
------------------------------------------------------------

see [residuals](residuals.md#check-success-and-review)  





RESOURCES
======================================================================
