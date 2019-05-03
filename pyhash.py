from sys import argv

file1 = str(argv[1])
file2 = str(argv[2])

#take the input, and reads it line by line, path to second function
def color_apply():
    with open(file1, 'r') as color:
        for line in color:
            global color_input
            color_input = line.strip('\n')
            city_apply()


#creates variable for 2nd file and reads it line by line, sends to number function            
def city_apply():
    with open(file2, 'r') as city:
        for line in city:
            global city_input 
            city_input = line.strip('\n')
            number_apply()

#adds both list together and adds a number between 00-99, writes to file with different formatting        
def number_apply():
    for number in range(0, 99):
        #writes all information to file.
        with open('getbent.txt', 'a') as the_file:
            #makes number 2 digit
            strnum = str(f'{number:02}')
            #input unfiltered
            the_file.write(color_input+city_input+strnum+'\n')
            #input with no space
            the_file.write((color_input+city_input+strnum+'\n').strip(" "))
            #input with lowercase color
            the_file.write(str.lower(color_input)+city_input+strnum+'\n')
            #input with lowercase color and no space
            the_file.write((str.lower(color_input)+city_input+strnum+'\n').strip(" "))
            #input with all lowercase
            the_file.write(str.lower(color_input+city_input+strnum+'\n'))
            #input with all lowercase and no space
            the_file.write((str.lower(color_input+city_input+strnum+'\n')).strip(" "))
            #the_file.write(str.lower((clrcty+strnum+'\n').strip(" ")))
                
#starts program       
color_apply()