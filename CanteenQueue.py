from collections import deque
students=deque([1,2,3,4,5,6,7,8,9,10])

def serve_food():
    print('Students are served in order:',students)
    students.rotate(-1)

print('breakfast')
serve_food()
print('lunch')
serve_food()
print('dinner')
serve_food()