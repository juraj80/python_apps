import movie_svc
import requests.exceptions

def print_header():
    print('------------------------------------------')
    print('             MOVIE SEARCH APP')
    print('------------------------------------------')

def search_event_loop():
    search = 'SEARCH_EVENT_LOOP'

    while search != 'x':
        try: # try to process code in block, if something goes wrong, raise exception
            search = input("Movie search text (x to exit): ")
            if search != 'x':
                result = movie_svc.find_movies(search)
                print("Found {} movies for search {}:".format(len(result), search))
                for r in result:
                    print("{} - {}".format(r.year, r.title))
                print()
        except ValueError: # catches valueError  from find_movies function
            print("Error: Search text is required.")
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print('exiting...')


def main():

    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()
