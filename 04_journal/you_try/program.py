import datetime
import journal


def main():
    print_header()
    run_event_loop()

def print_header():
    print('-----------------------------')
    print('           JOURNAL APP')
    print('-----------------------------')

def run_event_loop():

    print('What do you want to do with your journal?')
    journal_name = 'default'
    journal_data = journal.load(journal_name) # if new journal, returns empty list


    cmd = 'EMPTY'
    while cmd != 'x': # not equals to x and is True (non empty)

        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:  ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and not cmd:
            print('Try again!')



    journal.save(journal_name,journal_data)
    print('Done. End of Journal.')


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)

    for idx, entry in enumerate(data):
        print('* [{}] {}'.format(idx+1, entry))


def add_entries(data):
    text = input('Type your entry, <enter> for exit: ')
    journal.add_entry(text, data)

#    data[datetime.datetime.today()] = text



print('__name__:',__name__)

if __name__ == '__main__': # if a script is imported as a module , the variable __name__ equals to the name of a module, otherwise is set to a __main__
    main()