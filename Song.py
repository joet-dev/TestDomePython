class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        check = set()
        current = self
        while current is not None: 
            if current in check: 
                return True
            check.add(current)
            current = current.next
            
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)
    
print(first.is_in_repeating_playlist())