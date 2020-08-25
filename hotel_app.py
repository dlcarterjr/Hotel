hotel1 = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}

hotel2 = {
     '101': {
        'guest': {
            'name': 'Sam Alderson',
            'phone': 8675698
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Dave Alderson',
            'phone': 4567869
         }
    },
    '105': {},
}

hotel3 = {
     '101': {
        'guest': {
            'name': 'Theodore Alderson',
            'phone': 8675567
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Steve Alderson',
            'phone': 4567609
         }
    },
    '105': {},
}
## FUNCTION TO CHECK IF ROOM IS OCCUPIED.

## Iterate through each room number (key) in Hotel dictionary.
def is_vacant(which_hotel,room):

        ## Check if a guest is assigned to that key (room number).
        try:
            if 'guest' in which_hotel[room]:
                print(f'\n{which_hotel[room]["guest"]["name"]} is assigned to room {room}.\n')  ## If guest assigned, return "occupied".
                return False
            else: 
                print(f'\nNo guest assigned to room {room}.\n')  ## Print occupied status.
                return True

        except KeyError:
            print(f'\nRoom {room} does not exist.\n')  ## Print occupied status.

is_vacant(hotel1,'101')
is_vacant(hotel1,'102')
is_vacant(hotel1,'107')


## ASSIGN A PERSON TO A ROOM.

## Assign a dictionary entry with guest name and room number to a variable.
guest_checkin = {'Name:':'John Smith','Phone:':'547-2871'}


## Call is_vacant to check if room is available.
def check_in(hotel, room, guest_dictionary):
    

    ## If room is available, assign guest to the room
    if is_vacant(hotel,room) == True:
        hotel[room] = guest_dictionary
        name = guest_dictionary['Name:']
        print(f'{name} has checked in to {room}.')
    return hotel[room]
    ## If room not available, output choose another room.

## Output guest room assignment.

print(check_in(hotel1,'102',guest_checkin))
    

## CHECKOUT FUNCTION

## Assign a dictionary entry with guest name and room number to a variable.
guest_checkout = {'Name:':'John Smith','Phone:':'547-2871'}

## Return and remove the person dictionary in that room.
def check_out(hotel,room,):
    hotel[room] = {}
    print('Guest checked out.')

check_out(hotel1,'102')


## MEDIUM: THREE HOTELS
menu = '''
Choose an option:

1. Room Status

2. Check In

3. Check Out

4. Quit
'''

##  While true loop for input (Room Status, Check In, Check Out, Quit).
    ## Input which hotel to check.
hotel_menu = '''
Choose which hotel:

1. Hotel One

2. Hotel Two

3. Hotel Three
'''
while True:  ## If Room Status
        ## Call is_vacant
    hotel_num = int(input(hotel_menu))
    option = int(input(menu))
    room = input("Which room to check? ")
    if hotel_num == 1:
        if option == 1:
            is_vacant(hotel1,room)
        
        if option == 2:
            guest_name = input("Guest name: ")
            guest_phone = input("Guest phone number: ")
            guest = {'Name:':guest_name, 'Phone:': guest_phone}
            check_in(hotel1, room, guest)
    
    
    
    ## If Check In
        ## Call check_in

    ## If Check Out
        ## Call check_out

    ## Else Quit