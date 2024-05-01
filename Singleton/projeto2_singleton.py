class SanidadeCheck:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        return SanidadeCheck.__instance
    
    def __init__(self):
        self._servidores = []
        
    def checar_servidor(self, srv):
        print(f'Checando o', self._servidores[srv])
    
    def add_servidor(self):
        self._servidores.append('Servidor 1')
        self._servidores.append('Servidor 2')
        self._servidores.append('Servidor 3')
        self._servidores.append('Servidor 4')
    
    def mudar_servidor(self):
        self._servidores.pop()
        self._servidores.append('Servidor 5')
        
sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()
print('Cronograma de checagem de sanidade dos servidores A...')
for srv in range(4):
    sc1.checar_servidor(srv)

sc2.mudar_servidor()
print('Cronograma de checagem de sanidade dos servidores B...')
for srv in range(4):
    sc2.checar_servidor(srv)
    
    