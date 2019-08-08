# def square(number):
#     return number * number
#
#
# print(square(3))

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard!')
#
#
# print('Start')
# greet_user(last_name='Smith', first_name='John')
# print('Finish')


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word)
    return output;

message = input(">")
print(emoji_converter(message))

