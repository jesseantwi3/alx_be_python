# Ask for the task description
task = input("Enter your task: ")

# Ask for the task priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if it is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# If it is time-bound, add immediate attention note
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# ✅ Print with f-string exactly as required
print(f"Reminder: {reminder}")


