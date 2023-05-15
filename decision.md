# Decision making

Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions. Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome. You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise. Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value. Python programming language provides following types of decision making statements.

    if statements (An if statement consists of a boolean expression followed by one or more statements.)
    if...else statements (An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.)
    nested if statements (You can use one if or else if statement inside another if or else if statement(s).)

## Python IF Statement

It is similar to that of other languages. The if statement contains a logical expression using which data is compared and a decision is made based on the result of the comparison. Syntax:

    if expression:
        statement(s)

If the boolean expression evaluates to TRUE, then the block of statement(s) inside the if statement is executed. If boolean expression evaluates to FALSE, then the first set of code after the end of the if statement(s) is executed.

## Python IF...ELIF...ELSE Statements

An else statement can be combined with an if statement. An else statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value. The else statement is an optional statement and there could be at most only one else statement following if. Syntax:

    if expression:
        statement(s)
    else:
        statement(s)



## Bibliography

Python - Decision Making. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_decision_making.htm