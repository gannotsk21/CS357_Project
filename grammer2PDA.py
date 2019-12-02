### Converts a context free grammar to a PDA ###
### Polina Gannotskaya and Devin Smith       ###

import os
import subprocess
import sys
import string
import re

if len(sys.argv) > 1:
        inputdir = sys.argv[1]
else:
    inputdir = "inputs"

if not os.path.isdir(inputdir):
    print("Invalid input directory", inputdir)
    exit(1)
    

##############################################################
# readInput:
# Reads the input file and separates the rules
##############################################################
def readInput(input):
    with open(inputdir + "/" + input + ".txt", "r") as file:
       lines = [line.strip() for line in file]

       # checks to see if file is empty
       if not lines:
           print("Invalid: empty file - ", input)
           exit(1)
       # check to see if variables is in correct format
       var = list(map(str.strip, [lines[0][1:-1].split(",")][0]))
       lines.remove(lines[0])

       # checks to see if list of var is empty
       if not var:
           print("Invalid: empty variables state")
           exit(1)
       # TODO:check to see if alphabet is in correct format
       alphabet = list(lines[0][1:-1].split(","))
       lines.remove(lines[0])

       # checks to see if alphabet is empty
       if not alphabet:
           print("Invalid: empty alphabet state")
           exit(1)
       x = -1
       # check to see if acceptState is in correct format
       acceptState = []
       for aLine in lines:
            if (aLine[0] == '{'):
               acceptState.append(aLine[1:-1].split())
               acceptState = acceptState[0]
               lines.remove(aLine)

       # checks to see if acceptState is empty
       if not acceptState:
           print("Invalid: accept state")
           exit(1)
        
       # check to see if rules are in correct format
       rules = []
       y = len(var)
       for rule in lines:
           for x in range(0, y):
               if(rule[0:3] == var[x]):
                   rules.append(rule)
                   var[x] = var[x][1]

       # checks to see if rules is empty
       if not rules:
           print("Invalid: no rules")
           exit(1)

       startState = "<" + var[0] + ">"
       print("start state: ", startState)
       totalStates = []
       totalStates.append("q_accept")
       totalStates.append("q_loop")
       print("total states: ",totalStates)
       print("the alphabet", alphabet)
    
       gamma = alphabet+ var
       gamma.append("$")
       print("gamma ", gamma)
       print("delta:")
       print("accept state: ", acceptState)
       return alphabet, startState, rules

##############################################################
# createPDA:
# creates a PDA using the rules
############################################################## 
def createPDA(alphabet, startState, rules, numInput):
    #splitting the rules up
    delta = []
    #create start state, q1, and q_loop
    delta.append("q_startState -> q1 : e, e-> $")
    delta.append("q1 -> q_loop : e, e-> "+ startState)

    #create each petal 
    delta.append("q_loop:")
    for petal in rules:    
        readingIn = petal[0:4]
        print(readingIn)
        petal = petal[6:len(petal)]
        petal = petal.split("|")
        x = len(petal)
        for y in range(0, x):
            petal[y] = petal[y].split()
            petal[y].reverse()
            delta.append("e,"+ readingIn + "->" + petal[y][0])
            for p in range(1, len(petal[y])):
                delta.append("e, e ->" + petal[y][p])
            delta.append("|")
               
        #create petal to pop off the stack        
    for alph in range(0, len(alphabet), 1):
        delta.append(alphabet[alph] +", "+alphabet[alph]+" -> e")
        
    #create q_accept   
    delta.append("q_loop -> q_accept : $, $->e")

    #write to file
    createOutputFile(delta, numInput)
              
##############################################################
# createOutputFile:
# writes the PDA (delta) to a file named 'output.txt'
##############################################################      
def createOutputFile(delta, numInput):
    numInput = numInput[5:]
    with open('output'+str(numInput)+'.txt', "w+") as output:
        output.write("PDA:\r\n")
        for i in range(0, len(delta), 1):                  
            output.write(str(delta[i]))
            output.write("\r\n")
    output.close()  
       
       

for file in os.listdir(inputdir):
    # check if this is a file
    if not os.path.isfile(inputdir + "/" + file):
        continue
    # check file extension 
    if not file.endswith(".txt"):
        continue
    input = file[:-4] #strips off extension
    alphabet, startState, rules = readInput(input)
    createPDA(alphabet, startState, rules, input)
    
