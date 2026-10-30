
def wc(book_text_string):
    num_words = (len(book_text_string.split()))
    return num_words

def char_count(book_text_string):
    counts = {}
    for item in book_text_string:
        item = item.lower()
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def sort_on(value: tuple[str, int]):
    return value[1]

def chars_dict_to_sorted_list(char_counts: dict[str, int]):
    pairs_list = []
    for item in char_counts:
        pairs_list.append((item, char_counts[item]))
    pairs = sorted(pairs_list, reverse=True, key=sort_on)
    return pairs
