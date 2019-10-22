
all: clean mesh run

openfreecad:
	freecad freecad-cfd.FCStd

mesh: 
	make -C meshCase mesh

run: 
	make -C case run

view: 
	make -C case view

clean: 
	make -C meshCase clean
	make -C case     clean
