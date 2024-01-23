from models.GameOptions import GameOptions

class GameResults:
  WON = "won"
  LOSE = "lose"
  TIED = "tied"

  def check_result(self, usr_choice: str, machine_choice: str):
    if usr_choice == machine_choice:
      return self.TIED
    elif usr_choice == GameOptions.ROCK and machine_choice == GameOptions.SCISSOR:
      return self.WON
    elif usr_choice == GameOptions.SCISSOR and machine_choice == GameOptions.PAPER:
      return self.WON
    elif usr_choice == GameOptions.PAPER and machine_choice == GameOptions.ROCK:
      return self.WON
    else:
      return self.LOSE
    