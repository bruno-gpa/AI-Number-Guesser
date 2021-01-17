# AI-Number-Guesser

## Objetivo e funcionamento
O objetivo do projeto foi aplicar uma rede neural para adivinhar o número desenhado pelo usuário. O input dos dados é feito em uma tela em branco que é salva como imagem png e, em seguida, transformada em uma matriz 128 x 128 onde cada número representa um pixel. Essa matriz é submetida a rede neural pré-treinada com a MNIST database de números manuscritos e a previsão é postada na tela.

## Ferramentas utilizadas
- Python
- Pygame
- Keras/Tensorflow
- PIL
- Numpy
- Tkinter

## Resultados
A rede neural apresenta precisão de 90% com o dataset MNIST e acerta boa parte dos números desenhados com clareza. Desvios pequenos do padrão ao qual a rede neural está acostumada causam erros. O programa tem uma dificuldade particular em adivinhar o número 9.
