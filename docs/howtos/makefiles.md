Makefiles - a dictionary for your possible cli tasks
======================================================================

First you should use your preferred editor to look into the main `./Makefile` to see the different tasks which you can perform. 

    gedit Makefile

In the `Makefile` you find a list of tasks (in Makefiles called "targets") and after each target with an indent the commands, which will be executed, when you call a specific target.  

~~~Makefile
TARGET1:
    target1-bash-command1
    target1-bash-command2

# non-executed comment for TARGET2  
TARGET2:
    target2-bash-command1
    target2-bash-command2
~~~

All targets can be started with following command in the command line interface: 

    make TARGET1
