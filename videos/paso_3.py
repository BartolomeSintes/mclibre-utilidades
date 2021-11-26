from pyffmpeg import FFmpeg
# input_video = pyffmpeg.input("prueba.mp4")
# added_audio = pyffmpeg.input("prueba-1.mp3")
# merged_audio = pyffmpeg.filter([input_video.audio, added_audio], 'amix')
# (pyffmpeg
# .concat(input_video, merged_audio, v=1, a=1)
# .output("prueba-sonido.mp4")
# .run(overwrite_output=True))

ff = FFmpeg()
ff.options("-i prueba.mp4 -i prueba-1.mp3 -map 0:v -map 1:a -c:v copy -shortest prueba-sonido.mp4")

