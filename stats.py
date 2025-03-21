# get the word count of the book
def get_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

# ah, the joy of COUNTING!
def character_count(file_contents):
    file_contents = file_contents.lower()
    character_dicts = {}

    # iterate through every character in the file
    for char in file_contents:
        # increment
        if char in character_dicts:
            character_dicts[char] += 1
        # add char as key and set value to 1 if it doesn't exist
        else:
            character_dicts[char] = 1

    return character_dicts
    #return f"{len(file_contents.lower())} characters found in the document"

# format each dictionary into a list of cute pretty dicts
def format_dicts(main_dict):
        # list
    sort = []

    # iterate through each key:value pair
    for char, count in main_dict.items():
        if char.isalpha():
            # the pretty
            formatted = {
                "character": char,
                "count": count
            }
            # make the list of pretty dicts
            sort.append(formatted)

    return sort

# used for sorting pretty list from high to low
def sort_on(e):
    return e["count"]

# sort the pretty list
def sort_list(sort):
    sort.sort(reverse=True, key=sort_on)
    return sort

# format the pretty list for report
def format_list(sort):
    for item in sort:
        print(f"{item['character']}: {item['count']}")