scores: dict = {
    "a": 1,
    "e": 1,
    "l": 1,
    "i": 1,
    "n": 1,
    "o": 1,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10
}

with open("words_small.txt", "r") as word_file:
    for line in word_file:
        word = line.strip()
        
        # get the score for the current word
        score = 0
        for letter in word:
            score += scores[letter]
        print("word:", word, "score:", score)