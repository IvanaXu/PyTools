# -*-coding:utf-8-*-
# @auth ivan
# @time 20200105
# @goal Test pydub
from pydub import AudioSegment
song = AudioSegment.from_wav("098.Test_Pydub_test-192khz-16bit.wav")
print(song)

# ms
unit = 1000
five_seconds = 3 * unit

first_10_seconds = song[:five_seconds]
last_5_seconds = song[-five_seconds:]

# 将音量提高6dB
start = first_10_seconds + 6
# 将音量降低3dB
end = last_5_seconds - 3

# 连接
without_the_middle = start + end
assert without_the_middle.duration_seconds == 6
print(without_the_middle.duration_seconds)

without_the_middle.export("098.Test_Pydub_without_the_middle.mp3",
                          format="mp3")
