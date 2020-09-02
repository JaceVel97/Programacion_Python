message = input("> ")
words = message.split(' ')

emojis = {
    ":)": "😀",
    ":(": "😭",
    ";)": "😉",
    "XD": "😆",
    "(:": "🙃"
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '

print(output)