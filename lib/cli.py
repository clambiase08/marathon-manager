from helpers import *
from prompt_toolkit import prompt
from rich import print
from pick import pick

## Constants
MAX_WORKOUTS = 40
MAX_WORKOUT_DIFF = 2
MIN_MILES = 50

## Print functions

def display_welcome():
    print(
        "Welcome to Marathon Manager! Your premiere running training program simulator. Have fun :runner:"
    )

def invalid_choice():
    print("Invalid choice. Nice try. Please choose again!")

def print_make_selection():
    title = "Please make a selection:"
    return title


def print_goodbye():
    print(f"Thank you for using the Marathon Manager. Happy Trails! {goodbye_image}")

def press_enter():
    input("Press Enter to continue...")


goodbye_image = """
                _
              _( }
    -=   _  <<  |
        `.\__/`/\\
  -=      '--'\\  `
       -=     //
              \)
   """

## Main Menu functions

def display_main_menu():
    title = print_make_selection()
    options = ["View all runners", "Add yourself to our running training program", "Exit App"]
    option, index = pick(options, title, indicator="→")
    return option, index

def display_all_runners():
    runners = get_all_runners()
    for runner in runners:
        print_runner_info(runner)
    press_enter()
    title = print_make_selection()
    options = ["View a ranking of all runners", "See runner stats", "Choose a runner to run with", "Main menu"]
    option, index = pick(options, title, indicator="→")
    choice = index
    if choice == 0:
        print_all_ranked_runners()
    elif choice == 1:
        choose_runner_by_id()
    elif choice == 2:
        choose_runner_for_workout()
    elif choice == 3:
        return
    else:
        invalid_choice()

def add_runner():
    print("Please enter runner name (first and last): ")
    runner = input()
    if runner:
        add_runner_to_db(runner)
        print(f"Added {runner} to training program. Time to run!")
        press_enter()
    else:
        invalid_choice()

## View All Runners Sub Menu

def get_runners_ranking():
    runners = get_all_runners()
    sorted_runners = sorted(runners, key=lambda x: x.miles_run, reverse=True)
    return sorted_runners

def print_all_ranked_runners():
    runners = get_runners_ranking()
    for rank, runner in enumerate(runners, start=1):
        runner_info = return_runner_info(runner)
        if rank == 1:
            emoji = "🥇"
        elif rank == 2:
            emoji = "🥈"
        elif rank == 3:
            emoji = "🥉"
        else:
            emoji = ""
        print(f"{runner_info} | Rank: {rank} {emoji}")
    press_enter()

def return_runner_info(runner):
    return f"Runner: {runner.name} | Miles Run: {runner.miles_run} | ID: {runner.id}"

def choose_runner_by_id():
    runner = get_runner_by_id_prompt()
    if runner:
        print_runner_info(runner)
        print_runner_rank(runner)
        press_enter()
    else:
        invalid_choice()

def get_runner_by_id_prompt():
    search_id = input("Enter the ID of the runner you'd like to choose: ")
    runner = find_runner_by_id(search_id)
    return runner

def print_runner_info(runner):
    runner_info = return_runner_info(runner)
    print(runner_info)

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

def choose_runner_for_workout():
    runner = get_runner_by_id_prompt()
    if runner:
        print_runner_info(runner)
        print(
            f"Congrats! you have chosen {runner.name}. Hope you know what you are doing..."
        )
        print_workout_details(runner)
        press_enter() 
        display_runner_stats_menu(runner)
    else:
        invalid_choice()
    

def display_runner_stats_menu(runner):
    title = print_make_selection()
    options = ["See a list of trails to choose from", "Back to all runners", "Main menu"]
    option, index = pick(options, title, indicator="→")
    choice = index
    handle_runner_choice(choice, runner)

## Choose Trail Sub Menu

def handle_runner_choice(choice, runner):
    if choice == 0:
        display_all_trails(runner)
    elif choice == 1:
        display_all_runners()
    elif choice == 2:
        pass
    else:
        invalid_choice()
        press_enter()

def display_all_trails(runner):
    trails = get_all_trails()
    for trail in trails:
        print(
            f"Trail: {trail.name} | Location: {trail.location} | Length: {trail.miles_long} | ID: {trail.id}"
        )
    press_enter()
    title = print_make_selection()
    options = ["Choose a trail on which to run today's workout", "Back to all runners"]
    option, index = pick(options, title, indicator="→")
    choice = index
    if choice == 0:
        get_trail_by_id(runner)
    elif choice == 1:
        display_all_runners()
    else:
        invalid_choice()
        press_enter()

## Display Trails Sub Menu

def get_trail_by_id(runner):
    search_id = input("Enter the ID of the trail you'd like to choose: ")
    trail = find_trail_by_id(search_id)
    if trail:
        workout = get_workout_details(runner)
        if workout:
            print(
                f"You have chosen {trail.name}. Are you sure? {runner.name} has run {runner.miles_run} miles so far and today's workout is {workout.miles_long} miles."
            )
            press_enter()
            handle_trail_choice(trail, runner, workout)
    else:
        invalid_choice()

def handle_trail_choice(trail, runner, workout):
    title = print_make_selection()
    options = ["Yes! Let's DO THIS THING", "Hmm... on second thought, can I see those trails again?", "Main Menu"]
    option, index = pick(options, title, indicator="→")
    choice = index
    if choice == 0:
        handle_trail_run(trail, runner, workout)
    elif choice == 1:
        display_all_trails(runner)
    elif choice ==2:
        display_main_menu()
    else:
        invalid_choice()

def handle_trail_run(trail, runner, workout):
    if runner.miles_run < MIN_MILES and (trail.miles_long - workout.miles_long) > MAX_WORKOUT_DIFF:
        set_runner_to_zero(runner)
        print(
            f"Oooo yikes. {runner.name} has fainted and their miles have been set back to zero. Slow and steady wins the race!"
        )
    elif workout.miles_long <= trail.miles_long:
        updated_runner = update_runner_miles(runner, trail)
        print(
            f"Congratulations! {updated_runner.name} has now run a total of {updated_runner.miles_run} miles and completed a total of {workout.order} workouts."
        )
        if workout.order == MAX_WORKOUTS:
            print(
                "Congratulations! You are ready for the marathon. Time to carb load :)"
            )
        else:
            print(f"Only {40- (workout.order)} more workouts to go!")
    else:
        print(
            "Silly goose! You can't run a workout that's longer than the trail. Try again please."
        )
        press_enter()
        handle_trail_choice(trail, runner, workout)
    press_enter()

## Main CLI

if __name__ == "__main__":
    display_welcome()
    press_enter()
    while True:
        option, index = display_main_menu()
        choice = index
        if choice == 0:
            display_all_runners()
        elif choice == 1:
            add_runner()
        elif choice == 2:
            print_goodbye()
            break
        else:
            invalid_choice()
        
