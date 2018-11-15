# Assignment: Guessing Game
You're given a simple working guessing game in which the computer chooses a number at random and the user is invited to try and guess it. The game has a few tuneable parameters that allow players to change the number of starting lives, the difficulty increase with each level, and the starting range from which the computer chooses the secret number.

Your assignment is to add logic that allows the computer to give hints after each incorrect guess:
1. In the initialization section of the game loop, create a variable `hints` with an intial value of `True`
2. In the guessing loop, add code that informs the user whether her incorrect guess is too high or too low.
3. The code from the previous step should run __only__ if `hints` is set to `True`
