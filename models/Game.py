class Game:
  # constructor 
  def __init__(self, word: str, maxGuesses: int, totalGuesses: int):
    self.word = word
    self.maxGuesses = maxGuesses
    self.totalGuesses = totalGuesses
  # destructor
  def __del__(self):
    print("game ended")