# Trabalho Prático de Computação Gráfica - 01

Sofia França Campos Bhering 
665173 


## Organização:

O código está organizado em 4 arquivos diferentes, específicos para cada caso:

│
├── main.py                     
# Arquivo principal que inicializa a aplicação
├── clipping.py                
 # Implementação dos algoritmos de recorte
├── line_drawing.py             
# Implementação dos algoritmos de rasterização
└── transformations.py           
# Implementação das transformações geométricas


# Descrição dos Arquivos

# main.py
Este é o ponto de entrada da aplicação. Ele inicializa a interface gráfica e configura a aplicação, permitindo que o usuário interaja com os diferentes módulos. O arquivo gerencia a criação da janela principal, exibição de menus e chamadas das funções dos outros arquivos conforme as interações do usuário.

# clipping.py 
Este arquivo contém a implementação dos algoritmos de recorte, que são essenciais para limitar as seções de linhas ou formas exibidas na interface. Ele aborda:
    # Cohen-Sutherland:
 Um algoritmo que utiliza regiões codificadas para determinar se uma linha deve ser desenhada completamente, parcialmente ou não deve ser desenhada de modo algum, baseado em sua posição em relação a uma área de recorte.
    # Liang-Barsky: 
Um algoritmo que utiliza a equação paramétrica para realizar o recorte de linhas, sendo mais eficiente em muitos casos do que o Cohen-Sutherland.

# line_drawing.py:
Este arquivo é responsável pela implementação dos algoritmos de rasterização, permitindo que as formas sejam desenhadas na interface gráfica. Ele inclui:
    # DDA (Digital Differential Analyzer): 
Um algoritmo que gera os pontos que formam uma linha entre dois pontos dados, com base na inclinação da linha.
    # Bresenham: 
Um algoritmo mais eficiente que determina os pontos de uma linha, minimizando a quantidade de cálculos necessários. Ele também pode incluir a implementação para desenhar circunferências usando uma versão do algoritmo de Bresenham.

# transformations.py:
Este arquivo contém a implementação das transformações geométricas 2D que o usuário pode aplicar às figuras. As funções implementadas permitem que o usuário informe os fatores de transformação, sem valores fixos, e incluem:
    #Translação: 
Move a figura em uma direção específica, baseada nos valores de deslocamento fornecidos pelo usuário.
    #Rotação: 
Gira a figura em torno de um ponto (geralmente a origem) com um ângulo informado pelo usuário.
Escala: Redimensiona a figura com fatores de escala que o usuário pode definir.
    #Reflexões: 
Permitem que o usuário reflita a figura em torno dos eixos X, Y ou ambos, usando os parâmetros fornecidos.

## Como Usar: 

Requerimentos : ter instalado o git, python v >= 3.9, tkinter e math

Modo de Execução :

- clone o repositório (ou baixe como zip)
git clone git@github.com:sofiabhering/tp1-cg.git


# Como Utilizar

1. **Desenhar Objetos na Tela utilizando os Algoritmos de Rasterização**:
   - Clique com o botão esquerdo do mouse para selecionar **dois pontos** na tela. Em seguida, acesse o menu de **Rasterização** e escolha entre os algoritmos **DDA** ou **Bresenham** para desenhar a linha.
   - Para desenhar uma **circunferência** usando o algoritmo de **Bresenham**, clique com o botão esquerdo para selecionar **um ponto** central na tela e informe o **raio** da circunferência quando solicitado.

2. **Aplicar Transformações Geométricas 2D no Objeto Desenhado**:
   - Acesse o menu de **Transformações** e escolha o algoritmo desejado. Em seguida, insira os valores requeridos para a transformação e observe o resultado aplicado ao objeto desenhado.

3. **Aplicar os Algoritmos de Recorte**:
   - Desenhe objetos na tela utilizando os algoritmos **DDA** ou **Bresenham**.
   - Clique com o botão direito do mouse para selecionar os pontos **mínimo** e **máximo**, que definirão a **janela de recorte** (representada por um retângulo vermelho).
   - No menu de **Recorte**, escolha o algoritmo desejado (Cohen-Sutherland ou Liang-Barsky) para realizar o recorte da figura.
   - Você pode repetir o processo, alterando a janela de recorte conforme necessário.

**Obs: para melhores exemplos na prática, verifique a pasta prints, lá está disponível imagens da demonstração do programa na prática**