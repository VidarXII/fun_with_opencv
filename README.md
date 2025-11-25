# fun_with_opencv

this was basically just me goofing off with opencv. pose_detection.ipynb allows you to record an initial action which you can then use as a target which, when recreated, prompts opencv to play a gif. The way you record this target action is by getting into said pose, then either having somebody else press d on your computer or you pressing it yourself as fast as possible, taking advantage of the delay. There is a lot more that can be done with this and I will be updating this readme as and when I get time to revisit this project, but for now, its just my 67 detector.

dependencies : opencv-contrib-python, mediapipe ( pip install mediapipe will take care of other dependencies as well)
              specifically only works on python 3.11 (not later versions, not compatible with this for whatever reason)

files : read.py(a trial run file to see if facial detection works)
        mediapipe.ipynb (also trial runs to see if mediapipe works, the last three cells can be used to record target hand actions the same way pose_detection does, but for hand landmarks)
        pose_detection.ipynb (the actual 67 detector in the project)
        assets (bunch of images and gifs used within the project)

application : opencv itself has multiple applications, this particular project itself has uses in terms of hand detection (for video games, apps, etc.) This also can be configured to recognise a variety of memes, my 67 detector being just the start. This project was just for fun but there's prospects to improve on this and make this an industry standard code. thanks sm for reading
