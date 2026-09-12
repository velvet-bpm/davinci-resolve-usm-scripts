#!/usr/bin/env python
import os
from effect_relations import id_and_name
folder_path = os.path.join(os.environ["USERPROFILE"],"Documents","wav")
files = []

for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)

    if os.path.isfile(filepath):
        for key in id_and_name:
            if filename.split('.wav')[0] == id_and_name.get(key):
                files.append(filepath)
                break
            else:
                continue
        

project_manager = resolve.GetProjectManager()
media_storage = resolve.GetMediaStorage()
project = project_manager.CreateProject('USM')
current_project = project_manager.LoadProject('USM')


media_pool = current_project.GetMediaPool()

timeline = media_pool.CreateEmptyTimeline('Video')
current_project.SetCurrentTimeline(timeline)
current_timeline = current_project.GetCurrentTimeline()

video_track = current_timeline.SetTrackName('video', 1, 'Clips')
audio_track = current_timeline.SetTrackName('audio', 1, 'Sound Effects')

root_folder = media_pool.GetRootFolder()
sub_folder = media_pool.AddSubFolder(root_folder, "Sound Effects")
current_folder = media_pool.SetCurrentFolder(sub_folder)

clips = media_storage.AddItemListToMediaPool(files)


