from os import system as cmd
hell = input('What would you like to do? Add, Remove or List ')
if  hell.lower() == 'add':
	cmd('python3 todoadd.py')
elif hell.lower() == 'remove':
	cmd('python3 todorem.py')
elif hell.lower() == 'list':
	cmd('python3 todolist.py')
else:
	print('Error: Please pick Add, Remove or List')
	cmd('python3 todo.py')
