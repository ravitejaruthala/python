

def encrypt_text(code):
    source_tuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                    'p','q','r','s','t','u','v','w','x','y','z',' ','.')
    special_set = {'!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}',
                   '[',']','<','>','?','/','~','`',',','.',':',';'}
    special_dict = {}
    encrypted = ''
    special_list = []

    for i in special_set:
        special_list.append(i)
    special_dict = {source_tuple[i]: special_list[i] for i in range(len(source_tuple))}

    code = code.lower()

    for i in special_list[0:14]:
        encrypted = encrypted+i

    for i in code:
        encrypted = encrypted+special_dict[i]

    for i in special_list[14:]:
        encrypted = encrypted+i

    print(encrypted)


code = 'Hello World'
encrypt_text(code)


