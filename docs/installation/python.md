Standard Python
======================================================================

To execute [Python Postprocessing](../../scripts/python-postprocessing.py) from `make post` its necessary 
to install [Python3](https://www.python.org) and 
to install its installer "pip" if its not yet present.  

    python3 --version
    pip --version

    sudo apt update
    sudo apt-get install python3
    sudo apt-get install python3-pip


## Pandas and Matplotlib
Additionally some packages inside Python are used

    python3 -m pip install matplotlib
    python3 -m pip install pandas

~~~bash
# for matplotlib
Requirement already satisfied: matplotlib in /usr/lib/python3/dist-packages (3.5.1)

# for pandas
Requirement already satisfied: pandas in /usr/lib/python3/dist-packages (1.3.5)
~~~



To run [Paraview Picture Export](../../scripts/paraview-export-all.py) you need [Python from Paraview](paraview.md).  
