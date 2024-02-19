# Create your Game class logic in here.
 
import time
from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("phrase one"),Phrase("phrase twooo"),Phrase("phrase threeee"),Phrase("phrase fourrrrrr"),Phrase("phrase fiveeeeeee")]
        self.active_phrase = None
        self.guesses = []
    def get_random_phrase(self):
      return random.choice(self.phrases)
      # return self.phrases[random.randint(0, len(self.phrases)-1)]

    def welcome(self):
      print('WELCOME TO THE PHRASE HUNTER GAME!')
    def start(self):
      self.welcome()
      self.active_phrase = self.get_random_phrase()
      while not self.game_over():
        self.active_phrase.display()
        guess = self.get_guess()
        self.guesses.append(guess)
        if not self.active_phrase.check_letter(guess):
          self.missed += 1
          print(f"you have {5-self.missed} guesses left")
      self.newgame()

      #self.game_over()

    def get_guess(self):
      while True:
        try:
          guess = input("Enger a letter: ").lower()
          if not guess.isalpha() or len(guess) != 1:
            raise ValueError("Please enter a single letter from a to z")
          return guess
        except ValueError as e:
          print(e)
    def game_over(self):
      if self.active_phrase.check_complete():
        print('Congrats you won!')
        return True
      elif self.missed >= 5:
        print('Sorry you ran out of guesses, GAME OVER!')
        return True
      return False
