
# Makefiles are containing multiple "targets" (e.g. all, openfreecad, restore, ...)
# every target will execute normal bash commands
# a target is executed from bash with:
# 		make TARGETNAME
# a target can have prerequirements, so target "all" will first execute target "clean", "mesh" and "run"
# https://en.wikipedia.org/wiki/Make_(software) 



# targets
# ======================================================

# run "make all" if you want to create everything new
all: clean mesh run


# this target opens the freecad GUI
# you can also execute the command "freecad freecad-cfd.FCStd" directly in the terminal
openfreecad:
	freecad freecad-cfd.FCStd


# after exporting files from freecad everything inside case and meshCase will be overwriten
# this target moves the folder 0 inside case to 0.org, because otherwise 0 will be overwritten from the openfoam-solver
restore:
	mv -f case/0    case/0.org


# starts Allmesh script within meshCase to create the mesh
mesh: 
	cd meshCase ;  ./Allmesh


# run copies the initial state from 0.org to 0 and starts the Allrun script
run: 
	cp -rf  case/0.org  case/0 
	cd case ;  ./Allrun


# opens paraview for reviewing the mesh
viewMesh:
	cd meshCase  ;  paraFoam


# opens paraview for reviewing the results
viewRun:
	cd case  ;  paraFoam -builtin


# the clean target executes the clean targets cleanMesh and cleanCase
clean: cleanMesh cleanCase

# deletes the mesh and the related log files
cleanMesh: 
	rm -f  meshCase/log*
	rm -f  meshCase/mesh_outside.stl
	rm -rf meshCase/constant/extendedFeatureEdgeMesh
	rm -rf meshCase/constant/polyMesh
	rm -rf meshCase/constant/triSurface/*.eMesh
	rm -rf meshCase/gmsh


# deletes all files and folders created by the openFOAM-solver
cleanCase: 
	rm -rf case/log.*
	rm -rf case/0
	rm -rf case/constant/polyMesh
	rm -rf case/processor[0-9]
