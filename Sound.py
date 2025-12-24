try:
     import simplegui
except ImportError:
     import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from AssetLoader import load_sound

BG_MUSIC = load_sound("bg.wav")
BG_MUSIC_DURATION = 90.12 * 1000

class Sound:
     def __init__(self):
          self.music_timer = simplegui.create_timer(int(BG_MUSIC_DURATION), self.replay_music)

     def play_music(self):
          BG_MUSIC.play()
          self.music_timer.start()

     def stop_music(self):
          BG_MUSIC.pause()
          self.music_timer.stop()

     def replay_music(self):
          BG_MUSIC.rewind()
          self.play_music()

sound = Sound()
