# This entrypoint file to be used in development. Start by reading README.md
from mean_var_std import asking, calculate
#from unittest import main

#Aqui precisei definir o número no escopo global para que ele também possa ser utilizado pelo calculate
numero = asking()
calculate(numero)
#print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
#main(module='test_module', exit=False)