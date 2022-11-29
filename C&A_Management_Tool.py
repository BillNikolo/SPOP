'''
Date: 27/11/2022
Time: 10.30 am
Author: Vasileios Nikolopoulos
Product Name: Classroom and Attendance Management
Project general Description: This project concerns a tool that handles the Classrooms
and provide to Professor administrative access and management over it.
File Content: This is the main file that initiates the project, contains all the necessary classes
and methods. This is only a draft and needs much more time of programming to get it working.
'''

import numpy
from numpy import np
import random

Classrooms = {}
Professors = {}
Students = {}

class Classroom:

	def __init__(self, course_name, pr_Initials, number_of_seats, time, room_number, duration):
		self.course_name = course_name
		self.pr_Initials = pr_Initials
		temp = random.randint(10**6, 10**7)
		while temp in Classrooms.keys():
			temp = random.randint(10 ** 6, 10 ** 7)
		else:
			self.class_id = temp
		self.number_of_seats = number_of_seats
		self.time = time
		self.room_number = room_number
		self.registered_students = 0
		self.duration = duration
		if number_of_seats % 4 == 0:
			self.seating = np.full((number_of_seats/4, 4), "-")
		else:
			self.seating = np.full((number_of_seats/4 + 1, 4), "-")
		Classrooms[self.class_id] = [self.course_name, pr_Initials, self.registered_students]
		print("The classroom was created successfully!")

	def change_time(self, new_time):
		self.time = new_time
		print(f"The new time of the class is {self.time}")

	def change_room_number(self, new_number):
		self.room_number = new_number
		print(f"The new time of the class is {self.room_number}")

	def change_number_of_seats(self, new_number):
		"Need to change it a little bit"
		self.number_of_seats = new_number
		print(f"The new time of the class is {self.number_of_seats}")

	def visualize_seating(self):
		print(self.seating)

	def book_a_seat(self, row, column, student_Initials):
		if self.registered_students < self.number_of_seats:
			while self.seating[row, column] != "-":
				print("This seat has been selected, please choose another one: ")
				row = int(input("Please choose the row"))
				column = int(input("Please choose the column"))
			else:
				self.seating[row, column] = student_Initials


class Professor:
	def __init__(self):
		pass

	def createClass(self):
		pass

	def changeInfo(self):
		pass

	def cancelClass(self):
		pass

	def professorLogIn(self):
		pass

	def changeProfessorPassword(self):
		pass

	def extractAttendanceList(self):
		pass

	def professor_Int(self):
		pass

class Student:
	def __init__(self):
		pass

	def registerStudent(self):
		pass

	def registerClass(self):
		pass

	def changeSeating(self):
		pass

	def unregisterFromClass(self):
		pass

	def student_Int(self):
		pass

if __name__ == "__main__":
	while True:
		print("Welcome to my Class management Tool")
		target = input("Are you a Professor(1) or a student(2)")

