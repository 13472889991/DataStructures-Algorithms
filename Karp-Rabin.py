class RollingHash():
    def __init__(self, string=""):
        self.string = list(string)
        self.hash = sum([ord(i) for i in string])

    def remove(self, char):
        self.hash -= ord(char)
        self.string.pop(0)

    def add(self, char):
        self.hash += ord(char)
        self.string.append(char)

    def __str__(self):
        return str(self.hash)


def karprabin(target, text):
    hash1=RollingHash(target)
    hash2=RollingHash(text[0:len(target)])
    if hash1.hash == hash2.hash:
        if hash1.string == hash2.string:
            return True
    for i in range(len(target),len(text)):
        hash2.remove(hash2.string[0])
        hash2.add(text[i])
        print(hash1,hash2)
        if hash1.hash == hash2.hash:
            if hash1.string == hash2.string:
                return True

    return False


print(karprabin("Hello", "Hello World"))