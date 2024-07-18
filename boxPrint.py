from os import get_terminal_size
from json import loads

def getStyle(style):
    json = loads(open('styles.json').read())
    
    return json['styles'][style].values()
    
def getWidth(string, maxWidth, offset):
    mostLines = max(len(line) for line in string.split('\n'))
    if maxWidth == 'terminal':
        width = get_terminal_size().columns - offset

        if mostLines < width:
            width = mostLines
    else:
        width = maxWidth
    return width
    
def boxPrint(string, style='rounded', dotted=False, width='terminal'):
    string = str(string)
    """
    Função para imprimir um texto dentro de uma caixa estilizada.
    
    Parametros:
        string (str): O texto a ser impresso dentro da caixa.
        style (str, opcional): A estilização da caixa. Padrão é "simple". (Ver arquivo styles.json para mais estilos)
        dotted (bool, opcional): Se a borda da caixa deve ser pontilhada ou não. Padrão é False.
        width (int, optional): A largura da caixa. Padrão é a largura do seu terminal no momento de execução.
    """
    offset, top_left_decor, top_right_decor, bottom_left_decor, bottom_right_decor, vertical_decor, horizontal_decor = getStyle(style)

    width = getWidth(string, width, offset)
    if dotted:
        top_decor = top_left_decor
        bottom_decor = bottom_left_decor
        for i in range(width):
            top_decor += horizontal_decor if (i % 2 == 0) else ' '
            bottom_decor += horizontal_decor if (i % 2 == 0) else ' '
        top_decor += top_right_decor
        bottom_decor += bottom_right_decor
    else:
        top_decor = top_left_decor + (horizontal_decor * width) + top_right_decor
        bottom_decor = bottom_left_decor + (horizontal_decor * width) + bottom_right_decor

    lines = string.split('\n')
    text = ''
    for line in lines:
        if len(line) < width:
            line += ' ' * (width - len(line))
        text += line

    height = len(text) // width if len(text) % width == 0 else len(text) // width + 1
    print(top_decor, sep="")
    for i in range(height):
        print(vertical_decor,end="") if (i % 2 == 0 or not(dotted)) else print(' ',end="")
        for j in range(width):
            if i*(width)+j < len(text):
                char = text[i*(width)+j]
            else:
                char = ' '
            print(char, end="")
        print(vertical_decor) if (i % 2 == 0) or not(dotted) else print(' ')
    print(bottom_decor, sep="") if (height % 2 == 0 or not(dotted)) else print('\n', bottom_decor, sep="")

