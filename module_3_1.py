calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    string = str(string)
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Home'))
print(string_info('University'))
print(is_contains('Florence', ['flow', 'Flower', 'FLORA']))
print(is_contains('Ball', ['sphere', 'ball']))
print(calls)



