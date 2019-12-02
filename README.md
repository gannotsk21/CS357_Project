# CS357_Project

CS357 Python Project

Algorithm for converting a Context Free Grammar to PDA
1. Create q_startState
2. Create q1, place $ on stack when transitioning from q_startState to q1 3. Create q_loop
4. Create a “petal” using each of the rules:
   1. Iterate backwards through each individual rule, pushing each variable to the stack
   2. Once the end of a rule is reached, return to q_loop and go to the next rule
5. Create a petal that pops each character off of the stack
6. Create q_accept, pop $ off the stack when transitioning from q_loop to q_accept

To run the program:
1. Add a an input file to the input folder
2. Add a CFG in proper format (see example input below)
3. Run *python3 grammer2PDA.py* in the terminal
4. Check the matching output file for the PDA

Example:

Input:

{\<A>, \<B>, \<C>}
  
{a, b}

\<A> :: a | \<B> a b | e 
  
\<B> :: a <C> b | \<C> a 
  
\<C> :: b <C> | b | a b \<C> 
  
{\<A>}
  

Output:
PDA:
q_startState -> q1 : e, e-> $ q1 -> q_loop : e, e-> \<A> q_loop:
e,\<A> ->a
  
|
e,\<A> ->b
e, e ->a
e, e ->\<B>
  
|
e,\<A> ->e
  
|
e,\<B> ->b
e, e ->\<C>
e, e ->a
  
|
e,\<B> ->a
e, e ->\<C>
  
|
e,\<C> ->\<C>
e, e ->b
  
|
e,\<C> ->b
  
|
e,\<C> ->\<C>
e, e ->b
e, e ->a
  
|
a, a -> e
b, b -> e

q_loop -> q_accept : $, $->e
