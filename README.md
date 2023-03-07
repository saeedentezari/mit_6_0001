# [mit 6.0001: Introduction to Computer Science and Programming in Python](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjyj5eygMr9AhWMyqQKHYZDA-wQFnoECA0QAQ&url=https%3A%2F%2Focw.mit.edu%2Fcourses%2F6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016%2F&usg=AOvVaw0Ou2egTvV-U78H7xjzTSKd)

## [ps1](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/8cf75481d7047180c386de3e485bd050_MIT6_0001F16_ps1.pdf): Branching and Iteration, Bisection Search

Just a warm-up!

Using control flow in python, and formulating a computation solution to a problem. And also an exploration on bisection search.


## [ps2](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/d57834a8de13b1579b3e5274e520ea14_ps2.zip): String Manipulation, Guess and Check, Decomposition, Abstraction, Functions

A letter game called *Hangman* decomposited to its basic functions and implemented. It's an introduction to creating functions, as well as looping mechanisms.


## [ps3](): Dictionaries, Tuples, Lists, Aliasing, Mutability, Cloning, Testing and Debugging

A word game like *Scrabble* implemented. The main goals are to work with dictionaries, an understanding on mutability, writing a program by pseudocode, testing and debugging each function in creation.

A test file prepared as `test_ps3.py` to test each function in `ps3.py`.


## [ps4](): Recursion, Object Oriented Programming, Python Classes and Inheritance

This problem set has two parts:

1. Recursion: Solve the permutation problem by recursion in `ps4a.py` file.

2. OOP: Write two methods of encryption on text message, one by shift the letters in `ps4b.py`, and another by substitution in `ps4c.py`. Decryption also included.

---

`in_class_test.py` as its name says, is my test of functions and classes introduced in lecture videos. Such as:

* Recursive functions like *Towers of Hanoi*, *Palindrome*, and *Fibonacci* with/out memory.

* Order of growth of two bisection search methods, which are slightly different in implementation but have a big difference in runtime.<br>
Both of them are implemented in recursive fashion. The inefficient one copy! (by slicing `L[:mid]` or `L[mid:]`) each section of the searched list in each recursive step, but the efficient one just works with indices on the list to be searched.

* Sorting by *merge sort*, *bubble sort*, and *selection sort*.
