
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
# git checkout restores the Makefiles and .gitignore-files from the repository
# and moves the folder 0 inside case to 0.org, because otherwise 0 will be overwritten from the openfoam-solver
restore:
	git checkout case/Makefile
	git checkout case/.gitignore
	mv -f case/0    case/0.org


# starts Allmesh script within meshCase to create the mesh
mesh: 
	cd meshCase ;  ./Allmesh


# the run target changes to the folder case and executes there "make run" 
run: 
	make -C case run


# opens paraview for reviewing the mesh
viewMesh:
	cd meshCase  ;  paraFoam


# the viewRun target changes to the folder case and executes there "make view" 
viewRun:
	make -C case view


# the clean target executes the clean targets cleanMesh and cleanCase
clean: cleanMesh 
	make -C case     clean

# deletes the mesh and the related log files
cleanMesh: 
	rm -f  meshCase/log*
	rm -f  meshCase/mesh_outside.stl
	rm -rf meshCase/constant/extendedFeatureEdgeMesh
	rm -rf meshCase/constant/polyMesh
	rm -rf meshCase/constant/triSurface/*.eMesh
	rm -rf meshCase/gmsh


