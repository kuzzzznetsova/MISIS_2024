def merge_dicts(dict_a, dict_b, dict_c):
    merged_dict = {**dict_a, **dict_b, **dict_c}
    return merged_dict

dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}

result = merge_dicts(dict_a, dict_b, dict_c)

print(result)
