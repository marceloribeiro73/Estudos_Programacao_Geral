'''Exercicios de lopps em python do site exercism
https://exercism.org/tracks/python/exercises/making-the-grade
'''

#%%
"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    student_scores_rounded = []
    for score in student_scores:
        student_scores_rounded.append(round(score))
    return student_scores_rounded        


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    cont_failed =0
    for score in student_scores:
        if score <= 40:
            cont_failed += 1
    return cont_failed


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    list_best_scores = []
    for score in student_scores:
        if score >= threshold:
            list_best_scores.append(score)
    
    return list_best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    list_grades = []
    value_increment = round( (highest-41) / 4)
    for value_grade in range(41, highest, value_increment):
        list_grades.append(value_grade)
    return list_grades
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    list_student_ranking =[]

    for index, score in enumerate(student_scores):
        str_student_score = f'{index+1}. {student_names[index]}: {score}'
        list_student_ranking.append(str_student_score)

    return list_student_ranking

    


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    student_100 = []
    for student in student_info:
        if student[1] == 100:
            student_100.append(student)
            return student
    return student_100
    


#%%

round_scores([21.22,14,56.02,12.66,30.55])
#%%
count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40])

#%%
above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
#%%
letter_grades(highest=100)

#%%
student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
student_ranking(student_scores, student_names)

#%%
perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])