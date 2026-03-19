def text_has_length(start: str,end: str): 
    """
    Gives a string with the total amount of characters it contains within the string. 
    Arguments: 
        start (str): The start of the output string
        end (str): The end of the output string
    """
    from dictionary import wordform
    # Catchment for common errors
    # End of catchment
    number_len = len(str(start) + str(end)) # Initial
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