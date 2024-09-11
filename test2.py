import subprocess
import pyaudio


def play_audio_stream():
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)

    # 启动FFmpeg进程
    ffmpeg_process = subprocess.Popen(
        ['ffmpeg', '-i', '/Users/fanjunwei/Downloads/vvvv.mp4', '-f', 's16le', '-ar', '44100', '-ac', '2', '-'],
        stdout=subprocess.PIPE,
        bufsize=10 ** 8
    )

    try:
        while True:
            data = ffmpeg_process.stdout.read(1024)  # 读取音频数据
            if not data:
                break
            stream.write(data)  # 写入到PyAudio流
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        ffmpeg_process.terminate()


# 在MainWindow中调用这个函数
def start_playback():
    play_audio_stream()


start_playback()
