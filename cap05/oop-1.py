
#Modelar um celular a seguir
class Celular(object):


    def __init__(self, 
        fabricante:str, modelo:str, 
        tela:float, armazenamento: int, 
        memoria:int, camera:float, 
        bateria:int, tela_ligada:bool):

        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada
        
    
    def ligar_tela(self):
        self.tela_ligada = True

    def verificar_carga_bateria(self):
        """ 
        Utilizar a função random do módulo rabdom
        Printe na tela uma porcenteagem e o valor correspondente em mA
        exem.: Ocelular está com 46% de baterial e 1564mA restantes
        """
        
#instanciando objeto  de forma posicional:
celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21, 3400, False)

#Instanciando objeto de forma não posicional
celular_iphone = Celular(
    fabricante="Apple", 
    modelo="Iphone 13 PRO Max", 
    tela=5.75, 
    armazenamento=128, 
    memoria=4, 
    camera=16, 
    bateria=2650, 
    tela_ligada=False)


celular_iphone.ligar_tela()
#print(celular_iphone.tela_ligada)

