import time
from termcolor import colored
print(colored("Welcome to ToDo App, by Sanskar!", "blue", attrs=["bold"]))
todo_tasks = input("Tasks to add in todo list: ")

#opening file to append tasks 	
f = open("todo-tasks.txt", "a")
f.write(f"{todo_tasks} — Added on {time.asctime()}\n")

print(colored(f"'{todo_tasks}' was added in todo list.", "green", attrs=["bold"]))
f.close()

print('\n---------------#-------------#-----------')

print("Press 1 to see your incomplete todo(s) or 0 to quit")
user_choice = int(input("Enter Your Choice: "))

#opening file to read
f2 = open("todo-tasks.txt", "r")
contents = f2.readlines()

if user_choice == 1:
	print(colored("\nYour incomplete todo(s) are: ", "magenta", attrs=["bold"]))	
	i =0
	for content in contents:
		print(colored(f"{i}. {content}", "magenta", attrs=["bold"]))
		i += 1	
			
elif user_choice == 0:
	print("Thank You For Using Our Program!")
	exit()
		
else:
	print("Invalid Choice!")
f2.close()

edit_choice = int(input("To edit todo list press 1 or 0 to quit: "))

if edit_choice == 1:
    remove_choice = int(input("Select todo to remove from list: "))
    del contents[remove_choice]

    # Now open the file in write mode #fix
    f3 = open("todo-tasks.txt", "w")
    for content2 in contents:
        f3.write(content2)
    f3.close()
    print(colored("Success!", "green", attrs=["bold"]))

elif edit_choice == 0:
    print("Thank You For Using Our Program!")
    exit()

else:
    print("Invalid Option!")
	
f3.close()