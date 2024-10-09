# must be executed by pvbatch from paraview installation


from paraview.simple import *

import os
import sys


def main():
    paraviewState = '../post/paraview-state.pvsm'
    outputPath = 'visualization/paraview'

    if not os.path.exists(paraviewState):
        print("Did not find state-file")
        return False



    print("load pv.foam and paraview state")
    # ==========================================================

    pvfoam = OpenFOAMReader(FileName='pv.foam')
    LoadState(paraviewState,
        DataDirectory='../shared/postStates',
        pvfoamFileName='pv.foam')

    animationScene1 = GetAnimationScene()
    animationScene1.GoToLast()



    print("execute picture export")
    # ==========================================================

    #   export renderViews
    # ------------------------------------------------
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
