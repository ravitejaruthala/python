#For decrypting the given encrypted message

def decrypt_text(deCode):

    source_tuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                    'p','q','r','s','t','u','v','w','x','y','z',' ','.')
    decrypt_list = []
    decrypted = ''

    for i in deCode[0:14]:
        decrypt_list.append(i)

    for i in deCode[-14:]:
        decrypt_list.append(i)

    decrypt_dict = {decrypt_list[i]: source_tuple[i] for i in range(len(source_tuple))}

    for i in deCode[14:-14]:
        decrypted = decrypted+decrypt_dict[i]

    print(decrypted)

#Give the encrpted message here
code = '*](!#$=^@>;-+)^#--?`~?/-!?.</_[&%~{,:`}'
decrypt_text(code)
