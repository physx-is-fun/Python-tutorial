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

If the else statement is used with a while loop, the else statement is executed when the condition becomes false. Python supports to have an else statement associated with a loop statement.

## Bibliography

Python - Loops. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_loops.htm