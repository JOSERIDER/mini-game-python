from random import Random

class GameOptions():
  ROCK = "rock"
  PAPER = "paper"
  SCISSOR = "scissor"

  def contains(self, option: str) -> bool:
    return self.ROCK == option or self.PAPER == option or self.SCISSOR == option
  
  def get_random(self) -> str:
    index = Random().randrange(3)

    if index == 0:
      return self.ROCK
    elif index == 1: 
      return self.PAPER
    else:
      return self.SCISSOR