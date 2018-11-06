import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_header()

    folder = get_folder_from_user()
    if not folder:
        print("We can't search that location !")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing !")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
    #        print('------------MATCH-----------')
    #        print('file: {}'.format(m.file))
    #        print('linenum: {}'.format(m.line))
    #        print('match: {}'.format(m.text.strip()))
    #        print()
    print('Found {:,} matches.'.format(match_count))


def print_header():
    print('--------------------------------------')
    print('          FILE SEARCH APP')
    print('--------------------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search ? ')
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]?  ')
    if not text or not text.strip():
        return None
    return text.lower()


def search_folders(folder, text):
    print("Looking for {} in {}".format(text, folder))
    #    all_matches = []
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # matches = search_folders(full_item,text)
            # all_matches.extend(matches)
            # for m in matches:
            # yield m
            # yield from matches
            yield from search_folders(full_item, text)

        else:
            # matches = search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            # yield m
            yield from search_file(full_item, text)

#   return all_matches

def search_file(file_name, search_text):
    #    matches = []
    with open(file_name, 'r', encoding='utf-8') as fin:
        linenum = 0
        for line in fin:
            linenum += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(file=file_name, line=linenum, text=line)
                #                matches.append(m)
                yield m


#        return matches

if __name__ == '__main__':
    main()
