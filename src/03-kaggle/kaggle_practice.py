def word_search(doc_list, keyword):
    # word=list[]
    # for phrase in doc_list:
    #     word_list.append( phrase.lower().strip(",.").split() )
    indices = [] 
    for i, doc in enumerate(doc_list): #la función enumerate generar un índice para las listas. Ej, 0,1,2
        word_list = doc.split()
        #normalized = [token.strip(".,").lower() for token in words] #listas por comprensión
        normalized = [
            palabra.strip(".,").lower() #operación
            for palabra in word_list #bucle
        ]
        print(normalized)
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


doc_list = ["The Learn Python Challenge Casino.", "They bought a car, and a horse", "Casinoville"]
print(word_search(doc_list,'casino'))

