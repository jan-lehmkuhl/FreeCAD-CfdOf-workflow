
# Makefiles are containing multiple "targets" (e.g. all, open-freecad, restore, ...)
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
open-freecad:
	freecad freecad-cfd.FCStd
	make store-0-as-0org


# after exporting files from freecad everything inside case and meshCase will be overwriten
# this target moves the folder 0 inside case to 0.org, because otherwise 0 will be overwritten from the openfoam-solver
store-0-as-0org:
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
copy-0org-to-0:
	mkdir -p case/0
	cp -rf  case/0.org/*  case/0

# run copies the initial state from 0.org to 0 and starts the Allrun script
run: store-0-as-0org copy-0org-to-0
	cd case ;  ./Allrun


# reviewing created mesh and results
# -----------------------------------------------

# opens paraview for reviewing the mesh
view-mesh:
	cd meshCase  ;  paraFoam


# opens paraview for reviewing the results
view-results:
	cd case  ;  paraFoam -builtin



# archiving current data
# ======================================================

# creates a zipped filled of the current project without big mesh and calculated files
zip-archive:
	tar -vcjf  ARCHIVE-$(notdir $(CURDIR))-$(shell date +"%Y%m%d-%H%M%p").tar.bz2  --exclude='meshCase/constant' --exclude='*.stl' --exclude='*.pvsm' --exclude='case/0' --exclude='case/constant/polyMesh' --exclude='case/processor*' --exclude='*.tar.gz' --exclude='*.tar.bz2'  `ls -A -1`
	ls -la     .

# creates a zipped file of the current project without the ARCHIVE folder
zip-debug:
	tar -vcjf  ARCHIVE-$(notdir $(CURDIR))-$(shell date +"%Y%m%d-%H%M%p").tar.bz2  --exclude='ARCHIVE'   --exclude='*.tar.gz' --exclude='*.tar.bz2'  `ls -A -1`

# split archives to 10mb parts for a better uploading
# splitArchive:
#   split -b 10M  ARCHIVE.tar.gz  ARCHIVE.tar.gz.part
# rebuildArchive:
#   cat  ARCHIVE.tar.gz.part*  >  ARCHIVE.tar.gz


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
	rm -rf meshCase/constant/extendedFeatureEdgeMesh
	rm -rf meshCase/constant/polyMesh
	rm -rf meshCase/constant/triSurface/*.eMesh
	rm -rf meshCase/gmsh

clean-preliminary-meshes:
	rm -rf [1-9]

# deletes all files and folders created by the openFOAM-solver
clean-case: 
	rm -rf case/log.*
	rm -rf case/0
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
	# https://stackoverflow.com/questions/14219092/bash-script-and-bin-bashm-bad-interpreter-no-such-file-or-directory
	# removes cariage return "\r" at a line end "$"
	# to mask a "$" in a makefile an additional $ is needed
	sed -i -e 's/\r$$//'  meshCase/Allmesh
	sed -i -e 's/\r$$//'  case/Allrun
