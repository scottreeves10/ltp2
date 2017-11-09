# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        ''' (Rat, str, int, int) -> NoneType

        A Rat identified by a one-char symbol, located in a Maze at a row and column,
        and which eats brussel sprouts it finds in the Maze's paths as it moves around
        the rows and columns of the Maze.

        '''
        
        self.symbol = symbol #the 1-character str symbol for the rat
        self.row = row # the row int where the rat is located
        self.col = col # the column int where the rat is located
        self.num_sprouts_eaten = 0 # the number of sprouts that this rat has eaten, which is initially 0.

    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column '''

        self.row = row
        self.col = col

    def eat_sprout(self):
        ''' (Rat) -> NoneType

        Increment num_sprouts_eaten by 1. '''

        self.num_sprouts_eaten += 1


    def __str__(self):
        ''' (Rat) -> str
        
        Return a string representation of this Rat, in this format:
        
        symbol at (row, col) ate num_sprouts_eaten sprouts.
        
        For example:
        
        'J at (4, 3) ate 2 sprouts.'
        
        Do not put a newline character ('\n') at the end of the string.'''

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)      


        
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        ''' (Maze, list of list of str, Rat, Rat)

        Example call:

        Maze([['#', '#', '#', '#', '#', '#', '#'], 
              ['#', '.', '.', '.', '.', '.', '#'], 
              ['#', '.', '#', '#', '#', '.', '#'], 
              ['#', '.', '.', '@', '#', '.', '#'], 
              ['#', '@', '#', '.', '@', '.', '#'], 
              ['#', '#', '#', '#', '#', '#', '#']], 
              Rat('J', 1, 1),
              Rat('P', 1, 4))

        '''

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.maze[rat_1.row][rat_1.col] = rat_1.symbol #new
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol #new
        self.num_sprouts_left = 0
        lenL = len(maze)
        i = 0
        while i < lenL:
            self.num_sprouts_left = self.num_sprouts_left + maze[i].count(SPROUT)
            i += 1

    def is_wall(self, row, col):
        '''(Maze, int, int) -> bool

        The first parameter represents a maze, the second represents a row, and the third represents a column.

        Return True if and only if there is a wall at the given row and column of the maze.

        '''

        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        '''(Maze, int, int) -> str
        
        The first parameter represents a maze, the second represents a row,
        and the third represents a column.

        Return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should be returned rather than HALL.
        '''

        if self.maze[row][col] == HALL:
            return HALL
        else:
            return self.maze[row][col]
        
    def move(self, rat, vert, hor):
        ''' (Maze, Rat, int, int) -> bool

        The first parameter represents a maze, the second represents a rat,
        the third represents a vertical direction change (UP, NO_CHANGE or DOWN),
        and the fourth represents a horizontal direction change (LEFT, NO_CHANGE or RIGHT).

        Examine the location to be moved to.

        If it is a WALL, do nothing and return False.

        Otherwise, do the following:

          1. If the destination contains a SPROUT do the following:

            a) Decrease the number of sprouts left by one.

            b) Increase the number of sprouts the rat has eaten by one.

          2. Change the starting point to show a HALL

          3. Change the destination to show the rat. (ie. Move the rat to the new location)

          4. Return True.


        '''

        starting_row = rat.row
        starting_col = rat.col
        destination_row = rat.row + vert
        destination_col = rat.col + hor
        destination_char = self.get_character(destination_row, destination_col)
        
        if destination_char == WALL:
            return False
        else:
            if destination_char == SPROUT:
                self.num_sprouts_left = self.num_sprouts_left - 1
                rat.eat_sprout()
            self.maze[starting_row][starting_col] = HALL
            self.maze[destination_row][destination_col] = rat.symbol #new
            rat.set_location(destination_row, destination_col)
            return True
        
    def __str__(self):

        s = ''
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                s = s + self.maze[i][j]
            s = s + '\n'
        s = s + Rat.__str__(self.rat_1) + '\n'
        s = s + Rat.__str__(self.rat_2)

        return s   
                
                
                
    
