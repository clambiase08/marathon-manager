# Marathon Minder

## Summary

Marathon Manager is a CLI application marathon training plan simulator. A user can view a list of runners, add themselves as a runner to the program, and choose trails on which to run assigned workouts until they have completed the training program and are ready for the marathon. Careful, though, slow and steady wins the race!

---

## Requirements

- Python 3.x
- SQLAlchemy

---

## Installation

To start the program, the following commands must be run:

1. In the marathon-manager directory:

```console
pipenv install
pipenv shell
cd lib
```

2. In the lib directory:

```console
python seed.py
python cli.py
```

> **Note: Make sure you cd into the lib directory after you are in the shell
> otherwise the program will not execute properly.**

---

## Usage

Once the program is started, the user will press enter to see the main menu with the following choices:

- View all runners - view a list of runners with their names, total miles run, and IDs.
- Add yourself to our running training program - add a new runner by name to the existing runners. The new runner will start at 0 miles and have all the same options as the existing runners.
- Exit App - exit the application.

From the View all runners choice the user can then navigate through a series of submenus that allow the user to see the runner's stats, choose a trail to run on, see the list of trails, and execute a workout on a chosen trail.

After a runner has completed a run, their total miles run will increase by the length of their workout, and they'll move forward in the training program. After completing all workouts the user will see a message indicating that runner is ready for the marathon.

---

## Application Structure

### cli.py:

The main application file containing the command-line interface.

### helpers.py:

A set of helper functions to retrieve and update information from the database.

### models.py:

Contains the SQLAlchemy ORM models for the Runner, Workout, Trail, and Run classes.

### seed.py

Contains data seeding for the database.

Other files, such as alembic.ini, are related to database versioning and migrations.

---

## Additional Resources

This application also made use of Faker's python package and Pick's python library.

- [Faker](https://faker.readthedocs.io/en/master/)
- [Pick](https://pypi.org/project/pick/)

## Support

If you encounter any issues or have any questions regarding the Marathon Manager CLI, you can reach out to us through the following channels:

- [GitHub Issue Tracker](https://github.com/clambiase08/marathon-manager/issues)
- [Email](mailto:christina.lambiase@gmail.com)
