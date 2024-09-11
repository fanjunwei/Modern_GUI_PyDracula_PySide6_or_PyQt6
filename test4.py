import subprocess
import sys
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSlider
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, Qt, QIODevice, QByteArray, QProcess
import pathlib


class CustomIODevice(QIODevice):
    def __init__(self, data: bytes):
        super().__init__()
        self.data = data
        self.pos = 0

    def readData(self, maxSize: int) -> int:
        # 读取数据
        size = min(maxSize, len(self.data) - self.pos)
        if size > 0:
            data = self.data[self.pos:self.pos + size]
            self.pos += size
            return data
        return -1

    def writeData(self, data: QByteArray) -> int:
        # 写入数据（这个例子中不支持写入）
        return 0

    def isSequential(self) -> bool:
        # 是否支持随机访问
        return True

    def size(self) -> int:
        # 返回数据的大小
        return len(self.data)


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 1024, 768)
        output = pathlib.Path('./') / 'out.flv'
        process = QProcess()
        process.setProgram("ffmpeg")
        process.setArguments(['-i', '/Users/fanjunwei/Downloads/vvvv.mp4', '-y', '-f', 'flv', '-'])
        process.start()
        # ffmpeg_process = subprocess.Popen(
        #     ['ffmpeg', '-i', '/Users/fanjunwei/Downloads/vvvv.mp4', '-y', '-f', 'flv', '-'],
        #     stdout=subprocess.PIPE
        # )
        # all_data = bytearray()
        # device = CustomIODevice(all_data)

        # def run():
        #     try:
        #         while True:
        #             data = ffmpeg_process.stdout.read(1024)  # 读取音频数据
        #             if not data:
        #                 break
        #             all_data.extend(data)
        #     except KeyboardInterrupt:
        #         pass
        #     finally:
        #         ffmpeg_process.terminate()
        #
        # Thread(target=run).start()

        self.media_player = QMediaPlayer()
        # self.media_player.setSource(QUrl.fromLocalFile(str(output)))
        self.media_player.setSourceDevice(process, QUrl(''))
        device = self.media_player.sourceDevice()
        self.video_widget = QVideoWidget()
        self.audio_output = QAudioOutput()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setAudioOutput(self.audio_output)

        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_video)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_video)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_video)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.sliderMoved.connect(self.set_position)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

    def set_position(self, position):
        self.media_player.setPosition(position)

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_player = VideoPlayer()
    video_player.show()
    sys.exit(app.exec())
