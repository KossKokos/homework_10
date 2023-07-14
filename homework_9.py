from re import findall
dct_of_names_nums = {}

def input_error(func):
    def wrapper(command):
        try:
            result = func(command)
            return result
        except KeyError:
            return 'wrong name, please try again'
        except ValueError:
            return 'not a number, please try again'
        except IndexError:
            return 'enter one of those commands: (add, show_all, hello, change, phone)'
    return wrapper

@input_error
def say_hello(command):
    return 'How can I help you?'

@input_error
def add_num_name(command):
    find_name_num = r'[A-z\d]{1,}'
    lst_command = command.split(' ')
    lst_contact = ' '.join(lst_command[1:])
    lst_name_num = findall(find_name_num, lst_contact.lower())
    if lst_name_num[0].isalpha() and lst_name_num[1].isdigit():
        dct_of_names_nums.update({lst_name_num[0]:lst_name_num[1]})
        return 'Success!'
    else:
        return 'Not a name or not a number, please try again'

@input_error
def change_num(command):
    find_name_num = r'[A-z\d]+'
    name_num = command.split(' ')
    lst_contact = ' '.join(name_num[1:])
    lst_name_num = findall(find_name_num, lst_contact)
    if lst_name_num[0] in dct_of_names_nums.keys() and lst_name_num[1].isdigit():
        dct_of_names_nums[lst_name_num[0]] = lst_name_num[1]
        return 'Success!'
    else:
        return f'{lst_name_num[0]} is not in dictinonary'
    
@input_error
def find_phone(command):
    find_name_num = r'[A-z\d]+'
    name_num = command[5:]
    lst_name_num = findall(find_name_num, name_num.lower())
    if lst_name_num[0] in dct_of_names_nums.keys():
        return dct_of_names_nums[lst_name_num[0]]
    else:
        return f'{lst_name_num[0]} is not in dictionary'
    
@input_error
def show_all(command):
    return dct_of_names_nums

@input_error
def find_commands(command):
    command_re = r'^[A-z]{1,}'
    find_command = findall(command_re, command.lower())
    return find_command[0]

def main():
    while True:
        user_input = input('>>>')
        users_inputs = {
                    'hello': say_hello(user_input.lower()), 
                    'add': add_num_name(user_input.lower()),
                    'change': change_num(user_input.lower()), 
                    'phone': find_phone(user_input.lower()), 
                    'show_all': show_all(user_input.lower())
                    }
        if user_input == 'exit' or user_input == 'close' or user_input == 'good bye':
            print('Good bye!')
            break
        if user_input == None:
            print('enter a command')
        if find_commands(user_input) in users_inputs.keys():
            result = users_inputs.get(find_commands(user_input))
            print(result)
        else:
            print('wrong command')
            
if __name__ == '__main__':
    main()