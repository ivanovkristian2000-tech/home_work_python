"""Воспроизведение мультимедиа

Создайте два класса:

AudioFileMixin — требует наличие поля audio_tracks (список треков).
Метод play_audio() выводит:

Воспроизведение аудио для <НазваниеКласса>:

<название трека>

<название трека>

VideoFileMixin — требует наличие поля video_files (список видео).
Метод play_video() выводит:

Воспроизведение видео для <НазваниеКласса>:

<название видео>

<название видео>

Если нужное поле отсутствует — выбрасывайте AttributeError."""



class AudioFileMixin:
    def play_audio(self):
        print(f"Воспроизведение аудио для {type(self).__name__}:")
        if hasattr(self, "audio_tracks"):
            for track in self.audio_tracks:
                    print(track)
        else:
            raise AttributeError("У объекта отсутствует audio_tracks")


class Player(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class VideoFileMixin:
    def play_video(self):
        print(f"Воспроизведение видео для {type(self).__name__}:")
        if hasattr(self, "video_files"):
            for video in self.video_files:
                print(video)
        else:
            raise AttributeError("У объекта отсутствует video_files")


class VideoPlayer(VideoFileMixin):
    def __init__(self, video_files):
        self.video_files = video_files




tracks = ["track1", "track2", "track3"]
videos = ["vid1", "vid2", "vid3"]

play = Player(tracks)
play.play_audio()

play_vid = VideoPlayer(videos)
play_vid.play_video()
