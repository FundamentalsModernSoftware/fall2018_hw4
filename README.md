Programming Assignment 4
================================

**Fundamentals of Modern Software**  
**Fall 2018**  
**Due 11:59 PM, Wednesday October 3**

Introduction
------------


**REMINDERS**

1. **When you are done, be sure to submit your work.**
2. **You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.**
3. **Be sure to test your programs thoroughly. We will.**
4. **Your output should match the output in the samples EXACTLY, to the letter.**


babyNames.py
--------

The Social Security Administration maintains an annual list of all new baby names. The lists are available for download from <https://www.ssa.gov/oact/babynames/limits.html>; we have given you the national year-by-year lists in the `babies` subdirectory. The file `NationalReadMe.pdf` in that directory documents the format used by the SSA. Write a program that identifies the 100 most commonly used baby names from 1880 through 2016 (i.e, the names given to the most total babies). 

Your program should save the names to an output JSON file, `popularNames.json`, which lists the top 100 names in descending order of popularity.  The file should be formatted to match the following (with different names and counts, of course):

    [{"name": "mario", "count": 500000}, {"name": "luigi", "count": 400000}, {"name": "wario", "count": 1}]


**We have implemented for you the part of the code that gets a list of filnames, so you do not need to solve that portion of the task.**


queries.py
--------

Using the fmsdb package and the zipcodes database, write the following functions. **Your functions should never attempt to read the zipcodes CSV or the database schema. All access to the data must be through the functions defined in `fmsdb.py`.**

`state_of(zipcode)`: Returns the name of the state in which a zipcode is located.

`northernmost(state)`: Returns the northernmost zipcode in `state`.

`zipcodes_in_city(city_name)`: Returns the total number of zip codes in the place `city_name`.

`states_by_size()`: Returns a list of state names, sorted in order from the state containing the fewest zip codes to the state containing the most. _This cannot be done solely using the FMSDB interface. You will need to embed your calls to FMSDB inside some additional Python code._

