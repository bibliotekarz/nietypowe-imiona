import time
import urllib.request

baby=[]
dziady=[]
with urllib.request.urlopen('https://api.dane.gov.pl/media/resources/20210204/Wykaz_imion_%C5%BCe%C5%84skich_os%C3%B3b_%C5%BCyj%C4%85cych_wg_pola_imi%C4%99_pierwsze_wyst%C4%99puj%C4%85cych_w_rejestrze_PESEL_bez_zgon%C3%B3w.csv') as response:# with open('./pesel_baby.csv', "r", encoding='utf8') as f:
    lines1 = response.read()
    lines = str(lines1, encoding='utf-8')
    zz = lines.split('\r\n')
    for z in zz:
        row = z.split(',')
        if len(row[0]) > 1 and row[0][-1] !='A':
            baby.append(row[0])
print(baby)
print(f'Żeńskich imion nie kończących się na a jest {len(baby)}.')
time.sleep(5)


with urllib.request.urlopen('https://api.dane.gov.pl/media/resources/20210204/Wykaz_imion_m%C4%99skich_os%C3%B3b_%C5%BCyj%C4%85cych_wg_pola_imi%C4%99_pierwsze_wyst%C4%99puj%C4%85cych_w_rejestrze_PESEL_bez_zgon%C3%B3w.csv') as response:
    lines1 = response.read()
    lines = str(lines1, encoding='utf-8')
    zz = lines.split('\r\n')
    for z in zz:
        row = z.split(',')
        if len(row[0]) > 1 and row[0][-1] =='A':
            dziady.append(row[0])
print(dziady)
print(f'Męskich imion kończących się na a jest {len(dziady)}.')
