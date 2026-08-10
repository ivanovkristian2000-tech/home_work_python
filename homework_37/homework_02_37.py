"""Устройства

Создайте два класса:
MediaPlayer — поддерживает только аудио. Принимает список треков.
Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.
Данные:

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]


Пример вывода:
Воспроизведение аудио для MediaPlayer:

track1.mp3
track2.mp3

Воспроизведение аудио для Laptop:

track1.mp3
track2.mp3

Воспроизведение видео для Laptop:

movie.mp4
trailer.mov"""



class AudioFileMixin:
    def play_audio(self):
        print(f"Воспроизведение аудио для {type(self).__name__}:")
        if hasattr(self, "audio_tracks"):
            for track in self.audio_tracks:
                print(track)
        else:
            raise AttributeError("У объекта отсутствует audio_tracks")


class VideoFileMixin:
    def play_video(self):
        print(f"Воспроизведение видео для {type(self).__name__}:")
        if hasattr(self, "video_files"):
            for vid in self.video_files:
                print(vid)
        else:
            raise AttributeError("У объекта отсутствует video_files")


class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(VideoFileMixin, AudioFileMixin):
    def __init__(self, video_files, audio_tracks):
        self.video_files = video_files
        self.audio_tracks = audio_tracks




tracks = ["track1", "track2", "track3"]
videos = ["vid1", "vid2", "vid3"]

player = MediaPlayer(tracks)
player.play_audio()

laptop = Laptop(videos, tracks)
laptop.play_video()
laptop.play_audio()
