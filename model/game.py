class Game:
  # correctGuesses: int
  # if correctGuesses == num of uniq letters in word, you win


  # iterate over word
  # if letter we're on not in uniq chars add _
  # if it is in uniq char, leave alone


  # word: test
  # guesses: xt
  # totalGuesses: 2

  ####
  # ------
  #   |  |
  #   0  |
  #      |
  #      |
  # ------
  #
  # wrong: x
  # right: t__t
  ####

  # constructor 
  def __init__(self, word: str, maxGuesses: int, totalGuesses: int, 
  wrongGuesses: str, rightGuesses: str, uniqChars: str):
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