def count_words(text: str):
    split_text: list = text.split()
    return split_text.__len__()

def num_characters (text: str):
    results: dict = {}
    for char in text:
        if char.lower() in results:
            results[char.lower()] += 1
        else:
            results[char.lower()] = 1
    return results

def character_dict_sort(unsorted_dict: dict):
    new_list: list = []
    for key in unsorted_dict:
        new_list.append({"char": key, "num": unsorted_dict[key]})
    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(items: dict):
    return items["num"]