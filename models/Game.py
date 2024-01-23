from models.GameOptions import GameOptions
from models.GameResults import GameResults
  
class Game:
  user_score = 0
  machine_score = 0

  def start(self):
    usr_choice = ""
    machine_choice = ""

    usr_choice = self.__user_turn()
    machine_choice = self.__machine_turn()

    print("MACHINE CHOICE: ", machine_choice)
    print("YOUR CHOICE: ", usr_choice)
    self.__check_result(usr_choice, machine_choice)
    self.new_round_or_end()

  def new_round_or_end(self):
    usr_input = input("Do you want new round ? Y/N").lower()

    if usr_input == "y":
      self.start()
    
  def __check_result(self, usr_choice: str, machine_choice: str):
    result = GameResults().check_result(usr_choice, machine_choice)

    if result == "won":
      self.user_score += 100
      print("You're WON! :)")
    elif result == "lose":
      self.machine_score += 100
      print("You're LOSE :(")
    else:
      print("You're TIED :/")

  def __user_turn(self):
    valid_input = False
    while valid_input == False:
      usr_input = input("Insert your choice:").lower()

      if (GameOptions().contains(usr_input)):
        valid_input = True
    
    return usr_input

  def __machine_turn(self):
    return GameOptions().get_random()