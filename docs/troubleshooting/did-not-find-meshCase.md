Did not find "
======================================================================


FreeCAD at Windows writes path with backslashs `\`. 
In order to run WSL properly they must be replaced by slashs `/`. 
Goto [case/Allmesh](../../case/Allrun#L37) and fix the variable `MESHDIR`:  

~~~bash
MESHDIR="../meshCase"
~~~
