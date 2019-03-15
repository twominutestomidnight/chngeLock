from xlrd import open_workbook
from camera import Camera
import configparser
from ChangeLock import changeLogTries
import datetime



if __name__ == '__main__':
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini')
    #print(config_ini['DEFAULT']['program_mode'])

    book = open_workbook(config_ini['DEFAULT']['read_file'], 'utf-8')
    sheet = book.sheet_by_index(0)
    dict_list = []
    keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in range(sheet.ncols)}
        dict_list.append(d)



    camerasArray = []

    for index in range(len(dict_list)):

        camerasArray.append(Camera(ip=dict_list[index]['ip'], port=int(dict_list[index]['port']),
                                   login=dict_list[index]['login'],password=dict_list[index]['password']))


    #result = open(config_ini['DEFAULT']['path_to_save_file'], "w", encoding='utf8')

    log = open(config_ini['DEFAULT']['log_file'], 'w')
    for camer in camerasArray:
        print(camer)
        status = changeLogTries(camer.ip, camer.port, camer.login, camer.password)
        log.write("{}:{}\t{}\n".format(camer.ip, camer.port, status))




