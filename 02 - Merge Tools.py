def merge_the_tools(string, k):
    length = len(string) 
    parts = int(length/k)

    for index in range(parts):
        #Get the piece from string
        piece = string[:k]
        #Delete the piece from string
        string = string[k+1:]

        #Auxiliar string having distinct characters
        aux_string = ""
        for letter in piece:
            # If a character is not already in pieces
            if letter not in aux_string:
                aux_string += letter
        
        #Print final string
        print(aux_string)
        
