import numpy as np

student_scores = np.load("student_scores.npy")
print(student_scores)
#make an array of 5 students, make each variable inside a zero
#calculate mean using np.mean using axis = 1 and put it into an array[0]
#make it for other ones
print(np.mean(student_scores, axis=0))
print(np.mean(student_scores, axis=1))
print(np.mean(student_scores))
print(np.mean(np.sort(student_scores, axis = 1),axis = 1)[::-1][:3])
#divide original score data by a massive consisting of max numbers
print(student_scores/np.max(student_scores, axis = 1).reshape(-1,1)*100)
