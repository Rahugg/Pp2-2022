import os
while True:
    command = input()

    if command == 'cd':
        where = input()
        if os.path.isdir(where) and os.path.exists(where):
            os.chdir(where)
        else:
            print('Not a directory')

    elif command == 'gdeya':
        print(f'The current directory is: {os.getcwd()}')
    
    elif command == 'del':
        what = input()
        if os.path.exists(what):
            os.remove(what)
            print('Done')
        else:
            print('There is no such file')
    elif command == 'exit':
        break