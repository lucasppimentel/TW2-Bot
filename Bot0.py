from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import random as rd

navegador = webdriver.Chrome('[webdriver directory here]')
navegador.get('https://br.tribalwars2.com/page#/')
actions = ActionChains(navegador)
time.sleep(1)


def nivel(ids):
    a = navegador.find_element_by_xpath('//*[@id="{}"]/a/span[2]/span'.format(ids)).text
    if a.find('\n') > 0:
        return int(a[0:a.find('\n')]) + 1
    elif a == '':
        return 0
    else:
        return int(a)


Login = navegador.find_element_by_xpath("//input[@placeholder='Nome do jogador']")
Login.send_keys('[your login]')  # Login
Senha = navegador.find_element_by_xpath("//input[@placeholder='Senha']")
Senha.send_keys('[your password]')  # Senha
Senha.send_keys(Keys.ENTER)
time.sleep(4)

# colocar nome do mundo assim -> contains(.,"login (nome do mundo)"), esse é o texto do mundo qnd vc clica em jogar
mundo = navegador.find_element_by_xpath('//*[text()[contains(.,"[login (world name)]')
mundo.click()
time.sleep(15)  # usar wait.until

try:
    Recompensa = navegador.find_element_by_xpath('//*[@id="twx-w1"]/div/div/div/div/footer/ul/li')
except NoSuchElementException:
    pass
else:
    Recompensa.click()

navegador.find_element_by_class_name('icon-60x60-settings').click()
time.sleep(0.5)
navegador.find_element_by_xpath('//*[@id="settings"]/div/div[1]/div/div[2]/div/div/div/a/span').click()
navegador.find_element_by_xpath('//*[@id="settings"]/div/div[2]/div/div[2]/table[1]/tbody/tr[4]/td[2]/label').click()
mus = navegador.find_element_by_xpath(
    '//*[@id="settings"]/div/div[2]/div/div[2]/table[4]/tbody/tr[2]/td[2]/a')
actions.move_to_element(mus).perform()
navegador.find_element_by_xpath('//*[@id="settings"]/div/div[2]/div/div[2]/table[3]/tbody/tr[2]/td[1]/label').click()
navegador.find_element_by_css_selector('a.size-34x34.btn-red.icon-26x26-close[ng-click="closeWindow()"]').click()
Aldeia = navegador.find_element_by_xpath('/html/body/div[2]/footer/div/div[2]/a[4]')
Aldeia.click()
time.sleep(4)  # carregando aldeia

# ------------------------------------------Nível dos edifícios básicos-----------------------------------
nivelQuartel = nivel('label-barracks')
nivelHq = nivel('label-headquarter')
nivelArmazem = nivel('label-warehouse')
nivelMina = nivel('label-iron_mine')
nivelPoco = nivel('label-clay_pit')
nivelBosque = nivel('label-timber_camp')
nivelFazenda = nivel('label-farm')
nivelPe = nivel('label-rally_point')
# ------------------------------------------Posição dos edifícios(dentro da aldeia)-----------------------
time.sleep(2)
quartel = navegador.find_element_by_id('label-barracks')
hq = navegador.find_element_by_id('label-headquarter')
armazem = navegador.find_element_by_id('label-warehouse')
fazenda = navegador.find_element_by_id('label-farm')
poco = navegador.find_element_by_id('label-clay_pit')
bosque = navegador.find_element_by_id('label-timber_camp')
mina = navegador.find_element_by_id('label-iron_mine')
pe = navegador.find_element_by_id('label-rally_point')
# --------------------------------------------------------------------------------------------------------
ordem = ['min', 'poc', 'bos', 'pon', 'arm', 'faz', 'faz', 'min', 'bos', 'poc', 'arm', 'poc', 'bos', 'faz', 'mad',
         'hea', 'arm', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'faz', 'min',
         'bos', 'poc', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'faz', 'faz' 'arm', 'faz' 'qua',
         'qua', 'hea', 'hea', 'hea', 'faz', 'arm', 'arm', 'faz' 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'min', 'bos',
         'poc', 'min', 'bos', 'poc', 'faz', 'arm', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'min', 'bos', 'poc', 'min',
         'bos', 'poc', 'faz' 'qua', 'qua', 'qua', 'qua', 'arm', 'arm', 'qua', 'qua', 'arm', 'arm', 'arm', 'arm', 'arm',
         'faz' 'qua', 'qua', 'qua', 'qua']

