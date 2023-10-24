# Week 3, Unit 2: Exercise (Python_1)

# One of the nice features of Python is that it supports Unicode. Therefore, it is possible to use emojis
# just like other characters in strings. In this exercise you will use this feature to build an emoji translator.
# Below is a dictionary that maps English terms to Emojis (broken into multiple lines for better readability).

# Use this dictionary to build a program that:
#
# Reads a sentence from the user.
# Replaces all the words in the sentence with the corresponding Emoji.
# Below is an example execution of the program:

# Please enter a sentence: I'm so excited to learn python
# I'm so 🤩 to finally learn 🐍

emoji = {
"happy": "😃",
"heart": "😍",
"rotfl": "🤣",
"smile": "😊",
"crying": "😭",
"kiss": "😘",
"clap": "👏",
"grin": "😁",
"fire": "🔥",
"broken": "💔",
"think": "🤔",
"excited": "🤩",
"boring": "🙄",
"winking": "😉",
"ok": "👌",
"hug": "🤗",
"cool": "😎",
"angry": "😠",
"python": "🐍"
}


if __name__ == '__main__':
    print("")
