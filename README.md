# Advent of Code solutions and helpers

## Solutions
Not pretty, but the quickest solution I could hack together in python.

## run.py
The script takes care of 
* downloading the puzzle input
* prompts for the example input and solution
* runs the solution until it matches the expected example and then submits the solution
* creates a part 2 template based on the part 1 solution
* prompts for the second example solution
* runs and submits part 2 similar to part 1

## scoreboard.py
Is a small ascii scoreboard showing the scores for and until a given day.

## custom_leaderboard_userscript.js
This is a tampermonkey script for a changed browser leaderboard, it
* filters the leaderboard to only include active users (those with at least one star)
* displays the solution times
* allows ordering based on score, first star time, second star time and second star delta time
* allows to view the results of individual days as opposed to only the latest