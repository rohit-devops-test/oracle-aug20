import random

class EmoticonGenerator(object):

    """docstring for  EmoticonGenerator."""

    def __init__(self, maxiterations):
        self.strings = "!@#$^*_-=+?/,.:;~"
        self.grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]
        self.maxiterations = maxiterations
        self.iterations = 0

    def create_emoticon(self, grp):
        """actual method that creates the emoticon"""
        face_strings_list = [random.choice(self.strings) for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        return emoticon


    def __iter__(self):
        """returns the self object to be accessed by the for loop"""
        return self

    def __next__(self):
        """returns the next emoticon indefinitely"""
        grp = random.choice(self.grouped_strings)
        self.iterations += 1
        if(self.iterations <= self.maxiterations):
            return self.create_emoticon(grp)
        else:
            raise StopIteration
     

if __name__ == '__main__':

    g =  EmoticonGenerator(10)
    for i in g:
        print(i)
