class Reader():
    def __init__(self,arquivo):
        self.arquivo = arquivo
    
    def lendoArquivo(self):
        with open(arquivo) as f:
            header = f.readline()
            separator = header.split(' ')
            army_begin = separator[0]
            nro_castelos = separator[1]
            nro_estradas = separator[2]
            

        