def emojify(sentence):
    emoji_dict = {'thumbsup':'👍','sad':'😔','happy':'😊','hearteye':'😍'}
    split_sentence = sentence.split(':')
    emoji_word = sentence.split(':')[1]
    emoji = emoji_dict.get(emoji_word)
    split_sentence[1] = emoji
    print(''.join(split_sentence))