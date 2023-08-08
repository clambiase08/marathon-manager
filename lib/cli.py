from helpers import *
from prompt_toolkit import prompt
from rich import print

# Tasks:
# [x] 1. Show all the runners
# [x] 2. Show a runner's details
# [x]   - including name, id, miles run, and current workout
# [] 3. Show all the workouts -- maybe?
# [x] 4. Show all the trails
# [x] 5. Choose a runner to run with
# [x] 6. Choose a trail for that runner to run
# [] 7. After the runner has finished the workout, show new runner stats
# [] 8. See the runners ranked by miles run with medals for the top 3
# [] 9. Assign yourself as a new runner
# [] 10. Have a runner complete all the workouts and show a message indicating they are ready for the marathon
# [] 11. Write some fun welcome and goodbye messages
# [] 12. Add styling and slow type


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
    print("1. View a ranking of all runners")
    print("2. See runner stats")
    print("3. Choose a runner to run with")
    print("4. Main menu")
    choice = input()
    if choice == "1":
        print_all_ranked_runners()
    elif choice == "2":
        choose_runner_by_id()
    elif choice == "3":
        choose_runner_for_workout()
    elif choice == "4":
        display_main_menu()
    else:
        invalid_choice()


def print_all_ranked_runners():
    runners = get_runners_ranking()
    for runner in runners:
        print_runner_info(runner)


def print_runner_info(runner):
    print(f"Runner: {runner.name} | Miles Run: {runner.miles_run} | ID: {runner.id}")


def print_runner_rank(runner):
    runner_ranking = get_runners_ranking()
    chosen_runner_rank = None
    for rank, r in enumerate(runner_ranking, start=1):
        if r == runner:
            chosen_runner_rank = rank
            break
    if chosen_runner_rank is not None:
        if chosen_runner_rank <= 10:
            print(f"{runner.name} is ranked #{chosen_runner_rank}. Top 10 baby!")
        else:
            print(
                f"{runner.name} is ranked #{chosen_runner_rank}. Better hit the pavement!"
            )
    else:
        invalid_choice()


def get_runner_by_id_prompt():
    search_id = input("Enter the ID of the runner you'd like to choose: ")
    runner = find_runner_by_id(search_id)
    return runner


def choose_runner_by_id():
    runner = get_runner_by_id_prompt()
    if runner:
        print_runner_info(runner)
        print_runner_rank(runner)
    else:
        invalid_choice()


def choose_runner_for_workout():
    runner = get_runner_by_id_prompt()
    if runner:
        print_runner_info(runner)
        print(
            f"Congrats! you have chosen {runner.name}. Hope you know what you are doing..."
        )
        print_workout_details(runner)
        display_runner_stats_menu(runner)
    else:
        invalid_choice()


def display_runner_stats_menu(runner):
    print_make_selection()
    print("1. See a list of trails to choose from")
    print("2. Back to all runners")
    print("3. Main menu")
    choice = input()
    handle_runner_choice(choice, runner)


def handle_runner_choice(choice, runner):
    if choice == "1":
        display_all_trails(runner)
    elif choice == "2":
        display_all_runners()
    elif choice == "3":
        display_main_menu()
    else:
        invalid_choice()


def handle_trail_run():
    pass


def get_trail_by_id(runner):
    search_id = input("Enter the ID of the trail you'd like to choose: ")
    trail = find_trail_by_id(search_id)
    if trail:
        workout = get_workout_details(runner)
        if workout:
            print(
                f"You have chosen {trail.name}. Are you sure? {runner.name} has run {runner.miles_run} miles so far and today's workout is {workout.miles_long} miles."
            )
            print_make_selection()
            print("1. Yes! Let's DO THIS THING")
            print("2. Hmm... on second thought, can I see those trails again?")
            choice = input()
            if choice == "1":
                handle_trail_run()
            elif choice == "2":
                display_all_trails(runner)
            else:
                invalid_choice()
    else:
        invalid_choice()


def display_all_trails(runner):
    trails = get_all_trails()
    for trail in trails:
        print(
            f"Trail: {trail.name} | Location: {trail.location} | Length: {trail.miles_long} | ID: {trail.id}"
        )
    print_make_selection()
    print("1. Choose a trail on which to run today's workout")
    print("2. Back to all runners")
    print("3. Main Menu")
    choice = input()
    if choice == "1":
        get_trail_by_id(runner)
    elif choice == "2":
        display_all_runners()
    elif choice == "3":
        display_main_menu()
    else:
        invalid_choice()


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
            break
        else:
            invalid_choice()
