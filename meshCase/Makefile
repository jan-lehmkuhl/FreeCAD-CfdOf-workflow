
# stars Allmesh script to create the mesh
mesh:
	./Allmesh


# opens paraview for reviewing the mesh
view: 
	paraFoam


# deletes the mesh and the related log files
clean: 
	rm -f  log*
	rm -f  mesh_outside.stl
	rm -rf constant/extendedFeatureEdgeMesh
	rm -rf constant/polyMesh
	rm -rf constant/triSurface/*.eMesh
	rm -rf gmsh
