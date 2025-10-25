# heart_and_face
## main.py
O código 'main.py' funciona a partir do framework MediaPipe, utilizando da solução 'FACE_MESH' para coletar os landmarks da face. Utilizando os pontos de números 468 e 158, o código mede a distância entre o centro do olho e a pálpebra esquerda. A partir da biblioteca 'time', ele é capaz de cronometrar a execução do programa. Com estes dados, o código cria ou atualiza um arquivo 'data.csv', extensão que separa valores por linhas e colunas, nesse caso sendo as colunas ypos e time, tornando-o sensível a quando a pálpebra se move em relação ao olho.
## view_data.py
Este segundo programa realiza a análise dos dados coletados pelo programa anterior, oferecendo diversas funções para observação, dentre elas:
* get_rows(): retorna a quantidade de pares 'tempo' e 'posição' o código coletou.
* show_ypos() e show_time(): listam, respectivamente, as colunas de posição e de tempo.
* calc_avg(): calcula a distância média entre os landmarks.
* find_peak(): obtém o pico de proximidade da pálpebra em relação ao olho.
* get_freq(): por meio das funções anteriores, calcula a frequência com a qual a proximidade dos landmarks supera a média por um valor especificado em um intervalo de tempo também especificados. Recebe o tempo onde inicia e termina a análise e por quanto a proximidade supera a média.
