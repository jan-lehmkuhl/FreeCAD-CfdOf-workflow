# ================================================================================
#      ___                 _            _                 _            _      _ 
#     |_  |               | |          | |               | |          | |    | |
#       | |  __ _  _ __   | |      ___ | |__   _ __ ___  | | __ _   _ | |__  | |
#       | | / _` || '_ \  | |     / _ \| '_ \ | '_ ` _ \ | |/ /| | | || '_ \ | |
#   /\__/ /| (_| || | | | | |____|  __/| | | || | | | | ||   < | |_| || | | || |
#   \____/  \__,_||_| |_| \_____/ \___||_| |_||_| |_| |_||_|\_\ \__,_||_| |_||_|
#  
#   https://github.com/jan-lehmkuhl
#  
#   Purpose:    Export all Layouts from specified Paraview state as png
#   Author(s):  Jan Lehmkuhl
#  
#   Description:
#   Can be executed with 
#       pvbatch THIS_SCRIPT.py
#   or from "Run Script" in Paraview GUI
#  
# ================================================================================


from paraview.simple import *

import os
import sys


def main():
    load_data('pv.foam')
    load_state('../post/paraview-state.pvsm')
    export_views('visualization/paraview')


def load_data(paraviewDataDummy):
    print("load "+paraviewDataDummy)
    if not os.path.exists(paraviewDataDummy):
        print("ERROR: >" +paraviewDataDummy +"< not found")
        print( os.path.abspath(paraviewDataDummy) )
        return

    pvfoam = OpenFOAMReader(FileName=paraviewDataDummy)


def load_state(paraviewState):
    print("load paraview state: ")
    print( os.path.abspath(paraviewState) )

    if not os.path.exists(paraviewState):
        print("ERROR: paraview state-file not found")
        return

    LoadState(paraviewState,
        # DataDirectory='../shared/postStates',
        # pvfoamFileName='pv.foam'
        )

    animationScene1 = GetAnimationScene()
    animationScene1.GoToLast()


def export_views(outputPath):
    print("export renderViews to path:")
    print( os.path.abspath(outputPath) )

    idx = 1
    while True:
        try:
            renderView1 = FindView('RenderView' +str(idx))

            renderView1.ViewSize = [1359, 799]
            SetActiveView(renderView1)

            print("save renderView: " +str(idx))
            os.makedirs(outputPath, exist_ok=True)
            SaveScreenshot(outputPath +'/renderView' +str(idx) +'.png', renderView1, ImageResolution=[1359, 798])

            idx += 1
        except:
            break


if __name__ == "__main__":
    main()
elif __name__ =="__vtkconsole__":
    print("run script inside Paraview Python Shell")
    main()
