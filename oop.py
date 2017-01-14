class song(object):
    def __init__(this,lyrics): 
       this.lyrics=lyrics
    def sing_me_a_song(this):
        for line in this.lyrics:
            print line
hbd=song(["HBD TO U","HBD TO ME","HBD TO ALL"])
bop=song(["hello to u","hello to me","hello to all"])
song.sing_me_a_song(hbd)
bop.sing_me_a_song()

