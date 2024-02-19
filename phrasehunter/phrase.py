# Create your Phrase class logic here.


class Phrase(object):
    def __init__ (self, phrase):
        if isinstance(phrase, str):
            self.phrase = phrase.lower() #normalizes the phrase
        else:
            raise ValueError("Phrase must be a string")
        self.guessed_letters = set() #contains all guesssed letters

    def display(self):
        display_phrase = '' #display phrase initially all blank
        for letter in self.phrase:
            if letter == ' ':
                display_phrase += ' ' 
            elif letter in self.guessed_letters:
                display_phrase += letter
                #add correctly guessed letter to display_phrase
            else:
                display_phrase += '_'
                #non-guessed letters will display as _  
        print(display_phrase)
    def check_letter(self, letter): 
            letter = letter.lower() #normalizes guessed letters
            if len(letter) == 1 and letter in self.phrase:
                self.guessed_letters.add(letter)
                return True
                #adds correctly guessed lettes to guessed_letters
                #also returns as True
            else:
                return False

    def check_complete(self):
        for letter in self.phrase:
            if letter != ' ' and letter not in self.guessed_letters:
                return False
        return True
        #checks if the phrase has been completely guessed 
