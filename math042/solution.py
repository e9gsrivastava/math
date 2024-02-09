
t_list=[0.5*i*(i+1) for i in range(1,10000)]

letter_to_num_dict={ 'A':1,   'B':2,    'C':3,    'D':4,   'E':5,   'F':6,    'G':7,    'H':8,   'I':9,   'J':10,
                     'K':11,  'L':12,   'M':13,   'N':14,  'O':15,  'P':16,   'Q':17,   'R':18,  'S':19,  'T':20, 
                     'U':21,  'V':22,   'W':23,   'X':24,  'Y':25,  'Z':26 }


def is_traingle(word):
    '''to chcek if the word is traingular or not'''
    c=0
    for letter in word:
        c+=letter_to_num_dict[letter.upper()]
    if c in t_list:
        return True
    return False

def answer():
    with open('words.txt', 'r', encoding='UTF-8') as f:
        data=f.read()


    data=data.split(',')
    result=0

    for i in data:
        if is_traingle(i[1:-1]):
            result+=1
    return result

if __name__=='__main__':
    print(answer())

