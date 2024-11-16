def group_anagrams(strings: list):
    anagrams_list = []
    try:
        if not strings:
            return []

        anagrams_dict = {}
        for string in strings:
            sorted_string = ''.join(sorted(string))
            # all anagrams will have same sorted_string as key
            if not sorted_string in anagrams_dict:
                anagrams_dict[sorted_string] = [string, ]
            else:
                anagrams_dict[sorted_string].append(string)

        # Our anagrams list will be the values of this dictionary
        anagrams_list = list(anagrams_dict.values())
    except Exception as e:
        raise e
    finally:
        return anagrams_list


if __name__ == '__main__':
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(input_list))
