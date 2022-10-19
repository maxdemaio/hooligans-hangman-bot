class Game:
  # constructor 
  def __init__(self, word: str, maxGuesses: int, totalGuesses: int, 
  wrongGuesses: str, rightGuesses: str, uniqChars: int):
    self.word = word
    self.maxGuesses = maxGuesses
    self.totalGuesses = totalGuesses
    self.wrongGuesses = wrongGuesses
    self.rightGuesses = rightGuesses
    self.uniqChars = uniqChars

  # destructor
  def __del__(self):
    print("game destroyed")
  
  def getWord(self) -> str:
    return self.word

  def getMaxGuesses(self) -> int:
    return self.maxGuesses

  def getTotalGuesses(self) -> int:
    return self.totalGuesses

  def getUniqChars(self) -> int:
    return self.uniqChars

  def getWrongGuesses(self) -> str:
    return self.wrongGuesses

  def getRightGuesses(self) -> str:
    return self.rightGuesses

  def setWord(self, w: str):
    self.word = w

  def setUniqChars(self, u: int):
    self.uniqChars = u

  def incrGuesses(self):
    if self.totalGuesses + 1 > self.maxGuesses:
      raise Exception("total guesses cannot exceed max guesses")
    self.totalGuesses += 1

  def addRightGuess(self, g: str):
    if len(g) != 1:
      raise Exception("guess must be 1 character")
    self.rightGuesses += g
  
  def addWrongGuess(self, g: str):
    if len(g) != 1:
      raise Exception("guess must be 1 character")
    self.wrongGuesses += g

  def resetGame(self):
    self.word = None
    self.maxGuesses = 6
    self.totalGuesses = 0
    self.wrongGuesses = ""
    self.rightGuesses = ""
    self.uniqChars = 0