if int(nivelArmazem) + int(nivelMina) + int(nivelPoco) + int(nivelBosque) + int(nivelPe) + int(nivelFazenda) \
        + int(nivelHq) + int(nivelQuartel) - 5 >= 14:
    i = int(nivelArmazem) + int(nivelMina) + int(nivelPoco) + int(nivelBosque) + int(nivelPe) + int(nivelFazenda) \
        + int(nivelHq) + int(nivelQuartel) - 4
else:
    i = int(nivelArmazem) + int(nivelMina) + int(nivelPoco) + int(nivelBosque) + int(nivelPe) + int(nivelFazenda) \
        + int(nivelHq) + int(nivelQuartel) - 5

tic = time.perf_counter()


#  -----------------------------------------------attack---------------------------------------------------------------


def attack(x, y):
    navegador.find_element_by_id('world-map').click()
    navegador.find_element_by_xpath('//input[@ng-model="coordinates.x"]').send_keys(
        Keys.ARROW_RIGHT * 3, Keys.BACKSPACE * 3)
    navegador.find_element_by_xpath('//input[@ng-model="coordinates.x"]').send_keys(x)
    navegador.find_element_by_xpath('//input[@ng-model="coordinates.y"]').send_keys(
        Keys.ARROW_RIGHT * 3, Keys.BACKSPACE * 3)
    navegador.find_element_by_xpath('//input[@ng-model="coordinates.y"]').send_keys(y)
    navegador.find_element_by_xpath('//div[@ng-click="jumpTo(coordinates)"]').click()
    time.sleep(4)
    navegador.find_element_by_xpath('//div[@tooltip-content="Predefinições"]').click()
    time.sleep(4)
    navegador.find_element_by_class_name('btn-orange.size-20x20.btn-border.btn-preset-info.icon-26x26-info').click()
    time.sleep(1)
    navegador.find_element_by_css_selector('a.btn-red.icon-26x26-close[ng-click="closeWindow()"]').click()
    time.sleep(1)
    try:
        botaoa = navegador.find_element_by_xpath('//*[text()[contains(.,"predefa")]]/../../../tr[2]/td[3]/a')
        botaob = navegador.find_element_by_xpath('//*[text()[contains(.,"predefb")]]/../../../tr[2]/td[3]/a')
    except NoSuchElementException:
        navegador.find_element_by_css_selector('a.btn-red.icon-26x26-close[ng-click="closeWindow();"]').click()
    else:
        if 'ff-fix btn-max size-42x42 icon-34x34-attack btn-orange' in str(botaoa.get_attribute('outerHTML')):
            botaoa.click()
        elif 'ff-fix btn-max size-42x42 icon-34x34-attack btn-orange' in str(botaob.get_attribute('outerHTML')) \
                and -1 == botaoa.get_attribute('outerHTML').find('ff-fix btn-max size-42x42 icon-34x34-attack '
                                                                 'btn-orange'):
            botaob.click()
        else:
            navegador.find_element_by_css_selector('a.btn-red.icon-26x26-close[ng-click="closeWindow();"]').click()


#  ----------------------------------------------build---------------------------------------------------


def build(cons):
    global i
    try:
        if str(cons.size) == "{'height': 0, 'width': 0}":
            lv = navegador.find_element_by_css_selector('div.border[ng-switch-when="levelup"]')
            if lv.is_displayed():
                lv.click()
                i = i + 1
            else:
                lvc = navegador.find_element_by_css_selector('div.border[ng-switch-when="levelup-construct"]')
                if lvc.is_displayed():
                    lvc.click()
                    i = i + 1
                else:
                    pass
        else:
            cons.click()
            lv = navegador.find_element_by_css_selector('div.border[ng-switch-when="levelup"]')
            if lv.is_displayed():
                lv.click()
                i = i + 1
            else:
                lvc = navegador.find_element_by_css_selector('div.border[ng-switch-when="levelup-construct"]')
                if lvc.is_displayed():
                    lvc.click()
                    i = i + 1
                else:
                    pass
    except ElementClickInterceptedException as exc:
        print(exc)
        pass


