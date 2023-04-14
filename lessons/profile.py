class Profile:

    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str):
        self.handle = handle 
        self.followes = 0 
        self.is_private = False

    def tweet(self, msg: str) -> None:
        if not self.is_private:
            print(f"{self.handle} tweets {msg}")

    def toggle_privacy(self) -> None:
        self.is_private = not self.is_private
    
a: Profile = Profile ("alyssa")
b: Profile = Profile("tyler")
a.tweet("Sup")
b.toggle_privacy()
b.tweet("Heyyy")
