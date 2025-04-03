def main():
    # Anton's age is given directly
    anton = 21  
    
    # Beth is 6 years older than Anton
    beth = anton + 6
    
    # Chen is 20 years older than Beth
    chen = beth + 20
    
    # Drew is as old as Chen's age plus Anton's age
    drew = chen + anton
    
    # Ethan is the same age as Chen
    ethan = chen  
    
    # Print out each friend's age in the required format
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# Ensure that the main function is executed
if __name__ == '__main__':
    main()
