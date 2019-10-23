
all: clean mesh run

openfreecad:
	freecad freecad-cfd.FCStd

restore:
	git checkout meshCase/Makefile
	git checkout meshCase/.gitignore
	git checkout case/Makefile
	git checkout case/.gitignore
	mv -f case/0    case/0.org

mesh: 
	make -C meshCase mesh

run: 
	make -C case run

viewMesh:
	make -C meshCase view

viewRun:
	make -C case view

clean: 
	make -C meshCase clean
	make -C case     clean
