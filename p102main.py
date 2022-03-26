import sys

def main():

    print('Welcome to Casual Clothing Wash')

    laundry_count = int(input('Enter laundry count: '))

    shirts = int(input('How many shirts/t-shirts: '))
    pants = int(input('How many shorts/pants/trousers: '))
    undergarment = int(input('How many undergarments - underwear, bra, tank-top, socks: '))
    dresses = int(input('How many dresses/skirts: '))
    other = int(input('Other articles of clothing: '))

    if laundry_count == (shirts+pants+undergarment+dresses+other):
        begin_process = input('Type yes to start the process, or type no to end the process: ')

        if begin_process == 'yes':
            print('Washing your clothes!')
            
            shirts_cost = shirts*0.50
            pants_cost = pants*0.65
            undergarment_cost = undergarment*0.25
            dresses_cost = dresses*0.75
            other_cost = other*0.45

            total_cost = shirts_cost+pants_cost+undergarment_cost+dresses_cost+other_cost

            print('We are charging you $',total_cost,' for ',laundry_count, ' pieces of clothing')
            
            confirm = input('Type yes in the terminal to confirm the transfer, or type no to end the program: ')

            if confirm == 'yes':
                print('Transfer successful, have a nice day!')
            else:
                print('We will care for your clothes while you get the certain amount of money, have a nice day!')
                sys.exit()
        else:
            print('Thank you!, have a nice day!')
            sys.exit()
    
    else:
        print('Looks like the total laundry count does not add up to the articles of clothing you gave... Please run the program again!')
        sys.exit()

main()