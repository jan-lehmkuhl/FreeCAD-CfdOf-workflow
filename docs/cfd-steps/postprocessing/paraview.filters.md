Use Filters in Paraview
======================================================================

A first introduction is available in this [Video](https://drive.google.com/file/d/1dwdbhs--ozPWSsoJ7KqU_WeFgamhNrOt). 

When you have load a cfd result in ParaView all data is available at the first entry in the Pipeline Browser. 
From this starting point all data is **cut down with Filters** to pieces where you can look at. 



Some available Filters
------------------------------------------------------------

### Clip
A clip is a nice filter for reviewing your mesh. 
Use `Crincle clip` to look only on complete cells.


### Slice
A slice gives you a plane where you can plot a colored variable. 


### Glyph
A Glyph prints vector arrows from your flow. 
This works fine on a slice. 
Make sure the glyph length and scale depends on the desired variable. 


### Surface Vectors
Slice -> Surface Vectors -> Glyph  
This shows you the flow projected onto a plane.  


### Stream Tracer
Stream tracer can nicely be placed on inlets an show the flow. 
