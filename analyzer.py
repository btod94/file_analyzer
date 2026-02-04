def count_words(text):
    word_freq={}
    punct = ".,!?;:()[]\"'"
    for word in text.split():
        w=word.lower().strip(punct)
        
        if w == "":
            continue
        
        if w in word_freq:
            word_freq[w]+=1
        else:
            word_freq[w]=1
    
    return word_freq

def sorting_key(pair):
    return pair[1]

def main():

    filename=input("Insert filename:")

    try:
        with open(filename, "r") as f:
            text=f.read()

    except FileNotFoundError:
        print("File not found")
        return
    
    sorted_out=sorted(count_words(text).items(), key=sorting_key, reverse=True)
    top3=sorted_out[:3]
    
    for index, (key, value) in enumerate(top3, start=1):
        print(f"{index}. {key} - {value}")


main()
