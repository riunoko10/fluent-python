#pagina 45
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


color = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in color for size in sizes]