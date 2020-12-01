
# Makefiles are containing multiple "targets" (e.g. all, openfreecad, restore, ...)
# every target will execute normal bash commands
# a target is executed from bash with:
# 		make TARGETNAME
# a target can have prerequirements, so target "all" will first execute target "clean", "mesh" and "run"
# https://en.wikipedia.org/wiki/Make_(software) 


# some variables: 
date = $(shell date +"%Y%m%d-%H%M%S%p")
archiveFolder = ARCHIVE/run-$(date)



# std workflow targets
# ======================================================

# run "make all" if you want to create everything new
all: clean mesh run


# freecad
# -----------------------------------------------

# this target opens the freecad GUI
# you can also execute the command "freecad freecad-cfd.FCStd" directly in the terminal
openfreecad:
	freecad freecad-cfd.FCStd
	make store0as0org


# after exporting files from freecad everything inside case and meshCase will be overwriten
# this target moves the folder 0 inside case to 0.org, because otherwise 0 will be overwritten from the openfoam-solver
store0as0org:
	if [ ! -d case/0.org ] ;  then      \
		echo "*** copy 0 to 0.org"  ; \
		cp -rf case/0    case/0.org   ; \
	fi ; 


# meshing
# -----------------------------------------------

# starts Allmesh script within meshCase to create the mesh
mesh: 
	cd meshCase ;  ./Allmesh


# OpenFOAM calculation
# -----------------------------------------------
copy0orgto0:
	mkdir -p case/0
	cp -rf  case/0.org/*  case/0

# run copies the initial state from 0.org to 0 and starts the Allrun script
run: store0as0org copy0orgto0
	cd case ;  ./Allrun


# reviewing created mesh and results
# -----------------------------------------------

# opens paraview for reviewing the mesh
viewMesh:
	cd meshCase  ;  paraFoam


# opens paraview for reviewing the results
viewResults:
	cd case  ;  paraFoam -builtin


# creates a zipped filled of the current project without the ARCHIVE folder
zip:
	tar -vcjf  ARCHIVE-$(notdir $(CURDIR))-$(shell date +"%Y%m%d-%H%M%p").tar.bz2  --exclude='meshCase/constant' --exclude='*.stl' --exclude='*.pvsm' --exclude='case/0' --exclude='case/constant/polyMesh' --exclude='case/processor*' --exclude='*.tar.gz' --exclude='*.tar.bz2'  `ls -A -1`
	ls -la     .

# split archives to 10mb parts for a better uploading
# splitArchive:
#   split -b 10M  ARCHIVE.tar.gz  ARCHIVE.tar.gz.part
# rebuildArchive:
#   cat  ARCHIVE.tar.gz.part*  >  ARCHIVE.tar.gz



# archiving current data
# ======================================================

# checks if the main files are stored in git repository
isGitClean:
	@echo "** test whether main files are unchanged **"
	git diff  --quiet           freecad-cfd.FCStd
	git diff  --quiet           meshCase
	git diff  --quiet           case
	git diff  --quiet           post
	@echo "** test whether nothing is staged **"
	git diff  --quiet --cached
	@echo "** passed tests **"


archiveResults: isGitClean
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

# the clean target executes the clean targets cleanMesh and cleanCase to remove calculated files
clean: cleanMesh cleanCase

# deletes the mesh and the related log files
cleanMesh: cleanPreliminaryMeshes
	rm -f  meshCase/log*
	rm -f  meshCase/mesh_outside.stl
	rm -rf meshCase/constant/extendedFeatureEdgeMesh
	rm -rf meshCase/constant/polyMesh
	rm -rf meshCase/constant/triSurface/*.eMesh
	rm -rf meshCase/gmsh

cleanPreliminaryMeshes:
	rm -rf [1-9]

# deletes all files and folders created by the openFOAM-solver
cleanCase: 
	rm -rf case/log.*
	rm -rf case/0
	rm -rf case/constant/polyMesh
	rm -rf case/postProcessing
	rm -rf case/processor[0-9]


# deletes the complete FreeCAD export folders inklusive the necessary source files, which are also stored in git
deleteFreecadExports:
	rm -rf meshCase
	rm -rf case


# removes all changes in this repository and switches to the last git commit
reset: deleteFreecadExports
	git reset --hard


# removes on windows machines bad line endings which prevents bash scripts to run
fix-windows: 
	# https://stackoverflow.com/questions/14219092/bash-script-and-bin-bashm-bad-interpreter-no-such-file-or-directory
	sed -i -e 's/\r$//'  case/Allmesh
	sed -i -e 's/\r$//'  case/Allrun
