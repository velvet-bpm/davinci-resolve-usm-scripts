# davinci-resolve-usm-toolkit
Scripts that allow the easier creation of custom usm animations for Dokkan using DaVinci Resolve
The first script auto imports the .wav files into your Media Pool in a sub folder called Sound Effects.
It changes the project name to USM and creates a timeline called video and also changing the track names to clips and sound_effects.

The second script should be run when the animation is finished, it creates a file in the Documents folder with the PlaySe command with the sound effect id and frame it should start at. You just need to paste it in the lua you'll use :)

**Installation**
-  Download both scripts and the wav.zip
-  Extract the wav folder in your Documents folder
-  And add both scripts in the C:/Users/%USER%/AppData/Roaming/Blackmagic Design/DaVinci Resolve/Support/Fusion/Scripts/Comp folder

**How to run**
-  With DaVinci Resolve opened, create a new project.
-  In said project, on the top menu go to: Workspace -> Scripts -> Comp
-  Run the script you want to run
