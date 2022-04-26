import json

def Menu():
    print('\n\nAction\n1.initiallize data')
    print('2. getRoomById')
    print('3. getAllRoom')
    print('4. getChatById')
    print('5. getAllChatInRoom\n')
    inp = input('Select the Action: ')
    if inp == '1':
        Initialize()
    elif inp == '2':
        GetRoomByID()
    elif inp == '3':
        GetAllRoom()
    elif inp == '4':
        GetChatById()
    elif inp == '5':
        GetAllChatInRoom()
    else:
        print('Action not available, Plese select action again')

def Replay():
    a = input('\nPlease any button to Action menu\n\tor\nPlease 0 to exit program\n')
    if a == '0':
        print('Exit')
    else:
        Menu()

def Initialize():
    global data
    inp = input('Initialize data with file path: ')
    f = open(inp)
    data = json.load(f)
    f.close()
    print('Initialized')
    Menu()

def GetRoomByID():
    inp = int(input('getRoomById: '))
    if next((item for item in data['room'] if item['id'] == inp), None):
        print(next((item for item in data['room'] if item['id'] == inp), None))
    else:
        print('No room with id: ', inp)
    Replay()

def GetAllRoom():
    for i in data['room']:
        print(i)
    Replay()

def GetChatById():
    inp = int(input('getChatById: '))
    if next((item for item in data['chatEvent'] if item['id'] == inp),None):
        print(next((item for item in data['chatEvent'] if item['id'] == inp),None))
    else:
        print('No Chat with id: ', inp)
    Replay()

def GetAllChatInRoom():
    inp = int(input('getAllChatInRoomId: '))
    if next((item for item in data['chatEvent'] if item['roomId'] == inp),None):
        for i in data['chatEvent']:
            if i['roomId'] == inp:
                print(i)
    else:
        print('No chat in room id: ',inp)
    Replay()

Menu()