#!/usr/bin/env python
from effect_relations import id_and_name
from collections import defaultdict
import os
folder_path = os.path.join(os.environ["USERPROFILE"],"Documents")
new_file_path = os.path.join(folder_path, "SeCommands.lua")

project_manager = resolve.GetProjectManager()
current_project = project_manager.LoadProject('USM')
current_timeline = current_project.GetCurrentTimeline()
timeline_start_frame = current_timeline.GetStartFrame()
timeline_frame_rate = current_project.GetSetting("timelineFrameRate")


audio_track_list_items = current_timeline.GetItemListInTrack('audio',2)

effect_id_and_start_frames = defaultdict(list)
frames = []

if audio_track_list_items:
    for item in audio_track_list_items:
        for key in id_and_name:
            if id_and_name.get(key) == item.GetName().split('.')[0]:
                effect_id_and_start_frames[key].append(f"{round((item.GetStart() - timeline_start_frame) * 60 / timeline_frame_rate)}")
else:
    print("No item in track list")


if effect_id_and_start_frames:
    if new_file_path:
                os.remove(new_file_path)
    for effect in effect_id_and_start_frames:
        for frame in effect_id_and_start_frames[effect]:
            with open(new_file_path, "a+") as file:
                file.write(f'playSeVer2(spep_0 + {frame}, {effect}, "", 0, 0, 0, -1 ) --{id_and_name.get(effect)}\n')

