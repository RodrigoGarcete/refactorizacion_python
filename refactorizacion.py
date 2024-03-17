def main():
    while True:
        print_menu()
        num = input()

        if num.isdecimal():
            num = int(num)
            should_exit = process_menu_option(num)
            if should_exit:
                break
        else:
            print('Please enter a number between 1 and 3')


def print_menu():
    print('Choose the process you want to execute')
    print('1: Enter evaluation points and comments')
    print('2: Check previous results')
    print('3: Exit')


def process_menu_option(num):
    if num == 1:
        enter_evaluation()
    elif num == 2:
        check_results()
    elif num == 3:
        print('Exiting')
        return True  # Indicar que se debe salir del bucle principal
    else:
        print('Please enter a number between 1 and 3')
    return False  # Indicar que no se debe salir del bucle principal


def enter_evaluation():
    while True:
        print('Enter evaluation points between 1 and 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Please enter a number between 1 and 5')
            else:
                print('Enter a comment')
                comment = input()
                save_evaluation(point, comment)
                break
        else:
            print('Please enter evaluation points as numbers')


def save_evaluation(point, comment):
    post = f'Points: {point} Comment: {comment}'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')


def check_results():
    print('Previous results')
    with open("data.txt", "r") as read_file:
        print(read_file.read())


if __name__ == "__main__":
    main()
