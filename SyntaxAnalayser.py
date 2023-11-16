from Reader import Reader
from ErrorHandler import RaiseError
from Tokens import TYPE
CARLU=''
NUM_LIGNE=0
INDEX = 0

class SyntaxAnalayser:

    def __init__(self,program_file_path):
        self.prog = Reader(program_file_path).content
        if INDEX >= len(self.prog):
            RaiseError.END_OF_FILE()



    def LIRE_CAR(self,index):
        global CARLU
        global NUM_LIGNE
        global INDEX
        if INDEX < len(self.prog):
            CARLU  = self.prog[INDEX]
            if CARLU == '\n':
                NUM_LIGNE+=1
        else:
            RaiseError.END_OF_FILE()

    def is_seperateur(self):
        return self.prog[INDEX] == ' ' | self.prog[INDEX] == '    ' | self.prog[INDEX] == '\n'
    def is_comment(self):
        return self.prog[INDEX] == '{'
 
    def SAUTER_SEPARATEUR(self):
        global INDEX
        while INDEX < len(self.prog) and self.is_seperateur() :
            INDEX+=1
        def detect_comment(self):
            global INDEX 
            counter = 0 
            if self.prog[INDEX] == '{':
                counter += 1
                while counter != 0:        
                    if self.prog[INDEX] == '}':
                        counter -= 1
                    INDEX += 1
                    
            

    def is_entier(self) : 
        return self.prog[INDEX] == '0' | self.prog[INDEX] == '1' | self.prog[INDEX] == '2'| self.prog[INDEX] == '3' | self.prog[INDEX] == '4' | self.prog[INDEX] == '5' | self.prog[INDEX] == '6' | self.prog[INDEX] == '7' | self.prog[INDEX] == '8'| self.prog[INDEX] == '9' 
            
    def RECO_ENTIER(self) :
        global INDEX
        x=''
        while (INDEX < len(self.prog) and self.is_entier()) :
            x = x + str(INDEX)
            INDEX += 1 
        return TYPE

        

        

           
        
                

















SyntaxAnalayser("./ExampleProg.txt")
print("CARLU",CARLU)
