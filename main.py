from termcolor import colored
print(colored("Welcome to ToDo(s) Manager!", "cyan", attrs=["bold"]))
print(colored("1. View | 2. Add ToDo | 3. Remove ToDo | 4. Quit", "yellow", attrs=["bold"]))

def view():
		with open("todo-tasks.txt", "r") as f:
			all_todo = f.readlines()
			if len(all_todo) == 0:
				print(colored("No incomplete todos! Great!", "green", attrs=["bold"]))
			else:
				print(colored(colored("Following are incomplete todos:", "magenta", attrs=["bold"])))
				for n, todo in enumerate(all_todo):
					print(colored(f"{n}. {todo}", "white", attrs=["bold"]))
		
def add_todo(todo):
	with open("todo-tasks.txt", "a") as f:
			f.write(f"{todo}\n")
			print(colored("Success!", "green", attrs=["bold"]))

def rem_todo(todo_no):
		with open("todo-tasks.txt", "r") as f:
			all_todo = f.readlines()
			del all_todo[todo_no]
			
		with open("todo-tasks.txt", "w") as f:
			for todo in all_todo:
				f.write(todo)
			print(colored("Success!", "green", attrs=["bold"]))

while True:
	user_input = int(input(colored("\nEnter Choice: ", attrs=["bold"])))
	if user_input == 1:
		view()
	elif user_input == 2:
		add_todo(input("Enter ToDo Task: "))
	elif user_input == 3:
		rem_todo(int(input("Enter ToDo Number: ")))
	else:
		print(colored("Thank You!", "green", attrs=["bold"]))
		exit()