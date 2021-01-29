from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime



class InstagramBot:
  def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\userAD\Desktop\geckodriver.exe"
        )

  def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        driver.minimize_window()
        time.sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.click()
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(1)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.click()
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos()
     
  @staticmethod
  def digite_como_uma_pessoa(frase, onde_digitar):
      for letra in frase:
          onde_digitar.send_keys(letra)
          time.sleep(random.randint(1,5)/30)

  def comente_nas_fotos(self):
        driver = self.driver
        driver.get('your_photo_url') #//Aqui voce insere o link da foto que deve ser comentada 
        time.sleep(3)
        driver.minimize_window()
        contator =0
        while 1:
            print('Processando...')
            try:
                #// aqui voce insere seus comentáros 
                comentarios = ['Boa!', 'Massa!', 'Que Afude!', 'Vamos tentar a sorte então!', 'Dale!', 'Vamo Dale!', 'Baita Sorteio!', 'Vai que dá', 'Comentando pra tentar a sorte!'
                ,'A esperança é a ultima que morre', 'Vamo!', 'Comenando pra ver se ganho!', 'Comentários da esperança', 'Essa vai da bom',
                'Ihull!', 'Opaaa!', 'Eba!']
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                comentario = random.choice(comentarios)
                self.digite_como_uma_pessoa(comentario,campo_comentario)
                time.sleep(random.randint(2,10))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                contator = contator +1
                print("Comentado com Sucesso!\nO comentário ",contator," foi: " +comentario)
                time.sleep(random.randint(15,20))
            except Exception as e:
                print(e)
                print("Morri")
                driver.quit()
                print("Fechei o navegador")
                print("Daqui 1 minuto inicio novamente")
                time.sleep(60)
                print("Estou iniciando")
                

                bot = InstagramBot('your_user', 'your_password')
                bot.login()
                driver.minimize_window()
                print("Efetuando Login Novamente")
                #//Criar funcao de login 

               


        
        #//Ypffh"

bot= InstagramBot('your_user', 'your_password')
bot.login()
