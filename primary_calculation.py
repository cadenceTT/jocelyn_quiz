# !/urs/bin/env/python3
# coding:utf-8

import datetime
import random


def number_writing(ceil, matrix):
    """
    This function lead children to learn the numbers and signs writing.

    :param ceil: A positive integers, for the ceil of all numbers.

    :prama matrix: A two elements list of positive integers. matrix[0]
    is the number of column, and matrix[1] is the number of row.
    """
    DOCU_PATH = '/Users/dongrentan/PycharmProjects/Jocelyn_quiz/five_years_old/'
    DATE_STR = datetime.datetime.now().strftime('%Y%m%d')
    FILE_NAME = 'Quiz_NumWriting_' + DATE_STR
    FULL_PATH = DOCU_PATH + FILE_NAME + '.txt'
    PRIMARY_SIGNS = '+-×÷='

    quiz = open(FULL_PATH, 'w')
    title = '                  Quiz for Number Writing ' + DATE_STR + '\n\n'
    student = 'Student:____            Time:____            Grades:____\n\n'
    description = 'Description: This is a quiz for number writing, with ' \
                  'numbers\nbelow ' + str(ceil) + '.\n\n'
    quiz.writelines(title+student+description)
    for i in range(matrix[1]):
        line = ''
        for j in range(matrix[0]):
            blank = 1
            mix = []
            for k in range(9):   # 90% probability give a number, while 10% give a sign.
                mix.append(random.randint(0, ceil))
            mix.append(random.choice(PRIMARY_SIGNS))
            a = random.choice(mix)
            if type(a) == int and a >= 10:
                blank -= 1
            line += str(a) + blank*' ' + ':____      '
        line += '\n'
        quiz.writelines(line)
    return quiz.close()


def tow_numbers_plus(ceil, matrix):
    """
    This function randomly generate a quiz into a text file.
    There will be matrix[0] * matrix[1] problems in the quiz,
    and all of them are testing for plus/add ability testing.

    :param ceil: A two elements list of non-negative integers(natural numbers).
    ceil[0] is the possible ceil of number 1, and ceil[1] is the possible
    ceil of number 2. This parameter define the difficulty of the
    quiz.

    :param matrix: A two elements list of positive integers. matrix[0]
    is the number of column, and matrix[1] is the number of row.

    :return: A .txt file storing the quiz.
    """

    DOCU_PATH = '/Users/dongrentan/PycharmProjects/Jocelyn_quiz/five_years_old/'
    DATE_STR = datetime.datetime.now().strftime('%Y%m%d')
    FILE_NAME = 'Quiz_2NumPlus_' + DATE_STR
    FULL_PATH = DOCU_PATH + FILE_NAME + '.txt'

    quiz = open(FULL_PATH, 'w')
    title = '                Quiz for Two Numbers Plus ' + DATE_STR + '\n\n'
    student = 'Student:____            Time:____            Grades:____\n\n'
    description = 'Description: This is a quiz for PLUS method, which one ' \
                  'number\nis below ' + str(ceil[0]) + \
                  ', and the other is below ' + str(ceil[1]) + '.\n\n'
    quiz.writelines(title+student+description)
    for i in range(matrix[1]):
        line = ''
        for j in range(matrix[0]):
            blank = 1
            a = random.randint(0, ceil[0])
            if a < 10:
                blank += 1
            b = random.randint(0, ceil[1])
            if b < 10:
                blank += 1
            line += str(a) + '+' + str(b) + blank*' ' + '=       '
        line += '\n'
        quiz.writelines(line)
    return quiz.close()


if __name__ == '__main__':
    ceil = [20, 10]
    matrix = [5, 10]
    number_writing(ceil[0], matrix)
    tow_numbers_plus(ceil, matrix)
