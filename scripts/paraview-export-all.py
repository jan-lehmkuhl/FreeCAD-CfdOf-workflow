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


from paraview.servermanager import ProxyManager
from paraview.simple import *

import os
import sys


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
    print("export renderViews to path:")
    print( os.path.abspath(outputPath) )

    layouts = ProxyManager().GetProxiesInGroup("layouts")

    for layout_name, layout_proxy in layouts.items():
        # print(f"Processing layout: {layout_name}")
        
        if layout_proxy is None:
            print(f"Layout proxy is None, skipping.")
            continue

        # Get the view from the layout
        try:
            view = layout_proxy.GetView(0)
            if view is None:
                print(f"No view found in layout: {layout_name}")
                continue

            # Use only the first part of layout_name tuple for filename
            layout_base_name = layout_name[0] if isinstance(layout_name, tuple) else str(layout_name)
            layout_base_name = layout_base_name.replace('#','').replace(' ','-')
            filename = f"{output_dir}/{layout_base_name}.png"

            # Save screenshot
            os.makedirs(output_dir, exist_ok=True)
            SaveScreenshot(filename, view, 
                           ImageResolution=[1280, 720],
                           )
            print(f"Saved: '{layout_base_name}'")

        except Exception as e:
            print(f"Error processing layout {layout_name}: {e}")
            continue



if __name__ == "__main__":
    load_data('pv.foam')
    load_state(paraview_state)
    export_views(output_dir)

elif __name__ =="__vtkconsole__":
    print("run script inside Paraview Python Shell")
    export_views(output_dir)
