class Tests:
    def __init__(self, input):
        super().__init__()
        
        
        
        stringtocheck = input
def isPalendrome(stringtocheck):
        alphabet = [('a',False),  # lsit of tupes of char assosiated with boolean
                    ('b',False),
                    ('c',False),
                    ('d',False),
                    ('e',False),
                    ('f',False),
                    ('g',False),
                    ('h',False),
                    ('i',False),
                    ('j',False),
                    ('k',False),
                    ('l',False),
                    ('m',False),
                    ('n',False),
                    ('o',False),
                    ('p',False),
                    ('q',False),
                    ('r',False),
                    ('s',False),
                    ('t',False),
                    ('u',False),
                    ('v',False),
                    ('w',False),
                    ('x',False),
                    ('y',False),
                    ('z',False),]
        
        for i in range(len(stringtocheck)):
          for j in range(len(alphabet)):
                if(stringtocheck[i]) == alphabet[j][i]:
                     alphabet[j][1] == True

        print(alphabet)
                     

            
          

