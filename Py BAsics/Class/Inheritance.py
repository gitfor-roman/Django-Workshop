class Music:
    def playMusic(self):
        return "Music has been started."
class Guitar(Music):
    def guitarMusic(self):
        return "Jhing Jhing Jhing Jhing Jhing Jhing Jhing Jhing Jhing"

music= Music()
guitar=Guitar()

print(music.playMusic())
print(guitar.guitarMusic())