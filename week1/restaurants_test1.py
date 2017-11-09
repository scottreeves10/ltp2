def rest_test_1(file):

    line = file.readline()
    while line != '\n':
        print(line, end='')
        line = file.readline()
        
    file.close()
