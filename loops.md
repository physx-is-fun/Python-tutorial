# Python - Loops

In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on. There may be a situation when you need to execute a block of code several number of times. Programming languages provide various control structures that allow for more complicated execution paths. A loop statement allows us to execute a statement or group of statements multiple times. Python programming language provides following types of loops to handle looping requirements.

    while loop (Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.)
    for loop (Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.)
    nested loops (You can use one or more loop inside any another while, for or do..while loop.)

## Python while Loop Statements

A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true. The syntax of a while loop in Python programming language is:

    while expression:
        statement(s)

Here, statement(s) may be a single statement or a block of statements. The condition may be any expression, and true is any non-zero value. The loop iterates while the condition is true. When the condition becomes false, program control passes to the line immediately following the loop. In Python, all the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements. Here, key point of the while loop is that the loop might not ever run. When the condition is tested and the result is false, the loop body will be skipped and the first statement after the while loop will be executed.

## Using else Statement with While Loop

    If the else statement is used with a while loop, the else statement is executed when the condition becomes false. 

Python supports to have an else statement associated with a loop statement.

## Python for Loop Statements

It has the ability to iterate over the items of any sequence, such as a list or a string. Syntax:

    for iterating_var in sequence:
        statements(s)

If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable iterating_var. Next, the statements block is executed. Each item in the list is assigned to iterating_var, and the statement(s) block is executed until the entire sequence is exhausted.

## Using else Statement with For Loop

Python supports to have an else statement associated with a loop statement.

    If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

## Python nested loops

Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept.

    for iterating_var in sequence:
        for iterating_var in sequence:
            statements(s)
        statements(s)

The syntax for a nested while loop statement in Python programming language is as follows:

    while expression:
        while expression:
            statement(s)
        statement(s)

A final note on loop nesting is that you can put any type of loop inside of any other type of loop.

## Loop Control Statements

Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements. Click the following links to check their detail. Let us go through the loop control statements briefly.

    break statement (Terminates the loop statement and transfers execution to the statement immediately following the loop.)
    continue statement (Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.)
    pass statement (The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.)

## Python break statement

It terminates the current loop and resumes execution at the next statement, just like the traditional break statement in C. The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops. If you are using nested loops, the break statement stops the execution of the innermost loop and start executing the next line of code after the block. The syntax for a break statement in Python is as follows:

    break

## Python continue statement

It returns the control to the beginning of the while loop.. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop. The continue statement can be used in both while and for loops. Syntax:

    continue

## Python pass Statement

It is used when a statement is required syntactically but you do not want any command or code to execute. The pass statement is a null operation; nothing happens when it executes.

## Bibliography

Python - Loops. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_loops.htm