# CSC160_L8_Create <br>
You have been tasked with creating a Python program that allows two users to have a creature battle. But first, a few quick notes: <br>
-Your assignment should be completed in IDLE on your machine, not in GitHub. <br>
-You will only be using GitHub to get the URL for your repository. That is the URL in the address bar right now! <br>
---Don't worry right now if those terms seem unfamiliar. We will learn them in time! Just know that you do not need to leave this page to get started. <br>

The first thing that you should do is reference the [Submitting an Assignment using Github](https://otc.instructure.com/courses/50195/files/8233081?wrap=1) document. This will walk you through the process of ensuring that Git is installed on your computer and that you can download your assignment. Once you have completed step 3 in the instruction, you will be ready to begin programming. Please use the below instructions as a point of reference. <br>

To begin the assignment, open the Create8.py file in IDLE. <br>
There is no example output for this file. I encourage you to engage with your team creatively to make a suitable output <br>
Your completed program should reflect the following: <br>

# Group Assignment <br>
-This is a group assignment, ensure that you are working with your group to meet the objectives. <br>
-Decide on one person, and submit their repository link to Canvas for grading. <br>
-All team members will receieve the same base grade with adjustments made for individual performance <br>
-You can see who your team members are in Canvas, or on Microsoft Teams. <br>
---In Canvas, go to "People" and look in the Hangman Groups.

# Program Description <br>
-This program is a very small video game where two users can play together. Each will be given the opportunity to choose a creature and battle each other. <br>

# Program Flow <br>
-Player one is presented with the creatures that they are able to choose from <br>
-Player two is presented with the creates that they are able to choose from (cannot choose same as P1) <br>
-Each player will take turn choosing moves for their creature to use until the opposing creature is knocked out <br>
-Players have the option to play again if they would like <br>

# Technical Requirements
-Players must be given a choice of six creatures, each with a different speciality and name <br>
--Speciality will be determined by stats. <br>

-Each creature has four stats <br>
--Attack: Determines how strong a move is <br>
--Defence: Determines how much the creature will resist an opposing move <br>
--Speed: Determines how fast the creature can move <br>
--HP (Health Points): When health points reach 0, the creature is knocked out <br>

-Each creature should have it's stats randomized within a certain range <br>
--Instead of assigning a static stat value for each moster each time the program is run, a random value should be given <br>
--This random value will be detailed further when discussing specialty <br>

-Below are the stat spreads/specialties your creatures should utilize <br>
--Tanky     (HP: High,    Attack: Medium, Defence: High,    Speed: Low) <br>
--Quick     (HP: Medium,  Attack: Low,    Defence: Medium,  Speed: High) <br>
--Fragile   (HP: Low,     Attack: High,   Defence: Low,     Speed: High) <br>
--Balanced  (HP: Medium,  Attack: Medium, Defence: Medium,  Speed: Medium) <br>
--Aggro     (HP: High,    Attack: High,   Defence: Low,     Speed: Medium) <br>
--Bully     (HP: Low,     Attack: Medium, Defence: High,    Speed: High) <br>

-Each of the above stats should be a number value tied to an object. The number value should be randomly generated within a range. <br>
--You get to decide what the number range is for each category (low, medium, high) <br>

-You need to program no fewer than 16 unique moves for your creatures to learn. <br>
--Each creature can know a maximum of three moves. This means that some moves can be repeated across monsters <br>
--Each move should have a unique name and effect <br>
--Example move: <br>
[Dragon Slam] <br>
-Description: Does high damage to the opponen, but the user must skip the next turn <br>
-Programming: Move has 80 base-power. Enemy HP is reduced upon use, next turn for user is skipped <br>

-All moves and effects should be programmed into individual functions <br>
--Calculate damage dealt using a formula of your own creation. The required varaibles for the formula are: <br>
---Attacking creature's attack stat <br>
---Defencing creature's defence stat <br>
---Attacking creature's move's base power <br>
--The result of your formula should be subtracted from the defending creature's HP <br>

-The program will prompt users to go again or end once a creature reaches 0 HP <br>

-There is a lot to do here, but if you divide the tasks amongst your group and plan accordingly you will be succesful! <br>

-Be sure to give your users the following options: <br>
--Allow user to examine the moves of each creature before selecting them <br>
--Allow the user to check their current stats during a batte, as well as their move descriptions and opponents stats <br>

-Please see the rubric in Canvas for grading criteria 
