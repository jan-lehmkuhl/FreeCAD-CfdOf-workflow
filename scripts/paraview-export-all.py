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
#   Purpose:    Export all Views from Layouts specified in Paraview state as png
#   Author(s):  Jan Lehmkuhl
#  
#   Description:
#   Can be executed with 
#       pvbatch THIS_SCRIPT.py
#   or from "Run Script" in Paraview GUI
#  
# ================================================================================


from paraview.servermanager import ProxyManager
from paraview.simple import *

import os


paraview_state =    '../post/paraview-state.pvsm'
output_dir =        'visualization/paraview'



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
    print("export Paraview-Views as image to path:")
    print( os.path.abspath(outputPath) )

    views = ProxyManager().GetProxiesInGroup("views")

    if not views:
        print("No views found")
        return

    for view_name, view in views.items():
        if view is None:
            print(f"View {view_name} is None, skipping.")
            continue

        try:
            if isinstance(view_name, tuple):
                clean_name = str(view_name[0])
            else:
                clean_name = str(view_name)
            
            clean_name = clean_name.replace('#','').replace(' ','-').replace('/','-')
            
            # Create filename
            filename = f"{output_dir}/{clean_name}.png"

            # Save screenshot
            os.makedirs(output_dir, exist_ok=True)
            SaveScreenshot(filename, view, 
                           ImageResolution=[1280, 720],
                           )
            print(f"Saved: '{clean_name}'")

        except Exception as e:
            print(f"Error processing view {view_name}: {e}")
            continue



if __name__ == "__main__":
    load_data('pv.foam')
    load_state(paraview_state)
    export_views(output_dir)

elif __name__ =="__vtkconsole__":
    print("run script inside Paraview Python Shell")
    export_views(output_dir)
