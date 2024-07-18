# boxPrint

O boxPrint é uma função Python que imprime texto dentro de uma caixa decorativa no terminal. Esta função foi criada para ajudar na organização e visibilidade de mensagens, especialmente útil para iniciantes em programação.

* **Estilo Personalizado:** Escolha entre diferentes estilos de borda definidos em um arquivo JSON.
* **Inclua seu próprio estilo:** Inclua sua própria personalização no arquivo styles.json
* **Modo Pontilhado:** Opção para exibir a borda da caixa de forma pontilhada, adicionando um visual diferenciado.
* **Largura Ajustável:** Adapte a largura da caixa para se ajustar ao tamanho do terminal ou defina um valor específico.

## Instalação

* Baixe o arquivo .zip e extraia 'boxPrint.py' e 'styles.json' para a mesma pasta aonde deseja usar.
* Faça a importação:
  ```python
  from boxPrint.py import boxPrint
  ```
## Exemplos
```python
from boxPrint.py import boxPrint

#Para imprimir com as opções padrões
boxPrint("Hello World!")

#Para selecionar o estilo rounded, ativar pontilhado e limitar a largura para 1:
boxPrint("Hello World!",style="rounded", dotted=True, width=1)
```

Resultados
```
╭────────────╮
│Hello World!│
╰────────────╯

╭─╮
│H│
 e 
│l│
 l 
│o│
   
│W│
 o 
│r│
 l 
│d│
 ! 
╰─╯
```


