# Assignment: Scores and Grades
# Karen Clark
# 2018-06-03

import random

# Assignment: Scores and Grades
# Write a function that generates ten scores between 
# 60 and 100. Each time a score is generated, your 
# function should display what the grade is for a 
# particular score
def scores_and_grades():

    def print_score(score, letter):
        print "Score: " + str(score) + "; Your grade is " + letter

    print "Scores and Grades"
    for i in range(0, 10):
        score = random.randint(60, 101)
        if score > 59 and score < 70:
            print_score(score, "D")
        elif score > 69 and score < 80:
            print_score(score, "C")
        elif score > 79 and score < 90:
            print_score(score, "B")
        elif score > 89 and score < 101:
            print_score(score, "A")
    
    print "End of the program. Bye!"

scores_and_grades()