import subprocess
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import QUrl

# 创建ffmpeg子进程
ffmpeg_process = subprocess.Popen(
    ['ffmpeg', '-i', 'input.mp4', '-f', 'flv', 'out.flv'],
    stdout=subprocess.PIPE
)

# 创建QMediaPlayer对象
media_player = QMediaPlayer()

# 从ffmpeg子进程的标准输出流播放音频
# media_player.setMedia(
#     QMediaContent(QUrl.fromLocalFile(ffmpeg_process.stdout))
# )
media_player.setSource(QUrl.fromLocalFile("file://./out.flv"))

# 开始播放
media_player.play()

# 从ffmpeg子进程的标准输出流播放视频
# TODO: 实现视频播放逻辑
