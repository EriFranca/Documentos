import pyautogui
import time
import pygetwindow as gw

# 1 - Verificar se existe uma janela do SAP aberta
# Implemente a lógica de verificação da janela do SAP aberta de acordo com suas necessidades
# Função para verificar se uma janela do SAP está aberta
def is_sap_window_open():
    sap_window_title = "SAP"  # Título da janela do SAP (pode variar, ajuste conforme necessário)
    sap_window = gw.getWindowsWithTitle(sap_window_title)

    return len(sap_window) > 0

if not is_sap_window_open():
    print("A janela do SAP não está aberta. Por favor, abra o SAP e execute o script novamente.")
    exit()
    
# 2 - Acessar a transação /OZFIR002
# Pressionar a combinação de teclas para acessar a transação
pyautogui.hotkey('ctrl', '/')

# Esperar um tempo para o SAP abrir
time.sleep(5)

# Digitar a transação /OZFIR002
pyautogui.write('/OZFIR002')
pyautogui.press('enter')

# Esperar um tempo para a transação abrir
time.sleep(5)

# 3 - Configurar data e loja nos locais adequados
# Implemente a lógica para configurar data e loja de acordo com suas necessidades

# 4 - Exportar o relatório gerado
# Implemente a lógica para exportar o relatório de acordo com suas necessidades

# 5 - Selecionar o arquivo excel gerado
# Implemente a lógica para selecionar o arquivo excel de acordo com suas necessidades

# 6 - Copiar as informações na coluna G
# Implemente a lógica para copiar as informações da coluna G de acordo com suas necessidades

# 7 - Abrir o Chrome na página "https://fiscal.com.br"
pyautogui.hotkey('winleft', 'r')  # Pressionar a tecla Windows + R para abrir Executar
time.sleep(1)
pyautogui.write('chrome https://fiscal.com.br')  # Digitar o comando para abrir o Chrome com a URL
pyautogui.press('enter')

# Esperar um tempo para o Chrome abrir e a página carregar
time.sleep(10)
