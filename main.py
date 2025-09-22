def text_has_length(start,end): 
    from dictionary import wordform
    try: 
        str(start)
        str(end)
    except: 
        return "arguments are not strings"
    number_len = len(str(start) + str(end))
    interjection = ''
    for n in wordform: 
        if n == number_len:  
            print(start +   " " + interjection + ' ' + end)
            print(len(start + " " + interjection + ' ' + end))

    remainder = number_len
    while len(interjection + start + end) != number_len: 
        for n in reversed(wordform): 
            if remainder == 0: 
                break
            else: 
                if remainder % n == 0:
                    remainder -= remainder % n
                    interjection = str(interjection) + " " + str(wordform[remainder % n])
    
    print(start + " " + interjection + ' ' + end)
    print (len(start + " " + interjection + ' ' + end))


text_has_length("This sentence has "," characters. ")