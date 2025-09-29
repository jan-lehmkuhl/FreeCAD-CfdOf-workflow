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
import re
import fileinput

import matplotlib.pyplot as plt
import pandas as pd


paraview_state =    '../post/paraview-state.pvsm'
output_dir =        'visualization/paraview'

legend_font_size = 8    # Font size for legend labels
title_font_size = 10    # Font size for legend titles



#   Paraview Picture Export
# ==============================================================================

def load_data(paraviewDataDummy):
    print("load "+paraviewDataDummy)
    if not os.path.exists(paraviewDataDummy):
        print("ERROR: >" +paraviewDataDummy +"< not found")
        print("    " + os.path.abspath(paraviewDataDummy) )
        exit()

    pvfoam = OpenFOAMReader(FileName=paraviewDataDummy)



def check_state_file_compatibility(state_file_path):
    """Check ParaView state file for common compatibility issues"""
    print(f"Analyzing state file: {state_file_path}")
    
    try:
        with open(state_file_path, 'r') as f:
            content = f.read()
            
        # Check ParaView version
        version_match = re.search(r'<ServerManagerState version="([^"]+)"', content)
        if version_match:
            state_version = version_match.group(1)
            print(f"State file created with ParaView version: {state_version}")
        
        # Check for problematic patterns that might cause the NoneType error
        proxy_without_id = re.findall(r'<Proxy[^>]*(?!.*id=)[^>]*>', content)
        if proxy_without_id:
            print(f"WARNING: Found {len(proxy_without_id)} Proxy elements without id attribute")
            print("This might cause compatibility issues with some ParaView versions")
        
        # Check for file references
        file_refs = re.findall(r'FileName[^>]*>([^<]+)', content)
        if file_refs:
            print(f"Found file references in state: {set(file_refs[:5])}...")  # Show first 5
            
        return True
    except Exception as e:
        print(f"Error analyzing state file: {e}")
        return False



def remove_path_before_pvfoam(paraviewState): 
    """
    Remove any path before 'pv.foam' in the ParaView state file, so that only 'pv.foam' remains as the file reference.
    This is useful for making the state file portable across different machines/directories.
    """

    print("WARNING: Replace values=\"...pv.foam\" with value=\"pv.foam\" in state file")
    for line in fileinput.input(paraviewState, inplace=True):
        line = re.sub(r'(<Element[^>]*value=")[^"]*pv\.foam(")', r'\1pv.foam\2', line)
        print(line, end='')



def load_state(paraviewState):
    print("load paraview state: ")
    print("    " + os.path.abspath(paraviewState) )
    print("in current working directory: ")
    print("    " + os.getcwd() )

    if not os.path.exists(paraviewState):
        print("ERROR: paraview state-file not found")
        exit()

    check_state_file_compatibility(paraviewState)

    # Strategy 1: Try with DataPath method (newer ParaView versions)
    try:
        print("Attempt 1: Loading with DataPath mapping...")
        LoadState(paraviewState, 
                 data_directory=os.getcwd(),
                 restrict_to_data_directory=True)
        print("State loaded successfully with DataPath method")
        animationScene1 = GetAnimationScene()
        animationScene1.GoToLast()
        return
    except Exception as e:
        print(f"DataPath method failed: {e}")

    # Strategy 2: Try with filenames parameter (traditional method)
    try:
        print("Attempt 2: Loading with filenames mapping...")
        LoadState(paraviewState, 
                 filenames=[{
                     'FileName': os.path.join( os.getcwd(), "pv.foam" ),
                     'name': 'pv.foam',
                 }])
        print("State loaded successfully with filenames method")
        animationScene1 = GetAnimationScene()
        animationScene1.GoToLast()
        return
    except Exception as e:
        print(f"Filenames method failed: {e}")

    # Strategy 3: Load without file mapping (least robust but most compatible)
    try:
        print("Attempt 3: Loading without file mapping...")
        remove_path_before_pvfoam(paraviewState)
        LoadState(paraviewState)
        print("State loaded successfully without file mapping")
        print("WARNING: File paths in state may not be properly mapped!")
        animationScene1 = GetAnimationScene()
        animationScene1.GoToLast()
        return
    except Exception as e:
        print(f"No mapping method failed: {e}")

    # If all methods fail, give detailed error information
    print("ERROR: All state loading methods failed.")
    print("This suggests a fundamental incompatibility with the ParaView state file.")
    print("Possible solutions:")
    print("1. Regenerate the state file with your current ParaView version")
    print("2. Check ParaView version compatibility")
    print("3. Manually verify the state file XML structure")
    exit(1)
    animationScene1.GoToLast()



