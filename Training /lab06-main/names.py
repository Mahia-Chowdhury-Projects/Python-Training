# A collection of functions for analyzing and visualizing the popularity 
# of names over time. 

"""
This module provides a number of functions for analyzing name popularity.
"""

import matplotlib.pyplot as plt

def trim(line):
    """Removes the final newline from a string, if it exists.
    
    >>> trim("Hello there!\\n")  # ignore the extra backslash (it is required by doctests to express newlines) :(
    'Hello there!'
    >>> trim("Hello there!!")
    'Hello there!!'
    >>> trim("")
    ''
    """
    if len(line) > 0 and line[-1] == "\n":
        line = line[:-1]
    return line


def split(comma_separated_str):
    """Splits a comma-separated string into a list of substrings.
    
    For example, the string "mark,lida,rohit" would be split into
    the list of substrings ["mark", "lida", "rohit"]

    >>> split('a,b,c,d')
    ['a', 'b', 'c', 'd']
    >>> split('alpha,bravo,charlie')
    ['alpha', 'bravo', 'charlie']
    >>> split("csci134")
    ['csci134']
    """
    values = [] # initialize a list to store all values encountered
    current_value = ""

    # add items to the list until we run out of characters
    for character in comma_separated_str:

        # add a finished item to the list every time we encounter a comma
        # otherwise keep adding on to the item
        if character == ",":
            values = values + [current_value]
            current_value = ""
        else:
            current_value = current_value + character
    
    # check to add the final item in the string, if it exists
    if current_value != "":
        values = values + [current_value]

    return values

def read_names(filename):
    """
    This function takes the name of a CSV filename (string) containing name
    data and creates a dictionary of dictionaries.  The "outer" dictionary
    (year_db) maps the integer year (up to 2021) to "inner" dictionaries (name_db). 
    Each "inner" dictionary maps a string name to integer totals for a specific 
    year. Note that if multiple entries exist for a name in a given year (such as 
    an entry for the same name as both M and F), the totals for the name should 
    be *summed* in the dictionary. 
    Snippet from CSV for reference:
    year,name,sex,total
    2021,Emily,F,6541
    2021,Emilyn,F,37
    2021,Emilynn,F,14
    2021,Emilyrose,F,10
    2021,Emilya,F,7
    2021,Emily,M,6
    >>> db = read_names("data/namesDataAll.csv")
    >>> db[2021]["Emily"]
    6547
    >>> db[1880]["Emily"]
    210
    >>> 1900 in db
    True
    >>> 1600 in db
    False
    >>> len(db[1880])
    1889
    """
    year_db = dict()
    with open(filename) as reader: 
        for line in reader: 
            new_line = split(trim(line))
            year = int(new_line[0])
            name = new_line[1]
            freq = int(line[3])
            #checks fo dupliactes
            if year not in year_db:
                year_db[year] = dict()
            else:
                if name not in year_db[year]:
                    year_db[year][name] = freq
                else:
                    year_db[year][name]+=freq
    return year_db


def example_year_db1():
    """An example year_db (dictionary of dictionaries) for testing."""
    return {1977: {'Mark': 1000, 'Lida': 20, 'Rohit': 40},
            1978: {'Mark': 500, 'Lida': 15, 'Rohit': 80},
            1979: {'Mark': 200, 'Lida': 10, 'Rohit': 300}}
    

def example_year_db2():
    """An example year_db (dictionary of dictionaries) for testing.
    
    Create your own for making new tests!
    """
    return {1908: {'Ciera': 4000, 'Sistas': 70, 'Briiibrii': 400},
            1938: {'Samgreeneggsnham': 5000, 'Mahlulu': 100, 'Poot': 900},
            1971: {'Nana': 800, 'Citygurlzz': 300, 'NereereeCholeAristide': 890}}
 

def name_frequency(year_db, name):
    """
    Given a dictionary of dictionaries year_db (such as the one 
    returned by read_names()) and a string name, return a list 
    of totals (ints) for a given name across all years.  
    >>> name_frequency(example_year_db1(), "Rohit")
    [40, 80, 300]
    >>> name_frequency(example_year_db1(), "Lida")
    [20, 15, 10]

    >>> name_frequency(example_year_db2(), "Briiibrii")
    [400]
    >>> name_frequency(example_year_db2(), "NereereeCholeAristide")
    [890]
    """
    names_total = []
    for year in year_db:
        if name in year_db[year]:
            names_total = [year_db[year][name]]
        else:
            names_total+=[0]
    return names_total


def plot_name_frequency(year_list, freq_list):
    """
    For a list of frequencies (freq_list) for a specific name, plot 
    the popularity over time.  year_list is a list of ints corresponding
    to the years in freq_list.  
    """
    x_values = year_list
    y_values = freq_list
    plt.title('Name Frequency')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
   
    plt.plot(x_values,y_values)
    plt.savefig('nameFreq.png')


def letter_frequency(year_db, year):
    """
    Given a dictionary of dictionaries year_db and an integer year, return 
    a list of frequencies (ints) for how many names start with each letter.  
    The resulting list should have 26 entries corresponding to each letter 
    in alphabetical order.
    >>> letter_frequency(example_year_db1(), 1978)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 500, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> letter_frequency(example_year_db1(), 1979)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 200, 0, 0, 0, 0, 300, 0, 0, 0, 0, 0, 0, 0, 0]
    
    add 2 more doctests using example_year_db2()
    """
    # initialize dictionary to make sure every letter is represented

    letter_db = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
                 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
                 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
                 'Y': 0, 'Z': 0}
    freq_list = []
    year_dict = year_db[year]
    first_letter= name[0]
    for name in year_dict:
        letter_db[first_letter] = year_dict[name]
    
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        freq_list += [letter_db[letter]]
    return freq_list



def plot_letter_frequency(letter_freq_list):
    """
    For a list letter_freq_list of integer frequencies for each letter, 
    plot the frequency of each letter as a bar graph for the range
    of years given in year_list (a list of ints).  
    """
    # x-values are just letters in alphabet
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    x_values = letters
    y_values = letter_freq_list
    plt.figure(figsize = (10,5))
    plt.bar(x_values,y_values,width = .5)
    plt.title('Letter Frequency')
    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.savefig('letterFreq.png')



def test():
    """Exercise document tests."""
    from doctest import testmod
    testmod()


if __name__ == '__main__':
    # Run the doctests
    # test() 
    read_names("data/namesDataAll.csv") 

    # # Part 1.2. read in names, make dictionaries
    # # note: namesData.csv is a smaller file for testing purposes
    # #year_db = read_names('data/namesData.csv') 
    year_db = read_names('data/namesDataAll.csv')

    # # Part 1.3. get popularity of specific name
    freq_list = name_frequency(year_db, "Jeannie")
 
    # # Part 2.1. plot popularity of name over time
    year_list = [key for key in year_db]
    plot_name_frequency(year_list, freq_list)

    # # Part 3.1. get first letter frequencies for given year
    letters2020 = letter_frequency(year_db, 2020)

    # # Part 3.2. plot letter totals for specific year
    plot_letter_frequency(letters2020)
