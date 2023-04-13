## Making_the_NBA
# Objective
Creating a model to predict whether a college basketball player will be drafted into the NBA.  We will be using data from drafted and undrafted players. Using machine learning we will perform logistical regression model and/or neural networks that will take and compile all the college data from 2009 to 2021 to predict which player will go to the NBA.   

# Hypothesis
We predict that the higher the average field goal percentage the more likely to be drafted into the NBA.

# Data Source
Kaggle - https://www.kaggle.com/datasets/adityak2003/college-basketball-players-20092021

# Overview
1. Clean the data
-dropped  columns with a high percentage of nulls.......blah
2. Create visualizations in Tableau
-Discovered that the position, conference, average offensive rebounding, average assist, or last year in college did not have substancial differences in the drafted versus undrafted players
-The School attended, average defensive rebounds & average points did have a substantial difference in the drafted versus undrafted players.    
-88% of the drafted players are between 6 & 7 feet tall.  
3. Create a machine learning model to predict if a player will be drafted in the NBA

# Technologies
Mongo Database

Python

Jupyter Notebook

Tableau --  Emily & Princeton 

## The following stats made a substantial difference depending on drafted vs undrafted players
![NBA Difference.png](https://github.com/mleroseandrews/Making_the_NBA/blob/Tableau/NBA%20Difference.png)
- https://public.tableau.com/app/profile/emily.andrews6944/viz/NBADashboardDifference/Dashboard2?publish=yes
## The following stats did not make a substantial difference depending on drafted vs undrafted players
![NBA No Difference.png](https://github.com/mleroseandrews/Making_the_NBA/blob/Tableau/NBA%20No%20Difference.png)
-https://public.tableau.com/app/profile/emily.andrews6944/viz/NBADashboardNoDifference/Dashboard1?publish=yes


