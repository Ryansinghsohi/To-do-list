password = input('What is the password: ')
to_do_list = []

try:
    with open('uppgift.txt', 'r') as fil:
        to_do_list = [rad.strip() for rad in fil]
except FileNotFoundError:
    print("file 'uppgift.txt' doesn't appear. An empty list is being made.")


def index(item):
    for idx, item in enumerate(to_do_list, start=1):
        print(f'{idx}. {item}')


# basic password control
if password == '123':
    print('correct password!')
while password.lower() != 'exit':
    if password.lower() == '123':  # if password was correct run this script
        # menu and functions
        print('______Menu______')
        print('1. add to_do_list')
        print('2. view to_do_list')
        print('3. replace/remove to_do_list')
        print('4. mark done on to_do_list')
        print('5. clear list')
        print('6. save and exit\n')
        choose = input('what do u want to do: ')  # choice of what functions to run

        if choose == '1':  # adding to the list
            to_do_list.append(
                input('what do u want to add to your to_do_list: '))  # using the append function to add to the list
        elif choose == '2':  # print the list
            if to_do_list:
                print('list: ')
                index(to_do_list)
                rerun_code_after_view = input('rerun code(yes/no): ')
                if rerun_code_after_view != 'yes':
                    break
            else:
                print('list is empty')  # print list is empty if nothing is in there
        elif choose == '3':  # remove or replace element in the list
            remove_or_replace = input(
                'do you want to remove it or replace it(remove/replace): ')  # if you want to change or remove list
            if remove_or_replace.lower() == 'replace':  # if the user choose to replace an element
                index(to_do_list)  # print list with index
                change_index = int(
                    input('What to_do_list do you want to change: '))  # what in the list the user want's to change
                last_index = to_do_list.index(to_do_list[-1])
                first_index = to_do_list.index(to_do_list[0])
                if change_index in range(first_index, last_index):
                    replace_word = input('what do you want to change it to: ')  # what you want to change it to
                    to_do_list[change_index - 1] = replace_word  # adding it to the list
                else:
                    print('outside of range')
            if remove_or_replace.lower() == 'remove':  # if the user choose to remove an element
                print(index(to_do_list))  # print all to_do_lists
                remove_element = int(
                    input('What to_do_list to remove: '))  # veriabal that chooses the index of what to remove
                to_do_list.pop(remove_element - 1)  # how to remove element from list
        elif choose == '4':
            print(index(to_do_list))  # print the list
            mark_done = int(input('what do you want to mark done: '))  # get what you want to mark done
            to_do_list[mark_done - 1] += ': done'  # add done to the end of entry the program
        elif choose == '5':  # clear the list
            to_do_list.clear()  # the clear function to remove everything in list
        elif choose == '6':  # if they chose to save the list
            with open('uppgift.txt', 'w') as fil:
                for uppgift in to_do_list:
                    fil.write(uppgift + '\n')
                break
        else:
            print('please give a number from 1-6')
    else:  # if the password was wrong
        print('Wrong password')
        break
