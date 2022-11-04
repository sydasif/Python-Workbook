class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sang_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birth Day to You",
                    "Happy Birth Day"])
twinkle = Song(["Twinkle Twinkle little star",
                "How are wonder what you are"])

happy_bday.sang_a_song()
twinkle.sang_a_song()
