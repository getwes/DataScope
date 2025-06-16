from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
#parte de conexão com o site web
driver = webdriver.Chrome()
driver.get('https://www.olx.com.br/')

step = webdriver.Chrome()
step.get('https://www.pichau.com.br/?gad_source=1&gad_campaignid=1784047387&gbraid=0AAAAADvAK92EhzAbjc1W6PaZtT_S3ms-T&gclid=Cj0KCQjwmK_CBhCEARIsAMKwcD4rEsfRfj3Y-w6CjBfzWbpOlkK-LWUkLPa37pFtER9PHyNNHt5ulboaAvtOEALw_wcB')


ali = webdriver.Chrome()
ali.get('https://pt.aliexpress.com/?src=google&albch=fbrnd&acnt=907-325-7776&isdl=y&aff_short_key=UneMJZVf&albcp=22465909199&albag=178972697235&slnk=&trgt=kwd-14802285088&plac=&crea=737535531803&netw=g&device=c&mtctp=e&memo1=&albbt=Google_7_fbrnd&aff_platform=google&albagn=888888&isSmbActive=false&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=22465909199&gbraid=0AAAAAD2TwoHtkVEEbJfxrEmhwwVJa9f4t&gclid=CjwKCAjwgb_CBhBMEiwA0p3oOMeAVw22R8LgfL4x5EGmlkCXF_1p8ROxWdSLPGHpYsovnFXg7E0VThoCP_cQAvD_BwE&gatewayAdapt=glo2bra')

shopinfo = webdriver.Chrome()
shopinfo.get('https://www.shopinfo.com.br/hardware?srsltid=AfmBOor9lnN379k3qZ28fcgbnnYwnveKevF_QFI7r3DS34IjaRHBvknZ')

sleep(5)

#nome do produto
produtos = driver.find_elements(By.XPATH, "//h2[@class='olx-text olx-text--title-small olx-text--block olx-ad-card__title olx-ad-card__title--vertical']")
produtos2 = step.find_elements(By.XPATH, "//h2[@class='MuiTypography-root MuiTypography-h6 mui-1jecgbd-product_info_title-noMarginBottom']")
produtos3 = ali.find_elements(By.XPATH, "//div[@class='g1_p g1_hg']")
produtos4 = ali.find_elements(By.XPATH, "//div[@class='mz__product-name']")
#preco do prduto
precos = driver.find_elements(By.XPATH, "//div[@class='olx-ad-card__details-price--vertical']")
precos2 = step.find_elements(By.XPATH, "//div[@class='mui-1q2ojdg-price_vista']")
precos3 = ali.find_elements(By.XPATH, "//span[@class='g1_cu jm_h5']")
precos4 = ali.find_elements(By.XPATH, "//span[@class='value d']")

for produto, preco in zip(produtos, precos):
    nome = produto.text.strip()
    valor = preco.text.strip()

    if nome and valor:  # só escreve se ambos não forem vazios
        with open('preços.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{valor}{os.linesep}')

for produto2,preco2 in zip(produtos2,precos2):
    with open('preços.csv', 'a',encoding='utf-8') as arquivo:
        arquivo.write(f'{produto2.text},{preco2.text}{os.linesep}')

for produto3, preco3 in zip(produtos3, precos3):
    nome3 = produto3.text.strip()
    valor3 = preco3.text.strip()

    if nome3 and valor3:  # só escreve se ambos não forem vazios
        with open('preços.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome3},{valor3}{os.linesep}')


for produto4, preco4 in zip(produtos4, precos4):
    nome4 = produto.text.strip()
    valor4 = preco.text.strip()

    if nome4 and valor4:  # só escreve se ambos não forem vazios
        with open('preços.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome4},{valor4}{os.linesep}')
    

driver.quit()
step.quit()
ali.quit()
shopinfo.quit()
input('')

