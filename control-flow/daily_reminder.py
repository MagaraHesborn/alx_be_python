task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task that should be completed soon!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that should be completed this week!")
        else:
            print(f"{task} is a medium priority task that can be scheduled for later!")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task that can be done when you have free time!")
        else:
            print(f"{task} is a low priority task that can be postponed indefinitely!")