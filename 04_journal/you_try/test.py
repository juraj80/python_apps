import journaltest

def main():
    run_event_loop()


def run_event_loop():
    print("What do you want to do with your journal? ")
    journal_name ='default'
    journal_data = journaltest.load(journal_name)
    print('journaldata',journal_data)

    cmd= 'EMPTY'

    while cmd != 'x' and cmd:
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it:")
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and  cmd:
            print('Try again!')

    journaltest.save(journal_name,journal_data)
    print('Done. End of Journal')

def list_entries(data):
    print('Your journal entries: ')
    for idx,entry in enumerate(data):
        print('** {} {}'.format(idx+1,entry))

def add_entry(data):
    text = input('Type your entry, <enter> for exit: ')
    journaltest.add_entry(data,text)


if __name__ == '__main__':
    main()