#  -------------------------------------------recrutar----------------------------------------------------------


def recrutar(un_id, quant):
    quartel = navegador.find_element_by_id('label-barracks')
    quartel.click()
    navegador.find_element_by_class_name('menu-highlight').click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../../../..'.format(un_id)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../../../..'.format(un_id)).send_keys('{}'.format(
        quant))
    navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../../../..'.format(un_id)).send_keys(Keys.ENTER)
    navegador.find_element_by_css_selector('a.size-34x34.btn-red.icon-26x26-close[ng-click="closeWindow()"]').click()


# --------------------------------------------predef----------------------------------------------------------
if nivelPe < 2:
    pe.click()
    navegador.find_element_by_class_name('menu-highlight').click()
    time.sleep(2)
    navegador.find_element_by_css_selector('a.btn-orange.btn-border[ng-click="createPreset();"]').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//input[@placeholder="Digite o nome da predefinição"]').send_keys('predefa')
    navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[text()[contains(.,"Ok")]]/..').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[text()[contains(.,"Lanceiro")]]/../Input').send_keys('10')
    navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()  # predefa criada
    time.sleep(1)
    navegador.find_element_by_css_selector('a.btn-orange.btn-border[ng-click="createPreset();"]').click()  # predefb
    time.sleep(1)
    navegador.find_element_by_xpath('//input[@placeholder="Digite o nome da predefinição"]').send_keys('predefb')
    navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[text()[contains(.,"Ok")]]/..').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[text()[contains(.,"Viking")]]/../Input').send_keys('10')
    navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
    navegador.find_element_by_css_selector('a.btn-red.icon-26x26-close[ng-click="closeWindow()"]').click()

