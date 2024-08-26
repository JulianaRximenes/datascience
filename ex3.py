class Aluno():
    def __init__(self,ch,faltas):
        self.ch=ch
        self.faltas=faltas

    def calcular_faltas(self):
        percent_ch= self.ch * (25/100)
        if self.faltas > percent_ch:
         msg = 'retido'

        else:
           
            msg = 'promovido'

        return f' faltas-hs permitidas: {percent_ch} voce faltou: {self.faltas} horas: {msg}'
    # exercicio
    # considere