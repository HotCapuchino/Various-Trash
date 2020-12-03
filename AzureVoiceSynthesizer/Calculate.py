import wave
import contextlib


def calculateAmountOfLetters(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    f.close()
    return len(content)


def calculateDurationOfAudio(file_name):
    with contextlib.closing(wave.open(file_name, "r")) as f:
        frames = f.getnframes()
        framerate = f.getframerate()
        return frames / framerate
