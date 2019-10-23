
# run copies the initial state from 0.org to 0 and starts the Allrun script
run: 
	cp -rf  0.org  0 
	./Allrun


# executes "make mesh" in meshCase
mesh: 
	make -C ../meshCase mesh


# opens paraview for reviewing the results
view: 
	paraFoam -builtin


# deletes all files and folders created by the openFOAM-solver
clean: 
	rm -rf log.*
	rm -rf 0
	rm -rf constant/polyMesh
	rm -rf processor[0-9]
