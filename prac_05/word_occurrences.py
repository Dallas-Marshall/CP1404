def main():
    word_to_count = {}
    words = input("Text: ").split()
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    word_count_keys = list(word_to_count.keys())
    word_count_keys.sort()
    for word in word_count_keys:
        count = word_to_count.get(word)
        print("{:{}} {}".format(word + ':', calculate_longest_word(word_count_keys) + 1, count))


def calculate_longest_word(words):
    """Returns longest word length"""
    longest_word = 0
    for word_key in words:
        length = len(word_key)
        if length > longest_word:
            longest_word = length
    return longest_word


main()
