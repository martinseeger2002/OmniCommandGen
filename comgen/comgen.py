import numpy as np

print('If you like this program send LTC donations to the folloing address.\nMDUHFa18kKuCaGB3RdEHZ2GMbAAHVhgFCM\n')
token_name = "test"  #input('Enter the name of new tokens to create.\n')
sending_address = "test" #input('Enter your sending address.\n')
array_number = 0
serial_number = 100001
token_url = "test" #input('Enter your url or leave blank.\n')


def txt_to_list():
    global data_packet, array
    text_data = open('data.txt', "r")
    data = text_data.read()
    text_data.close()
    string = (data)
    n = 255
    list = [string[index : index + n] for index in range(0, len(string), n)]
    array = np.array(list)
    data_packet = (array[int(array_number)])

def create_omni_txt():
    f = open('omnicommands.dat', 'w+')
    f.close()


def add_to_omni_txt():
    f = open('omnicommands.dat', 'a+')
    f.write(omni_command)
    f.write("\n")
    f.close()


def create_omni_command_d1():
    global omni_command_d1, array_number
    omni_command_d1 = "omni_sendissuancefixed " + '"' + sending_address + '" ' + "1 1 0 " + '"' + data_packet


def create_omni_command_d2():
    global omni_command_d2, array_number
    omni_command_d2 = '" "' + data_packet

def create_omni_command_d3():
    global omni_command_d3, array_number
    omni_command_d3 = '" "' + token_name + str(serial_number)[1:] + '" "' + token_url + '" "' + data_packet + '" "1"'

def add_one_to_array_number():
    global array_number
    if array_number < last_array_number:
        array_number = array_number+1

        



txt_to_list()
create_omni_txt()
last_array_number = len(array)


while array_number<=last_array_number:
    if array_number == last_array_number-1:
        txt_to_list()
        create_omni_command_d1()
        omni_command = omni_command_d1 + '" "' + '" "' + token_name + str(serial_number)[1:] + '" "' + token_url + '" "''" "1"'
        add_to_omni_txt()
        exit()
    elif array_number == last_array_number-2:
        create_omni_command_d1()
        add_one_to_array_number()    
        txt_to_list()
        create_omni_command_d2()
        omni_command = omni_command_d1 + omni_command_d2 + '" "' + token_name + str(serial_number)[1:] + '" "' + token_url + '" "''" "1"'
        add_to_omni_txt()
        exit()
        serial_number=serial_number+1
    
    elif array_number==last_array_number-3:
        txt_to_list()
        create_omni_command_d1()
        add_one_to_array_number()    
        txt_to_list()
        create_omni_command_d2()
        add_one_to_array_number() 
        txt_to_list()
        create_omni_command_d3()
        add_one_to_array_number()
        omni_command = omni_command_d1 + omni_command_d2 + omni_command_d3
        add_to_omni_txt()
        exit()
    elif array_number<=last_array_number-4:
        txt_to_list()
        create_omni_command_d1()
        add_one_to_array_number()    
        txt_to_list()
        create_omni_command_d2()
        add_one_to_array_number() 
        txt_to_list()
        create_omni_command_d3()
        add_one_to_array_number()
        omni_command = omni_command_d1 + omni_command_d2 + omni_command_d3
        add_to_omni_txt()
        serial_number=serial_number+1
        