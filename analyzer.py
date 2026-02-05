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
    
    while True:
        try:
            top_words=int(input("How many top words: "))
            if top_words <= 0:
                print("Please insert the number greater than 0")
                continue
            break
        
        except ValueError:
            print("Please input a valid number")
            

    sorted_out=sorted(count_words(text).items(), key=sorting_key, reverse=True)
    top_words_list=sorted_out[:top_words]
    
    for index, (key, value) in enumerate(top_words_list, start=1):
        print(f"{index}. {key} - {value}")



main()
