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
import datetime


paraview_state =    '../post/paraview-state.pvsm'
output_dir =        'visualization/paraview'

legend_font_size = 8    # Font size for legend labels
title_font_size = 10    # Font size for legend titles



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
        data_directory='.',
        restrict_to_data_directory=True,
        )

    animationScene1 = GetAnimationScene()
    animationScene1.GoToLast()



def adjust_legend_font_sizes(view, legend_font_size=14, title_font_size=16):
    try:
        representations = view.Representations

        # Handle scalar bar widgets (for 3D views)
        for rep in representations:
            if str(type(rep)).find('ScalarBarWidget') != -1:
                if hasattr(rep, 'LabelFontSize'):
                    rep.LabelFontSize = legend_font_size
                if hasattr(rep, 'TitleFontSize'):
                    rep.TitleFontSize = title_font_size

                # Additional scalar bar formatting options
                if hasattr(rep, 'LabelBold'):
                    rep.LabelBold = 0  # 0 = not bold, 1 = bold
                if hasattr(rep, 'TitleBold'):
                    rep.TitleBold = 1  # Make title bold
                if hasattr(rep, 'LabelItalic'):
                    rep.LabelItalic = 0  # 0 = not italic, 1 = italic
                if hasattr(rep, 'TitleItalic'):
                    rep.TitleItalic = 0

        # Handle line chart views specifically
        if hasattr(view, 'LegendFontSize'):
            view.LegendFontSize = legend_font_size
        if hasattr(view, 'LegendBold'):
            view.LegendBold = 0
        if hasattr(view, 'LegendItalic'):
            view.LegendItalic = 0

        # For line chart views, also try to adjust axis label fonts
        view_type = str(type(view))
        if 'LineChart' in view_type or 'XYChart' in view_type:
            # Left axis properties
            if hasattr(view, 'LeftAxisLabelFontSize'):
                view.LeftAxisLabelFontSize = legend_font_size
            if hasattr(view, 'LeftAxisTitleFontSize'):
                view.LeftAxisTitleFontSize = title_font_size
            # Bottom axis properties
            if hasattr(view, 'BottomAxisLabelFontSize'):
                view.BottomAxisLabelFontSize = legend_font_size
            if hasattr(view, 'BottomAxisTitleFontSize'):
                view.BottomAxisTitleFontSize = title_font_size
            # Right axis properties
            if hasattr(view, 'RightAxisLabelFontSize'):
                view.RightAxisLabelFontSize = legend_font_size
            if hasattr(view, 'RightAxisTitleFontSize'):
                view.RightAxisTitleFontSize = title_font_size
            # Top axis properties
            if hasattr(view, 'TopAxisLabelFontSize'):
                view.TopAxisLabelFontSize = legend_font_size
            if hasattr(view, 'TopAxisTitleFontSize'):
                view.TopAxisTitleFontSize = title_font_size

    except Exception as e:
        print(f"Warning: Could not adjust legend font sizes: {e}")
        import traceback
        traceback.print_exc()



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
            filename = f"{output_dir}/{clean_name}.png"

            # Save screenshot
            os.makedirs(output_dir, exist_ok=True)
            adjust_legend_font_sizes(view, legend_font_size, title_font_size)

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
    print("Export Screenshots inside Paraview Python Shell")
    print( datetime.datetime.now().isoformat())

    export_views(output_dir)

    print("finished export at: " + datetime.datetime.now().isoformat())
