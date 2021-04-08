import winsound

# 按一下电脑扬声器。这个 频率 参数指定声音的频率（赫兹），并且必须在37到32767之间。这个 期间 参数指定声音应持续的毫秒数。
winsound.Beep(1000, 500)

# 调用基础 MessageBeep() 来自平台API的函数。这将播放注册表中指定的声音。这个 type 参数指定要播放的声音；可能的值为 -1 ， MB_ICONASTERISK ， MB_ICONEXCLAMATION ， MB_ICONHAND ， MB_ICONQUESTION 和 MB_OK
winsound.MessageBeep()

# 调用基础 PlaySound() 来自平台API的函数。这个 声音 参数可以是文件名、系统声音别名、音频数据 bytes-like object 或 None . 它的解释取决于 flags ，它可以是下面描述的常量的按位或“或”组合。如果 声音 参数是 None ，任何当前播放的波形声音都将停止。
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
