
run: 
	cp -rf  0.org  0 
	./Allrun

mesh: 
	make -C ../meshCase mesh

view: 
	paraFoam -builtin

clean: 
	rm -rf log.*
	rm -rf 0
	rm -rf constant/polyMesh
	rm -rf processor[0-9]
