calls = 0
def count_calls(call):
    global calls
    calls += call
    return calls
def string_info(string):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a
def is_contains(string_info, is_contains):
    string_info.lower()
    new_is_contains = []
    count_calls(1)
    for i in is_contains:
        new_is_contains.append(i.lower())
    return (string_info.lower() in new_is_contains)

print(string_info('Microwave'))
print(string_info('Brain'))
print(is_contains('house', ['housefly', 'doghouse','house']))
print(is_contains('pen', ['schoppen', 'penalty', 'open']))
print(calls)