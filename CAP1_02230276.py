################################
# Name: Tshering Dorji
# Department: 1 Mechanical Engineering
# Student ID: 02230276
################################
# REFERENCES
#Python File Open : https://www.w3schools.com/python/python_file_handling.asp and https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
#CSF 101 Notes
#Youtube: https://www.youtube.com/watch?v=Uh2ebFW8OYM
#Youtube: https://www.youtube.com/watch?v=DmHSwTiD5Tk
################################
# SOLUTION
# Your Solution Score: 50223
# Put your number here:
# input_6_cap1
################################
# Read the input.txt file
def read_input():
    game_data = []  # creating an empty list
    with open('C:/Users/user/Desktop/CSF 2024/CSF-101-CAP/input_6_cap1.txt','r') as file:    #helps to read file
        data_of_the_file = file.readlines()
        for line in data_of_the_file:
            values = line.strip().split()    # strip removes the whitespaces and split splits the line into values
            game_data.append((values[0], values[1]))
    return game_data

# solution
def calculate_score(game_data):
    choices_score = {'A': 1, 'B': 2, 'C': 3}    #using dictionary to map choice to score
    outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}   #using dictionary to map outcome to score
    total_score = 0     #initial score is zero

    for opponent_move, outcomes in game_data: 
        your_move = 0
        #using conditional statement to find the score
        if outcomes == 'Y': #for draw(Y)
            your_move = opponent_move #choose same option
        elif outcomes == 'Z': #For win(Z)
            if opponent_move == 'A':    #Rock
                your_move = 'B' #Paper
            elif opponent_move == 'B':  #paper
                your_move = 'C' #scissors
            elif opponent_move == 'C':  #scissors
                your_move = 'A' #rock
        elif outcomes == 'X':   #For lose(X)
            if opponent_move == 'A':    #rock
                your_move = 'C' #scissors
            elif opponent_move == 'B':  #paper
                your_move = 'A' #rock
            elif opponent_move == 'C':  #scissors
                your_move = 'B' #paper
        

        your_score = choices_score[your_move] + outcome_scores[outcomes]   #Score for the round

        total_score += your_score  #total score for the game

    return total_score

# Calling the functions
game_data = read_input()
end_score = calculate_score(game_data)
print(f"Total Score: {end_score}")
