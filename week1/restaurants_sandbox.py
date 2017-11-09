"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'

#Open the file containing the restaurant data
restaurants_file = open(FILENAME, 'r')


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    # return as a tuple: name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    # names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    # names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    # result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    #test reading a section - this works
    '''
    line = file.readline()
    while line != '\n':
        print(line, end='')
        line = file.readline()
    '''

    '''
    >>> read_restaurants(restaurants_file)
    Georgie Porgie
    87%
    $$$
    Canadian,Pub Food
    '''

    #test making a list from the first section, which means up to the first line == '\n' - this works
    '''
    line_list =[]
    line = file.readline()
    while line != '\n':
        line_list.append(line.rstrip('\n'))
        line = file.readline()

    print(line_list)
    '''

    '''
    >>> read_restaurants(restaurants_file)
    ['Georgie Porgie', '87%', '$$$', 'Canadian,Pub Food']
    ''' 

    #test making a list of each section until EOF, which means up to the first line == '' - this works - WAIT - not getting the 5th (last) section
    
    temp_list = []
    for line in file:
        if line != '\n':
            temp_list.append(line.rstrip('\n'))
            if len(temp_list) == 4:
                name_to_rating[temp_list[0]] = int(temp_list[1].strip('%'))
                temp_list = []
        
    for name in name_to_rating:
        print(name, name_to_rating[name])
        
    
    
    '''
    >>> read_restaurants(restaurants_file)
    ['Georgie Porgie', '87%', '$$$', 'Canadian,Pub Food']
    ['Queen St. Cafe', '82%', '$', 'Malaysian,Thai']
    ['Dumplings R Us', '71%', '$', 'Chinese']
    ['Mexican Grill', '85%', '$$', 'Mexican']
    '''

    #test inserting from line_list(s) into dicts

    '''
    line = file.readline()  #get the first line from the file
    while line != '':       #while not at the end of the file
        line_list =[]       #initiate empty line_list as an accumulator for each section in the file beteen purely new lines
        while line != '\n': #while not a break between section
            line_list.append(line.rstrip('\n')) #append the line from the file to the line_list
            line = file.readline()              #get the next line for the current section to go append to the line_list
        print(line_list) #test
        # insert code here to update dicts
        name_to_rating[line_list[0]] = int(line_list[1].rstrip('%'))
        line = file.readline()  # get the first line of the next section, or EOF
    '''
    
