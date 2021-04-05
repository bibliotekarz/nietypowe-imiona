import time
import urllib.request

name=[]
def get_from_pesel(sex):
    if sex == 'K':
        response_source = 'https://api.dane.gov.pl/media/resources/20210204/Wykaz_imion_%C5%BCe%C5%84skich_os%C3%B3b_%C5%BCyj%C4%85cych_wg_pola_imi%C4%99_pierwsze_wyst%C4%99puj%C4%85cych_w_rejestrze_PESEL_bez_zgon%C3%B3w.csv'
        message = 'Żeńskich imion nie kończących się na a jest '
    else:
        response_source = 'https://api.dane.gov.pl/media/resources/20210204/Wykaz_imion_m%C4%99skich_os%C3%B3b_%C5%BCyj%C4%85cych_wg_pola_imi%C4%99_pierwsze_wyst%C4%99puj%C4%85cych_w_rejestrze_PESEL_bez_zgon%C3%B3w.csv'
        message = 'Męskich imion kończących się na a jest '

    with urllib.request.urlopen(response_source) as response:
        lines1 = response.read()
        lines = str(lines1, encoding='utf-8')
        zz = lines.split('\r\n')
        for z in zz:
            row = z.split(',')
            if sex == 'K':
                if len(row[0]) > 1 and row[0][-1] !='A':
                    name.append(row[0])
            else:                    
                if len(row[0]) > 1 and row[0][-1] =='A':
                    name.append(row[0])
    print(name)
    print(message + str(len(name)))


source =''
sex=''
data_complete = False
while data_complete != True:
    
    print(f'zastane source to{source}_')
    if source != 'W' and source != 'P':
        source = input('Wpisz P żeby obrobić dane z bazy (P)ESEL, albo wpisz W żeby przetworzyć listę imion z (W)ikipedii.\n :')
        source = source.upper()
        print('Literówka jakaś?\n')
        print(f'wprowadzone source to {source}')
        continue
    else:
        print('Idziemy dalej')
        if sex != "K" and sex != "M":
            sex = input('Wpisz K żeby wybrać imiona (K)obiece, albo wpisz M żeby wybrać imiona (M)ęskie.\n :')
            sex = sex.upper()
            print('Literówka jakaś?\n')
            print(f'wprowadzona płeć to {sex}')
            continue
        else:
            data_complete = True
            print(f'Wybrałeś źródło {source} i płeć {sex}')
            if source == 'P':
                get_from_pesel(sex)
            else:
                get_from_wiki(sex)
