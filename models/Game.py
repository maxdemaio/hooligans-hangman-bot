class Game:
  # constructor 
  def __init__(self, word: str, maxGuesses: int, totalGuesses: int):
    self.word = word
    self.maxGuesses = maxGuesses
    self.totalGuesses = totalGuesses

  # destructor
  def __del__(self):
    print("game destroyed")
  
  # get word
  def getWord(self):
    return self.word

  # set word
  def setWord(self, w: str):
    self.word = w