import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer


class FFmpegVideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FFmpeg Video Player")

        # 创建QVideoWidget作为显示视频的区域
        self.video_widget = QLabel(self)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        self.setLayout(layout)

        # 启动 FFmpeg 解码器
        self.ffmpeg_process = subprocess.Popen(
            [
                'ffmpeg',
                '-i', '/Users/fanjunwei/Downloads/vvvv.mp4',  # 或其他流媒体源
                '-f', 'rawvideo',
                '-s', '640x360',
                '-pix_fmt', 'rgb24',
                '-'
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # 设定视频尺寸
        self.width = 640
        self.height = 360

        # 创建一个定时器，用来读取并显示帧
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 每 30 毫秒刷新一帧

    def update_frame(self):
        # 从FFmpeg进程的标准输出中读取帧
        raw_frame = self.ffmpeg_process.stdout.read(self.width * self.height * 3)

        if len(raw_frame) == self.width * self.height * 3:
            # 将帧数据转换为QImage
            image = QImage(raw_frame, self.width, self.height, QImage.Format_RGB888)

            # 将QImage转换为QPixmap并显示在QVideoWidget上
            pixmap = QPixmap.fromImage(image)
            self.video_widget.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication([])
    player = FFmpegVideoPlayer()
    player.show()
    app.exec()
