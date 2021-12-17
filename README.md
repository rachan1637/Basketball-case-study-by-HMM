# Fall: Statistical Methods and Analyses in Sports

In this fall term, we start a reading course about sports analytics. We read through the textbook "Handbook of Statistical Methods and Analyses in Sports" from Chapter 9-12, and quickly go over the first 12 chapters of "Bayesian Data Analysis".

The notes could be found in [Reading Notes](https://github.com/rachan1637/basketballHMM/tree/main/Reading%20Course/Reading%20Notes).

Also, the project specifically focuses on the Chapter 12 of the HSMAS, about fitting the intensity surface for player's shots and typifying players based on the surface, is created in the last few weeks. 

The code for fitting the intensity surface is modified from the Github Repo [flecks](https://github.com/andymiller/flecks), contributed by one of the authors of the chapter, Andrew Miller.

However, the fitted surfaces are still problematic, since the intensity surface around the three point line is hard to converge. The current progress can still be viewed in the notebook [Project](https://github.com/rachan1637/basketballHMM/blob/main/Reading%20Course/Project.ipynb).

We might continue to make the fitting process work in the next few weeks. Besides, the next step of this interesting project will be discussed later.

# Summer: Detecting Basketball Events by HMM

The goal of the case study is to use HMM for modelling basketball data and provide useful insights, advised by Professor Vianey Leos Barajas.

The textbook we use is "Hidden Markov Models for Time Series: An Introduction Using R".

## Ongoing Progress 

Identify the 3pt shooting together with long pass. Consider the dribble, and other complex basketball events.

## Completed Progress

### June-July

(a) Idetify the long pass and 3pt shooting.

The data is obtained from [this repo](https://github.com/sealneaward/nba-movement-data), Credit: [@sealneaward](https://github.com/sealneaward) and [@neilmj](https://github.com/neilmj/BasketballData)

The additional preprocessing codes are written in python ([preprocess data](https://github.com/rachan1637/Basketball-case-study-by-HMM/tree/main/Basketball/data_preprocess)), including swithcing the player name and creating speed.

The analysis part are written in R and R Studio, the pdf file is here: [Identify long pass and 3pt shooting](https://github.com/rachan1637/Basketball-case-study-by-HMM/blob/main/Basketball/basketball2.pdf).

Two gif plots are made for the identification respectively, [pass](https://github.com/rachan1637/Basketball-case-study-by-HMM/blob/main/Basketball/event1_passing.gif) and [3pt shooting](https://github.com/rachan1637/Basketball-case-study-by-HMM/blob/main/Basketball/event28_3pt.gif).

<br>

(b) Identify the layup following other's case.

The codes are written in R and R Studio, the pdf file is in the same location: [Identify the Layup by HMM](https://github.com/rachan1637/Basketball-case-study-by-HMM/blob/main/Basketball/basketball.pdf).

Reference: [Tagging Basketball Events with HMM in stan](https://mc-stan.org/users/documentation/case-studies/bball-hmm.html#pre-process-data)

<br>

(c) Writing codes for simulating a simple basketball game (leading or falling behind, and what are the strategies under these cases) by HMM.

The codes are written in R and R Studio [Simple Basketball Game Simulation by HMM](https://github.com/rachan1637/Basketball-case-study-by-HMM/blob/main/Practice%20Code/Simulating-HMM-basketball.Rmd), and the report can be found [here](https://github.com/rachan1637/Basketball-case-study-by-HMM/blob/main/Practice%20Code/Simulating-HMM-basketball.pdf).

### June 9th
End up reading the textbook chapter 1-5, and make notes for summarizing the key points in the textbook.  

The notes can be found in [HMM Notes](https://github.com/rachan1637/Basketball-case-study-by-HMM/tree/main/HMM%20Notes).
