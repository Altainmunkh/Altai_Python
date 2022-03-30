#The mega function
booked_seats = [[[],[],[]],[[],[],[]],[[],[],[]]]
def cinema_booking():
    movie_index=None
    session_index=None 
    chosen_seating="nothing"
    #the seating function
    def the_seating_function():
        nonlocal chosen_seating
        nonlocal movie_index
        nonlocal session_index
        while chosen_seating not in seating:
            chosen_seating = input("Which seat would you like? ")
            if chosen_seating == "x":
                print('This seat is taken')
                chosen_seating='nothing2'
            elif chosen_seating in seating:
                print("You have chosen seat [", chosen_seating,']')
                booked_seats[movie_index][session_index]=chosen_seating
            else:
                print("error, input not accepted. (check your spelling and capitalization)")
    #name and phone number
    name = input('What is your name?')
    phone_number = input('What is your phone number?')

    #confirming the phone number
    phone_confirm = input(f"{phone_number} Confirm? y/n ")
    while phone_confirm != "y":
        match phone_confirm:
            case "y" : 
                break
            case "n": 
                phone_number = input('What is your phone number?')
                phone_confirm = input(f"{phone_number} Confirm? y/n ")
            case defult: 
                print('Enter again') 
                phone_confirm = input(f"{phone_number} Confirm? y/n ")

    #the movie list
    movies = ( 'The Movie','The Movie 2','The Movi3' )
    print("These are today's movies")
    for movie in movies:
        print(movie)

    #Checking if the movie is right 
    chosen_movie = "sdfghjk"
    while chosen_movie not in movies:
        chosen_movie = input("Which movie would you like to watch? ")
        if chosen_movie in movies:
            print("You have chosen", chosen_movie)
            movie_index=movies.index(chosen_movie)
        else:
            print("error, input not accepted. (check your spelling and capitalization)")


    #confirming the movie choice
    movie_confirm = input(f"{chosen_movie} Confirm? y/n ")
    while movie_confirm != "y":
        match movie_confirm:
            case "y" : 
                break
            case "n": 
                chosen_movie = "sdfghjk"
                while chosen_movie not in movies:
                    chosen_movie = input("Which movie would you like to watch? ")
                    if chosen_movie in movies:
                        print("You have chosen", chosen_movie)
                    else:
                        print("error, input not accepted. (check your spelling and capitalization)")
                movie_confirm = input(f"{chosen_movie} Confirm? y/n ")
            case defult: 
                print('Enter again') 
                movie_confirm = input(f"{chosen_movie} Confirm? y/n ")

    #the time table
    times = ('Morning','Afternoon','Evening')
    print("These are today's times")
    for time in times:
        print(time)

    chosen_time = "sdfghk"
    while chosen_time not in times:
        chosen_time = input("When would you like to watch? ")
        if chosen_time in times:
            print("You have chosen to watch in the", chosen_time)
            session_index=times.index(chosen_time)
        else:
            print("error, input not accepted. (check your spelling and capitalization)")


    #confirming the time choice
    time_confirm = input(f"{chosen_time} Confirm? y/n ")
    while time_confirm != "y":
        match time_confirm:
            case "y" : 
                break
            case "n": 
                chosen_time = "sdfghjk"
                while chosen_time not in times:
                    chosen_time = input("Which time would you like to watch? ")
                    if chosen_time in times:
                        print("You have chosen", chosen_time)
                    else:
                        print("error, input not accepted. (check your spelling and capitalization)")
                time_confirm = input(f"{chosen_time} Confirm? y/n ")
            case defult: 
                print('Enter again') 
                time_confirm = input(f"{chosen_time} Confirm? y/n ")
    #the seating arrangement
    match chosen_movie:
        #movie 1
        case "The Movie":
            match chosen_time:
                case "Morning":
                    seating = ["1",'2','x','x','x','6','7','8']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()

                case "Afternoon":
                    seating = ["1",'2','3','x','x','6','7','x']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
                case "Evening":
                    seating = ["1",'2','3','x','x','x','x','x']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
        #movie 2
        case "The Movie 2":
            match chosen_time:
                case "Morning":
                    seating = ["x",'2','x','4','x','6','7','x']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
                case "Afternoon":
                    seating = ["1",'2','3','4','x','6','7','x']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
                case "Evening":
                    seating = ["x",'x','x','4','5','6','7','8']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
        #movie 3
        case "The Movi3":
            match chosen_time:
                case "Morning":
                    seating = ["1",'2','x','4','5','6','x','8']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
                case "Afternoon":
                    seating = ["1",'x','x','x','x','6','7','8']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
                case "Evening":
                    seating = ["1",'x','3','x','x','6','7','8']
                    print (seating[0:4])
                    print (seating[4:8])
                    the_seating_function()
    #booking info
    print("You have chosen to watch",chosen_movie,"in the",chosen_time,"at seat [",chosen_seating,']')    


#the variables
final_confirm='n'
#chosen_seating="[something's wrong]"
#intro 
print('Welcome to The Grand Movie Theatre')

#the code
while final_confirm != "y":
        match final_confirm:
            case "y" : 
                print("Confirmed, thank you for booking with us.")
            case "n": 
                chosen_time = "sdfghjk"
                chosen_movie = "sdfghjk"
                final_confirm = "n"
                seating = ['[a]','[b]','[x]','[d]']
                cinema_booking()
                final_confirm = input("Confirm? y/n ")
            case defult: 
                print('Enter again') 
                final_confirm = input("Confirm? y/n ")