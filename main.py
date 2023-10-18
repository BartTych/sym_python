
import os
import numpy as np
import time


from os.path import exists

# wiec robie tak
# mam w pythonie petle z danymi tego jak bedzie smigac symulacja
    # robie plik konfiguracyjny txt dla symulacji C#
    # odpalam symulacje (ona odczytuje dane z pliku konfiguracyjnego)
    # czekam az sie policzy i co 3s sprawdzam czy jest juz plik z wynikami
    # odczytuje wynik sym i dopisuje do wyniku
    # usuwam plik z wynikami
# wrzucam wynik_koncowy do pliku tak jak w c#

def prepare_sym_config_file(file, path, DC_size, DC_shift, sort_size, sort_shift):
    file_exists = exists(path + file)

    if not file_exists:
        f = open(path + file, "x")
    else:
        f = open(path + file, "w")

    f.write("DC_size, DC_shift, sort_size, sort_shift"+'\n')
    f.write(f'{DC_size},{DC_shift},{sort_size},{sort_shift}')
    f.close()

def read_and_del_file(file_neme, path):
    f = open(path + file_neme, "r")
    zawartosc = f.read()
    f.close()
    # os.remove(path + file_neme)
    return int(zawartosc[:-1])

def save_final_results_in_file(file, path,list_of_results, list_of_DC_size, list_of_DC_shift):
    file_exists = exists(path + file)

    if not file_exists:
        f = open(path + file, "x")
    else:
        f = open(path + file, "w")

    _str = ''
    for i, n in enumerate(list_of_DC_size):
        if i != 0:
            _str += ','
        _str += str(n)
    f.write(_str + '\n')

    _str = ''
    for i, n in enumerate(list_of_DC_shift):
        if i != 0:
            _str += ','
        _str += str(n)
    f.write(_str + '\n')
    f.write("DC_size, DC_shift, sort_size, sort_shift, number_of_rides" + '\n')

    for i, n in enumerate(list_of_DC_size):
        for j, m in enumerate(list_of_DC_shift):
            f.write(f'{list_of_DC_size[i]},{list_of_DC_shift[j]},{list_of_DC_size[i]*2},0,{list_of_results[i][j]}' + '\n')
    f.close()

    # List_of_DC_size
    # List_of_DC_shift
    # opis co jest co wynikach w jednym wierszu
    # wyniki w jednym wierszu ma spis konfiguracji i liczbe przejazdow





def run_symulation(file, path, DC_size, DC_shift, sort_size, sort_shift):

    #prepare_sym_config_file('config.txt', '', DC_size, DC_shift, sort_size, sort_shift)

    os.system("dotnet run --project /Users/bart/python/repository/TransSym/Transport")

    return read_and_del_file(file,'')

number_of_repetitons = 2

list_of_results = []
list_of_DC_size = np.linspace(4, 20, 25)
list_of_DC_shift = np.linspace(0, 6, 25)

for DC_size in list_of_DC_size:
    list_of_results_for_size = []
    for DC_shift in list_of_DC_shift:

        prepare_sym_config_file('sym_config.txt', '', DC_size, DC_shift, DC_size*2, 0)

        wynik = 0

        for n in range(number_of_repetitons):
            wynik += run_symulation('sym_result.txt', '/Users/bart/python/repository/TransSym/', DC_size, DC_shift, DC_size * 2, 0)

        list_of_results_for_size.append(int(wynik / number_of_repetitons))
    list_of_results.append(list_of_results_for_size)

print(list_of_results)
save_final_results_in_file('final_results.txt','', list_of_results, list_of_DC_size, list_of_DC_shift)
#for DC_size in np.linspace(4,15,44,endpoint = True):
#    for DC_shift in np.linspace(0,5,5, endpoint = True):
#        for i in range(2):
#            pass
            # method run sym
            # save result
        # save result in final result file