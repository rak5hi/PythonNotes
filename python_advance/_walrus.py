
(walrus := 1)
print(walrus)

def get_info(text: str) -> dict:
    
    return {'text': text,
            'letter': (length := len(text.replace(' ',''))),
            'words': (words := text.split()),
            'total_words': (word_length := len(words)),
            'avg_per_words': round(length / word_length, 2)}
    

if 0:
    for key, value in get_info('This is some text!').items():
        print(key, value, sep=':')
        

if 1:
    while user_input := input('You: '):
        print(">>", user_input)
    else:
        print("We are done here...")