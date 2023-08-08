from helpers import *
from prompt_toolkit import prompt
from rich import print

# Tasks:
# 1. Show all the runners
# 2. Show a runner's details
#   - including name, id, miles run, and current workout
# 3. Show all the workouts
# 4. Show all the trails
# 5. Choose a runner to run with
# 6. Choose a trail for that runner to run
# 7. See the runners ranked by miles run with medals for the top 3
# 8. Assign yourself as a new runner
# 9. Have a runner complete all the workouts and show a message indicating they are ready for the marathon
# 10. Write some fun welcome and goodbye messages
# 11. Add styling and slow type


def display_welcome():
    print("hi")


def display_main_menu():
    print_make_selection()
    print("1. View all runners")
    print("2. Add yourself to our running training program")
    print("3. Exit App")


def display_all_runners():
    runners = get_all_runners()
    for runner in runners:
        print_runner_info(runner)
        print_make_selection()
        print("1. See runner stats")
        print("2. Choose a runner to run with")
        print("3. Main menu")
        choice = input()
        if choice == "1":
            choose_runner_by_id()
        elif choice == "2":
            choose_runner_by_id()
            print(
                f"Congrats! you have chosen {runner.name}. Hope you know what you are doing..."
            )
        elif choice == "3":
            display_main_menu()
        else:
            invalid_choice()


def choose_runner_by_id():
    search_id = input("Enter the ID of the runner you'd like to choose")
    runner = find_runner_by_id(search_id)
    print_runner_info(runner)
    print_workout_details(runner)
    display_runner_stats_menu(runner)


def display_runner_stats_menu(runner):
    print_make_selection()
    print("1. See a list of trails to choose from")
    print("2. See runner ranking")
    print("3. Back to all runners")
    print("4. Main menu")
    choice = input()
    handle_runner_choice(choice, runner)


def handle_runner_choice(choice, runner):
    if choice == "1":
        display_all_trails()
    elif choice == "2":
        get_runner_ranking()
    elif choice == "3":
        display_all_runners()
    elif choice == "4":
        display_main_menu()
    else:
        invalid_choice()


def display_all_trails():
    trails = get_all_trails()
    for trail in trails:
        print(
            f"Trail: {trail.name} | Location: {trail.location} | Length: {trail.miles_long} | ID: {trail.id}"
        )


def add_runner():
    pass


if __name__ == "__main__":
    display_welcome()
    while True:
        display_main_menu()
        choice = input()
        if choice == "1":
            display_all_runners()
        elif choice == "2":
            add_runner()
        elif choice == "3":
            print_goodbye()
        else:
            invalid_choice()
display_main_menu()
