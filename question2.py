class Netflix:
    shows = []
    
    def __init__(self, name, genres, episodes=10):
        self.name = name
        self.genres = genres
        self.episodes = episodes
        self.shows.append(self)
        
    def __str__(self):
        genre_str = ", ".join(self.genres)
        return(f"Show name: {self.name}\n"
               f"Episodes : {self.episodes}\n"
               f"Genre: {genre_str}") 
        
    @classmethod
    def numofshow(total):
        print("Total number of shows:", len(total.shows))
        for show in total.shows:
          print(show.name)        
        
s1 = Netflix("Wednesday",["Mystery","Supernatural"],15)
print(s1)
s2 = Netflix("Dark",["Mind-Bending","Sci-fi"])
print(s2)
Netflix.numofshow()
s3 = Netflix("Wednesday",["Comedy","Courtroom"],20)
print(s3)
s4 = Netflix("Demon Slayer",["Anime"],22)
print(s4)
Netflix.numofshow()      
         