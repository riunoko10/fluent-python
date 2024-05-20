#pagina 45
symbols = '$¢£¥€¤'
codes = []

#En el código proporcionado, 
# ord(symbol) devolverá el valor Unicode 
# del carácter contenido en la variable symbol.

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]
# Listcomps Versus map and filter

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))


# Cartesian Products

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

tshirts2 = [(color, size) 
            for size in sizes 
            for color in colors]

print(tshirts2)

## Generator Expressions
#Las expresiones generadoras usan 
# la misma sintaxis que las comprensiones de listas, 
# pero están encerradas entre paréntesis en lugar de corchetes.
symbols = '$¢£¥€¤'
list_item = tuple(ord(symbol) for symbol in symbols)
print(list_item)


## Inicializar un array con un generador
import array
array_item = array.array('I', (ord(symbol) for symbol in symbols))



## Producto cartesiano en una expresión generadora
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)