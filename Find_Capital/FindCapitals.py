from tkinter import Tk, simpledialog, messagebox #imports resources from tkinter

def read_from_file(): #defines the function that will read the file with capitals and countries

    with open('capital_data.txt') as file: #opens .txt file to use

        for line in file: #for every line in the file

            line = line.rstrip('\n') #puts the words all in one line

            country, city =line.split('/') #puts country and city into variable

            the_world[country] = city #inputs it into list

def write_to_file(country_name, city_name): #defines a new functio that will input new countries and cities

    with open('capital_data.txt', 'a') as file: #open the following txt file

        file.write('\n' + country_name + '/' + city_name) #writes in the new country and corresponding city

print ('Ask the Expert - Capital Cities of the World') #display text

root = Tk() 

root.withdraw() 

the_world ={} #make dictionary

read_from_file() #runs funtion

 

while True:

    query_country = simpledialog.askstring('Country', 'Type the name of a country: ') #displays following string in a "simple dialog" and takes in input from user

 

    if query_country in the_world: #if the country that is being asked can be found in the txt file

        result = the_world[query_country] #find the corresponding capital and store in result variable
 
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!') #display the captial of the city being asked

    else: 

        new_capital= simpledialog.askstring('capital', "I don't know that one! Can you tell me what the capital is?") #display message and takes input
        write_to_file(query_country, new_capital) #using the function, writes the new capital and city into the txt file
        exit() 
       

root.mainloop() #loops code
