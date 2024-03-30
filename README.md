# CS50P-Final-Project - MealPlanner
The Final Project of the CS50P online course. A command-line interface MealPlanner if you are indecisive of what to eat for each meal.

Video Demo &rarr; https://youtu.be/AEWFeAbsOu4?si=WX1bAUCEjkCUiUVJ

## Functionalities
- It randomises and help you select the different kind of dishes for your meal time, whether is it for breakfast, lunch or dinner.
- Within each meal, there is also different kind of meal such as those with eggs or just meat or even both
- The last meal eaten will be recorded in the program so if the user's username exist in the program. This is to ensure that in the case the food is nice, and that the user forgotten what meal that they last eaten, the program will show up the name of the meal.

## Modules

1. `sys` Used to exit the program using sys.exit(). However, you can choose to modify the program and go with exit() if you want.

2. `random` Used to randomise the selection of the dishes for the different mealtimes so that it ensures that the user get a balance of the dishes and not eat the same dishes all the time.



## Installation
Use pip to install the package `sys` and `random`. Sys and random module should have come preinstalled with python. In case, somehow the modules are deleted or not installed, you can install with the commands below. 
1. `pip install sys`
2. `pip install random`

## Usage
To run the application, you will need to have [python](https://www.python.org/) install. Then follow the below command to run the python script.

```
$ python project.py
```

You then use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application for any issues or errors.

```
$ pytest test_project.py
```

The following code will soon be implemented with more functionalities to include personal dishes.

# Acknowledgements
Thank you for the CS50P Introduction to Programming course. The course is greatly produced with execellent explanation for each video by David Malan and his team. Thank you for the excellent problem sets 0-8 in helping to facilitate the learning process.
