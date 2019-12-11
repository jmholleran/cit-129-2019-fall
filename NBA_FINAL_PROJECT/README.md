# Joe Holleran		Python 2		Final Project		Fall 2019

## Python Program to Simulate NBA Games in order to Evaluate Simulation Probabilities in Comparison to Offered Moneyline Probabilities

The program will scrape NBA daily matchups and NBA team statistics from basketball-reference.com.  

The program displays a 'dashboard' like output to view each team's prior game results and then allows the user to enter the Moneylines for the matchup.

The program then displays the Moneylines implied probability and outputs the simulation probabilities.  The simulation is a Monte Carlo simulation of the matchup run 10,000 times.

The Kelly Criterion is displayed which takes in the decimal odds (based on moneyline) and the simulation probability.  The Kelly Criterion allows a bettor to determine
if the payoff is worth risk (chance of losing vs. chance of winning).

The user is then allowed to 'adjust' the probability to display a new Kelly Criterion output.  The user could determine a Bayesian probability or mathematical expectation
from prior results of the simulation.

The user is finally asked if they would like to output the data to an Excel file.

## Other Options

The program will output all of the NBA matchups today

The program allows the user to input their own matchup and display an analysis described above.





