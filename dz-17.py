test_sting = "there is vomit on his sweater already"
test_sting_2 = "greetings, friends"


def correct_sentence(text):
    text_end = ""
    if text[-1] not in "!?.,;:":
        text_end = "."
    return text[0].upper() + text[1::] + text_end


correct_sentence(test_sting_2)

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')