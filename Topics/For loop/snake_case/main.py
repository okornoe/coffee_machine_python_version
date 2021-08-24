user_input = input()

for ch in user_input:
    if ch.isupper() and user_input.index(ch) != 0:
        ch_index = user_input.index(ch)
        user_input = user_input.replace(ch, ch.lower(), 1)
        user_input = user_input[:ch_index] + "_" + user_input[ch_index:]
print(user_input.lower())