
# Makefiles are containing multiple "targets" (e.g. all, freecad-open, restore, ...)
# every target will execute normal bash commands
# a target is executed from bash with:
# 		make TARGETNAME
# a target can have prerequirements, so target "all" will first execute target "clean", "mesh" and "run"
# https://en.wikipedia.org/wiki/Make_(software)


MAKEFLAGS += --always-make

# some variables:
date = $(shell date +"%Y%m%d-%H%M%S%p")
archiveFolder = ARCHIVE/run-$(date)
paraviewState = '../post/paraview-state.pvsm'
    # Hint: also hard coded in scripts/paraview-export-all.py



# std workflow targets
# ======================================================

# run "make all" if you want to create everything new
all: clean fix-windows mesh run post


# freecad
# -----------------------------------------------

# this target opens the freecad GUI
# you can also execute the command "freecad freecad-cfd.FCStd" directly in the terminal
freecad-open:
	freecad freecad-cfd.FCStd


# meshing
# -----------------------------------------------

# starts Allmesh script within meshCase to create the mesh
mesh:
	cd meshCase ;  ./Allmesh


# OpenFOAM calculation
# -----------------------------------------------

run:
	sed --in-place --expression='s/\.\.\\meshCase/\.\.\/meshCase/'  case/Allrun
	cd case ;  ./Allrun


# reviewing created mesh and results
# -----------------------------------------------

post:
	cd case ;  pvbatch ../scripts/paraview-export-all.py


# opens paraview for reviewing the mesh
paraview-mesh:
	cd meshCase  ;  paraview pv.foam


paraview-run-no-state:
	cd case ;  paraview pv.foam

# opens paraview with the referenced state file for reviewing the results
paraview-run:
	cd case ;  paraview --state=$(paraviewState)


# archiving current data
# ======================================================

# creates a zipped filled of the current project without big mesh and calculated files
zip-repository:
	tar -vcjf  ARCHIVE-$(notdir $(CURDIR))-$(shell date +"%Y%m%d-%H%M%p").tar.bz2  --exclude='meshCase/constant'   --exclude='case/constant/polyMesh' --exclude='case/processor*' --exclude='*.tar.gz' --exclude='*.tar.bz2'  `ls -A -1`
	ls -la     .

# creates a zipped file of the current project without the ARCHIVE folder
zip-debug:
	tar -vcjf  ARCHIVE-$(notdir $(CURDIR))-$(shell date +"%Y%m%d-%H%M%p").tar.bz2  --exclude='ARCHIVE'   --exclude='case/constant/polyMesh' --exclude='case/processor*'   --exclude='*.tar.gz' --exclude='*.tar.bz2'  `ls -A -1`


# checks if the main files are stored in git repository
is-git-clean:
	@echo "** test whether main files are unchanged **"
	git diff  --quiet           freecad-cfd.FCStd
	git diff  --quiet           meshCase
	git diff  --quiet           case
	git diff  --quiet           post
	@echo "** test whether nothing is staged **"
	git diff  --quiet --cached
	@echo "** passed tests **"


archive-results: is-git-clean
	@echo archiving files to:      $(archiveFolder)
	mkdir                   $(archiveFolder)
	cp freecad-cfd.FCStd    $(archiveFolder)
	mv meshCase             $(archiveFolder)/meshCase
	mv case                 $(archiveFolder)/case
	mv post                 $(archiveFolder)/post
	git log  -n500        > $(archiveFolder)/git-log.txt
	@echo restoring tracked files
	git checkout meshCase
	git checkout case
	git checkout post



# cleaning the repository
# ======================================================

# the clean target executes the clean targets clean-mesh and clean-case to remove calculated files
clean: clean-mesh clean-case

# deletes the mesh and the related log files
clean-mesh: clean-preliminary-meshes
	rm -f  meshCase/log*
	rm -f  meshCase/mesh_outside.stl
	rm -f  meshCase/surfaceMesh.vtk
	rm -rf meshCase/constant/extendedFeatureEdgeMesh
	rm -rf meshCase/constant/polyMesh
	rm -rf meshCase/constant/triSurface/*.eMesh
	rm -rf meshCase/gmsh

clean-preliminary-meshes:
	rm -rf [1-9]

# deletes all files and folders created by the openFOAM-solver
clean-case:
	rm -rf case/log.*
	rm -rf case/constant/polyMesh
	rm -rf case/postProcessing
	rm -rf case/processor[0-9]
	rm -f  case/system/turbulenceLib


# deletes the complete FreeCAD export folders inklusive the necessary source files, which are also stored in git
delete-freecad-exports:
	rm -rf meshCase
	rm -rf case


# removes all changes in this repository and switches to the last git commit
reset: delete-freecad-exports
	git reset --hard


# removes on windows machines bad line endings which prevents bash scripts to run
fix-windows:
	@# https://stackoverflow.com/questions/14219092/bash-script-and-bin-bashm-bad-interpreter-no-such-file-or-directory
	@# removes cariage return "\r" at a line end "$"
	@# to mask a "$" in a makefile an additional $ is needed
	sed --in-place --expression='s/\r$$//'  meshCase/Allmesh
	sed --in-place --expression='s/\r$$//'  case/Allrun
