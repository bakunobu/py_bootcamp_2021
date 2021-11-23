#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



PATH = './day_twenty_four/Mail Merge Project Start'
        
LETTER_BODY = '/Input/Letters/starting_letter.txt'
NAMES = '/Input/Names/invited_names.txt'
WRITE_TO = '/Output/ReadyToSend/'


class LetterWriter():
    def __init__(self, main_path, letter_path, names_path, write_to):
        self.main_path = main_path
        self.letter_path = letter_path
        self.names_path = names_path
        self.write_to = write_to
        self.letter_body = None
        self.name_list = []
        
    
    def get_body(self):
        path = self.main_path + self.letter_path
        with open(path, 'r') as f:
            self.letter_body = f.read()
            
    
    def get_names(self):
        path = self.main_path + self.names_path
        with open(path, 'r') as f:
            data = f.readlines()
            for name in data:
                name = name.replace('\n', '')
                self.name_list.append(name)
    
    
    def create_letter(self, name):
        letter = self.letter_body.replace('[name]', name)
        return(letter)
    
    
    def write_letter(self, name):
        filename = f'letter_for_{name}.txt'
        letter_filled = self.create_letter(name)
        path = self.main_path+self.write_to+filename
        with open(path, 'w') as f:
            f.write(letter_filled)
            
            
    def fill_all_letters(self):
        self.get_body()
        self.get_names()
        for name in self.name_list:
            self.write_letter(name)
        

sender = LetterWriter(PATH,
                      LETTER_BODY,
                      NAMES,
                      WRITE_TO)

sender.fill_all_letters()