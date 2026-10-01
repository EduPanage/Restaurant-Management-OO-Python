class Music:
    
    musics = []
    
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration
        
        Music.musics.append(self)

        
    def convertMin(self, duration):
        mins, secs = divmod(duration, 60)
        return f'{mins} mins e {secs} secs'    
    
    
    @classmethod
    def listMusics(cls):
        print('\nMusics: ')
        for music in cls.musics:
            print(music)
        
    def __repr__(self):
        return f'\nName: {self.name}\nArtist: {self.artist}\nDuration: {self.convertMin(self.duration)} \n'