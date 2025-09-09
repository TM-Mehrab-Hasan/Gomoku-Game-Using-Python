# Build script for creating Gomoku Game executable
# Run this script to create a standalone .exe file

import os
import subprocess
import sys

def build_exe():
    """Build the Gomoku Game executable using PyInstaller."""
    print("Building Gomoku Game executable...")
    
    # PyInstaller command with options
    cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--windowed",          # Hide console window (for GUI apps)
        "--name=GomokuGame",   # Name of the executable
        "--add-data=GUI_Pic;GUI_Pic",  # Include GUI_Pic folder
        "--icon=GUI_Pic/black.png",    # Use black.png as icon (optional)
        "gomoku.py"            # Main Python file
    ]
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print(f"Executable created in: dist/GomokuGame.exe")
        print("\nYou can find your standalone executable at:")
        print(os.path.abspath("dist/GomokuGame.exe"))
        
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        print(f"Error output: {e.stderr}")
        return False
    
    return True

if __name__ == "__main__":
    build_exe()
