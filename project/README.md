## Project

## Description

For this project, either work with a partner or by yourself.

This is a multi-stage project and thus you will have some class time to work on it.

You need to:
import all of the libraries you are going to use
final a database that is useable as research IE at least 100 tuples and a reasonable conclusion
use python for all of your programming
also turn in a preliminary 'plan' 

The turn-ins are as follows:

Pick a data science or statistics algorithm to determine something about a real dataset you found in the world. This can be anything from saying the average is off, like with measuring global temperatures worldwide, or classifying data to either predict a yes or no or to classify it in more categories. (naive bayes, null hypothesis test)

Have a proposal, one page maximum, that covers the following:
What data are you analyzing?
What algorithm are you using and why?
What are you hoping to learn?
Where did you get the data, does it seem accurate?

Next, convert the data into a .csv file if you have not already done so, turn in with code
Write the python program to process your information and print out a conclusion
How accurate was your algorithm by %? If you use a z-test, how close was the actual mean to the calculated one? Was it bigger, smaller, different?
Write a small, once again 1 page conclusion answering the following:
Was your test accurate?
What could have altered the results?
Did it work or do we need to run a different test or get more data?

And finally, make a separate .py file and write a function that does exactly what the imported functions do IE Naive Bayes or z-test. Run the test again and in your conclusions answer the following:
Were the results between the written functions and the imported functions the same? Different? Why?
Why are libraries so important but also dangerous?
Extrapolate this to AI, sure we can get the correct answer but who interprets the data? Who knows its right? The movement of software developers to designers is underway, how can we use what we know to manipulate the data? 

## Data

[Spambase Data Set](https://archive.ics.uci.edu/dataset/94/spambase)

4601 emails, with 1813 spam emails (39.4%). The data set has 58 features, 57 of them for identifying spam emails and 1 for the label.

We are lucky to have data that has NO MISSING VALUES. Which is rare in the real world.

This allows to train a model for easy classification of spam emails.

## Approach

We are going to use a neural network algorithm to determine if an email is spam or not. As of our
current plan. The network will consist of multiple layers: an input layer that receives the
attributes as features, two hidden layers with ReLu activation functions, and an output layer a
with a soft max activation function for binary classification. The model will be trained using
categorical cross-entropy loss using Keras.

## Setup (Assuming vs code)

1.  Open the CS3080ClassCode folder in VS Code
2.  cd into the project folder assuming you are in the CS3080ClassCode folder (cd project)
3.  run `pip install -r requirements.txt`
4.  run `python neural_network_with_3p_libraries.py` to run the neural network with 3rd party libraries