from turtle import Screen, Turtle
import turtle
from state_label import StateLabel, Score
import pandas as pd


"""
def get_mouse_click_coor(x, y):
    print(x, y)
"""
class Game():
    def __init__(self, file_path='day_twenty_five/50_states.csv',
                 image_path='day_twenty_five/blank_states_img.gif'):
        self.coord_file = file_path
        self.image = image_path
        self.coord_dict = dict()
        self.guessed = []
        with open(self.coord_file, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.split(',')
                self.coord_dict[line[0]] = (int(line[1]), int(line[2]))
                
        self.max_states = 50
        self.cur_score = 0
        self.score = Score()
        self.screen = Screen()
        self.screen.title('U.S. States Game')
        self.screen.addshape(self.image)
        turtle.shape(self.image) 
    
        
    def guess(self):
        answer = self.screen.textinput(title='Guess the State',
                                prompt='What\'s another state\'s name?')
        return(answer)
    
    
    def game_loop(self):
        self.screen.tracer(0)
        while self.cur_score < self.max_states:
            self.score.print_score(self.cur_score, self.max_states)
            self.screen.update()
            user_guess = self.guess().title()
            if user_guess == 'Exit':
                missed_states = [key for key in self.coord_dict.keys() if key not in self.guessed]
                missed_report = pd.DataFrame(missed_states, columns=['State'])
                missed_report.to_csv('day_twenty_five/missed_states.csv')
                self.score.game_over('Game Over!')

                break
            
            if user_guess in self.coord_dict.keys() and user_guess not in self.guessed:
                self.cur_score += 1
                self.guessed.append(user_guess)
                x, y = self.coord_dict[user_guess]
                label = StateLabel(user_guess, x, y)
                label.add_state()
            self.score.clear()
        else:
            self.score.game_over('Done!')
            
        self.screen.exitonclick()
            
            
            
game = Game()
game.game_loop()