def adjust_legend_font_sizes(view, legend_font_size=14, title_font_size=16):
    verbose = False
    try:
        if verbose: print(f"Adjusting legend properties: font={legend_font_size}, title={title_font_size}")

        representations = view.Representations

        # Handle scalar bar widgets (for 3D views)
        for rep in representations:
            if str(type(rep)).find('ScalarBarWidget') != -1:
                if hasattr(rep, 'LabelFontSize'):
                    rep.LabelFontSize = legend_font_size
                    if verbose: print(f"  Set ScalarBar LabelFontSize to {legend_font_size}")
                if hasattr(rep, 'TitleFontSize'):
                    rep.TitleFontSize = title_font_size
                    if verbose: print(f"  Set ScalarBar TitleFontSize to {title_font_size}")

                # Additional scalar bar formatting options
                if hasattr(rep, 'LabelBold'):
                    rep.LabelBold = 0  # 0 = not bold, 1 = bold
                    if verbose: print(f"  Set ScalarBar LabelBold to 0")
                if hasattr(rep, 'TitleBold'):
                    rep.TitleBold = 1  # Make title bold
                    if verbose: print(f"  Set ScalarBar TitleBold to 1")
                if hasattr(rep, 'LabelItalic'):
                    rep.LabelItalic = 0  # 0 = not italic, 1 = italic
                    if verbose: print(f"    Set ScalarBar LabelItalic to 0")
                if hasattr(rep, 'TitleItalic'):
                    rep.TitleItalic = 0
                    if verbose: print(f"    Set ScalarBar TitleItalic to 0")

        # Handle line chart views specifically
        if hasattr(view, 'LegendFontSize'):
            view.LegendFontSize = legend_font_size
            if verbose: print(f"  Set view LegendFontSize to {legend_font_size}")
        if hasattr(view, 'LegendBold'):
            view.LegendBold = 0
            if verbose: print(f"  Set view LegendBold to 0")
        if hasattr(view, 'LegendItalic'):
            view.LegendItalic = 0
            if verbose: print(f"  Set view LegendItalic to 0")

        # For line chart views, also try to adjust axis label fonts
        view_type = str(type(view))
        if 'LineChart' in view_type or 'XYChart' in view_type:
            if verbose: print(f"  Found line chart view, adjusting axis fonts")

            # Left axis properties
            if hasattr(view, 'LeftAxisLabelFontSize'):
                view.LeftAxisLabelFontSize = legend_font_size
                if verbose: print(f"  Set LeftAxisLabelFontSize to {legend_font_size}")
            if hasattr(view, 'LeftAxisTitleFontSize'):
                view.LeftAxisTitleFontSize = title_font_size
                if verbose: print(f"  Set LeftAxisTitleFontSize to {title_font_size}")
            # Bottom axis properties
            if hasattr(view, 'BottomAxisLabelFontSize'):
                view.BottomAxisLabelFontSize = legend_font_size
                if verbose: print(f"  Set BottomAxisLabelFontSize to {legend_font_size}")
            if hasattr(view, 'BottomAxisTitleFontSize'):
                view.BottomAxisTitleFontSize = title_font_size
                if verbose: print(f"  Set BottomAxisTitleFontSize to {title_font_size}")
            # Right axis properties
            if hasattr(view, 'RightAxisLabelFontSize'):
                view.RightAxisLabelFontSize = legend_font_size
                if verbose: print(f"  Set RightAxisLabelFontSize to {legend_font_size}")
            if hasattr(view, 'RightAxisTitleFontSize'):
                view.RightAxisTitleFontSize = title_font_size
                if verbose: print(f"  Set RightAxisTitleFontSize to {title_font_size}")
            # Top axis properties
            if hasattr(view, 'TopAxisLabelFontSize'):
                view.TopAxisLabelFontSize = legend_font_size
                if verbose: print(f"  Set TopAxisLabelFontSize to {legend_font_size}")
            if hasattr(view, 'TopAxisTitleFontSize'):
                view.TopAxisTitleFontSize = title_font_size
                if verbose: print(f"  Set TopAxisTitleFontSize to {title_font_size}")


        if verbose: print(f"  Completed font adjustments for view")

    except Exception as e:
        print(f"WARNING: Could not adjust legend font sizes: {e}")
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



#   Plotting Data from "postProcessing" Folder
# ==============================================================================

def plot_data(file_path, logy= True):
    """
    https://gist.github.com/kastnerp/e76fb8ec1394fe0b0926deb07b9689f1
    """

    export_path = "visualization/plots"
    data_name = file_path.split("/")[-1].rstrip('.dat')

    if not os.path.exists(file_path):
        print("File not found: ", file_path)
        return False

    with open(file_path, 'r') as file:
        lines_starting_with_hash = [line for line in file if line.startswith('#')]

    print("write plot for " +file_path)
    data = pd.read_csv(file_path, skiprows=len(lines_starting_with_hash)-1, delimiter=r'\s+').iloc[:, 1:].shift(+1,axis=1).drop(["Time"], axis= 1)

    plot = data.plot(logy= logy, figsize=(15,5))
    fig = plot.get_figure()
    ax = plt.gca()
    ax.legend(loc='upper right')
    ax.set_xlabel("Iterations")
    ax.set_ylabel(data_name)
    ax.grid(linestyle="--")

    os.makedirs(export_path, exist_ok=True)
    plt.savefig(os.path.join(export_path, data_name +".png") ,dpi=600)


def plot_postProcessing_data():
    plot_data("postProcessing/residuals/0/residuals.dat")
    plot_data("postProcessing/probes/0/p", logy= False)



if __name__ == "__main__":
    print("\nCrete plots from postProcessing folder\n==================================================")
    plot_postProcessing_data()

    print("\nCrete ParaView visualizations\n==================================================")
    load_data('pv.foam')
    load_state(paraview_state)
    export_views(output_dir)

elif __name__ =="__vtkconsole__":
    print("Export Screenshots inside Paraview Python Shell")
    print("    " + datetime.datetime.now().isoformat())

    export_views(output_dir)

    print("finished export at: " + datetime.datetime.now().isoformat())
