# Simple-Zoo-Simulator

Assignment for Programming and Problem Solving I done in 2021 with Journal, Pseudocode and Python code by Amanda W.

The Simple Zoo Simulator is a program that simulates a simple zoo for fun and profit.

You have a list of animals, which each generate "income" according to their name length (as everyone knows, longeranimal names mean higher profit at a zoo... 
but they cost more to buy). Each day when you wait, arandom "luck" value between 0-100 is generated, which determines how much income the animals generate, 
but if you are unlucky, a random animal will escape. You can buy new animals with theincome you make, but you cannot have more than one of each animal (name).
The program starts with a welcome, some instructions and three animals. 
Then there's a repeating menu with the following four options:

• (W)ait
  
This simulates a day starting with luck between 0 and 100. If you get less than 33 (thinkabout constants) then a random animal from your list will escape 
and be deleted from the list. Animals are deleted before any income calculations.
Each animal generates an amount of income according to the formula:luck / 100 * name lengthe.g., if luck is 70, a "Zebra" animal (5 characters)
would generate 0.7 * 5 = 3.5 as aninteger, so an income of 3.
  
• (D)isplay animals 
      
This simply displays the animals in your zoo (or “No animals.” if you have none).• (A)dd new animalo You can only add animals you can afford.
You can have infinite animals but you cannothave any with the same name as existing animals.
New animal names cannot be empty, so error-check and repeat for empty names.When you input an animal, the name should be converted to title case (using Python's.title()
string method), so if the user enters "HEARTy bass", it will become "HeartyBass" (and would cost 11 income).When you add an animal, 
the name length (cost) is deducted from your total income.
      
• (Q)uit
      
This will end the main menu (follow the menu pattern!) and show the final details
including the animals, the number of days simulated, the number of animals and theamount of income. Animals in the list should always be in alphabetical sorted order,
but only sort when you need to(when the list has changed).
