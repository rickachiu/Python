class ai:
    def __init__(self,**kwargs):
        self.variables = kwargs
    def create_brain(self, k, v):
        self.variables[k] = v
    def getvar(self, k):
        return self.variables.get(k)

def main():
    ac = ai()
    ac.create_brain('neuron', '882')
    ac.create_brain('type','machine learning')
    ac.create_brain('software', 'tensorflow')
    print(ac.getvar('neuron'))
    print(ac.getvar('type'))
    print(ac.getvar('software'))

main()