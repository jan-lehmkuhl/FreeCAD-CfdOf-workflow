
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
	git checkout meshCase/Makefile
	git checkout meshCase/.gitignore
	git checkout case/Makefile
	git checkout case/.gitignore
	mv -f case/0    case/0.org


# the mesh target changes to the folder meshCase and executes there "make mesh" 
mesh: 
	make -C meshCase mesh


# the run target changes to the folder case and executes there "make run" 
run: 
	make -C case run


# the viewMesh target changes to the folder meshCase and executes there "make view" 
viewMesh:
	make -C meshCase view


# the viewRun target changes to the folder case and executes there "make view" 
viewRun:
	make -C case view


# the clean target executes the clean targets in meshCase and case
clean: 
	make -C meshCase clean
	make -C case     clean
