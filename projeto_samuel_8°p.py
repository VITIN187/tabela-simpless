from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
import openpyxl
driver = webdriver.Edge()
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

email = driver.find_element(By.XPATH, "//input[@id='email']")

email = driver.find_element(By.XPATH, "//input[@id='email']")

sleep(3)
email.send_keys('samuka.vitin@gmail.com')
senha = driver.find_element(By.XPATH,"//input[@id=senha']")
sleep(5)
senha.send_keys('Yeshu@1883')
botao_entrar = driver.find_element(By.XPATH,"// button[@id=entrar']")
sleep(3)
botao_entrar.click()
empresas = openpyxl.load_workbook('./empresas.xlsx')
paginas_empresas = empresas['dados das empresas do cliente']
for linha in paginas_empresas.iter_rows(min_row=2,values_only=True):
    Nome_da_Empresa, email, Telefone, Endereço, CNPJ, area_de_Atuacao, Quantidade_de_Funcionarios, Data_de_Fundaçao = linha
    data_fundaçao = linha

    driver.find_element(By.ID, 'nomeEmpresa').send_keys(Nome_da_Empresa)
    sleep(1)
    driver.find_element(By.ID, 'email').send_keys(email)
    sleep(1)
    driver.find_element(By.ID, 'telefoneEmpresa').send_keys(Telefone)
    sleep(1)
    driver.find_element(By.ID, 'enderecoEmpresa').send_keys(Endereço)
    sleep(1)
    driver.find_element(By.ID, 'CNPJEmpresa').send_keys(CNPJ)
    sleep(1)
    driver.find_element(By.ID, 'areaatuacao').send_keys(area_de_Atuacao)
    sleep(1)
    driver.find_element(By.ID, 'quantidadefuncionarios').send_keys(Quantidade_de_Funcionarios)
    sleep(1)
    driver.find_element(By.ID, 'datafundacao').send_keys(data_fundaçao)
    sleep(1)

    driver.find_element(By.id, 'Cadastrar').click()
    sleep(3)