# -----------------------------------------------Início do while--------------------------------------------
while not navegador.find_element_by_xpath('//*[@id="twx"]/body').is_enabled() == 'chrome not reachable':
    toc = time.perf_counter()

    # -------------------------------------Analisa recursos-------------------------------------------------
    Pontos = int(navegador.find_element_by_xpath('//*[@id="info-player-money"]/div[2]').text.replace('.', ''))
    madeira = int(navegador.find_element_by_xpath('//*[@id="resources-wrapper"]/div[1]/div[2]/div[1]').text.replace(
        '.', ''))
    ferro = int(navegador.find_element_by_xpath('//*[@id="resources-wrapper"]/div[3]/div[2]/div[1]').text.replace(
        '.', ''))
    argila = int(navegador.find_element_by_xpath('//*[@id="resources-wrapper"]/div[2]/div[2]/div[1]').text.replace(
        '.', ''))
    populacao = int(navegador.find_element_by_xpath('//*[@id="resources-wrapper"]/div[4]/div[2]/div[1]').text.replace(
        '.', ''))
    # -----------------------------------------attack------------------------------------------------------
    while toc - tic > 300:
        nivelQuartel = nivel('label-barracks')
        barbaros = ['492', '429', '490', '434', '489', '426', '495', '432']  # coords das aldeias: 'x', 'y', 'x1', 'y1'
        z = rd.randint(1, int(len(barbaros) / 2) - 1) * 2  # ataca as aldeias em ordem aleatoria
        for tt in range(0, int(len(barbaros) / 2)):
            attack(barbaros[z], barbaros[z + 1])
        Aldeia.click()
        time.sleep(2)
        try:
            Aldeia.click()
        except ElementNotInteractableException:
            pass

        time.sleep(4)
        if madeira > 900 and argila > 900 and 900 < ferro < madeira:
            recrutar('Lanceiro', '10')
        elif madeira > 900 and argila > 900 and 900 < madeira < ferro and nivelQuartel > 3:
            recrutar('Espadachim', '8')
        else:
            pass
        tic = time.perf_counter()

    # --------------------------------------Recompensa das missões------------------------------------------
    try:  # tenta abrir a missão 1
        M1 = navegador.find_element_by_xpath('//*[@id="interface-quests"]/div/div[1]/ul/li[1]')  # Pega a 1a missão
        if 'quest-line-item first quest-line-finishable' in str(
                M1.get_attribute('outerHTML')):  # Se tiver completa, clica
            M1.click()
        elif 'quest-line-item first quest-line-unread' in str(M1.get_attribute('outerHTML')):
            M1.click()
        else:
            pass
    except:
        pass

    try:  # tenta abrir a missão 2
        M2 = navegador.find_element_by_xpath('//*[@id="interface-quests"]/div/div[1]/ul/li[2]')
        if 'quest-line-item quest-line-finishable' in str(M2.get_attribute('outerHTML')):
            M2.click()
        elif 'quest-line-item quest-line-unread' in str(M2.get_attribute('outerHTML')):
            M2.click()
        else:
            pass
    except:
        pass

    try:  # tenta abrir a missão 3
        M3 = navegador.find_element_by_xpath('//*[@id="interface-quests"]/div/div[1]/ul/li[3]')
        if 'quest-line-item quest-line-finishable' in str(M3.get_attribute('outerHTML')):
            M3.click()
        elif 'quest-line-item quest-line-unread' in str(M3.get_attribute('outerHTML')):
            M3.click()
        else:
            pass
    except:
        pass
    finally:
        time.sleep(1.5)  # Espera carregar a missão

    try:  # tenta pegar a recompensa das missões
        RecMissao = navegador.find_element_by_xpath("//*[contains(text(), 'Finalizar Missão')]")
    except:
        try:
            navegador.find_element_by_css_selector('a.btn-red.icon-26x26-close[ng-click="closeWindow()"]').click()
        except:
            pass
        else:
            pass
    else:
        RecMissao.click()
        try:
            navegador.find_element_by_css_selector('a.btn-red.icon-26x26-close[ng-click="closeWindow()"]').click()
        except:
            pass
        else:
            pass
    # --------------------------------------------------Construção-------------------------------------------------
    quartel = navegador.find_element_by_id('label-barracks')
    hq = navegador.find_element_by_id('label-headquarter')
    armazem = navegador.find_element_by_id('label-warehouse')
    fazenda = navegador.find_element_by_id('label-farm')
    poco = navegador.find_element_by_id('label-clay_pit')
    bosque = navegador.find_element_by_id('label-timber_camp')
    mina = navegador.find_element_by_id('label-iron_mine')
    pe = navegador.find_element_by_id('label-rally_point')

    if ordem[i] == 'arm':
        armazem = navegador.find_element_by_id('label-warehouse')
        build(armazem)

    elif ordem[i] == 'poc':
        poco = navegador.find_element_by_id('label-clay_pit')
        build(poco)

    elif ordem[i] == 'min':
        mina = navegador.find_element_by_id('label-iron_mine')
        build(mina)

    elif ordem[i] == 'bos':
        bosque = navegador.find_element_by_id('label-timber_camp')
        build(bosque)

    elif ordem[i] == 'pon':
        pe = navegador.find_element_by_id('label-rally_point')
        build(pe)

    elif ordem[i] == 'faz':
        fazenda = navegador.find_element_by_id('label-farm')
        build(fazenda)

    elif ordem[i] == 'hea':
        hq = navegador.find_element_by_id('label-headquarter')
        build(hq)

    elif ordem[i] == 'qua':
        quartel = navegador.find_element_by_id('label-barracks')
        build(quartel)

    elif ordem[i] == 'mad':
        navegador.find_element_by_id('inventory-button').click()
        time.sleep(1)
        navegador.find_element_by_xpath('//*[text()[contains(.," Usar Item ")]]/..').click()
        time.sleep(0.5)
        navegador.find_element_by_css_selector('a.btn-orange.btn-border[ng-click="confirm()"]').click()
        navegador.find_element_by_css_selector('a.size-34x34.btn-red.icon-26x26-close[ng-click="closeWindow()"]')
        i = i + 1

    # ---------------------------------recrutamento------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------
    finish = navegador.find_element_by_xpath('//*[@id="interface-building-queue"]/div/ul/li[1]/div[1]/div/div[1]/a')
    if finish.is_displayed():
        finish.click()
    else:
        pass
print('Fim')

# label-chapel
# label-clay_pit
# label-farm
# label-headquarter
# label-iron_mine
# label-rally_point
# label-timber_camp
# label-warehouse
# label-hospital
# label-preceptory
# label-academy
# label-tavern
# label-market
# label-wall
