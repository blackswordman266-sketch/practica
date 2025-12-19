# net_parser.py - Модуль для обработки данных CDP
import re

def extract_cdp_data(command_output):
    """
    Извлекает информацию о соседних устройствах из текста команды 'show cdp neighbors'
    и формирует словарь связей.

    Ключ словаря: (имя_локального_устройства, локальный_интерфейс).
    Значение: (имя_удаленного_устройства, удаленный_интерфейс).
    """
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        if ">" in line or "#" in line:
            hostname = line.split(">")[0].split("#")[0]
        
        columns = line.split()
        if len(columns) >= 5 and columns[3].isdigit():
            r_host = columns[0]
            l_int = columns[1]
            l_int_num = columns[2]
            r_int = columns[6]
            r_int_num = columns[7]
            
            local_key = (hostname, f"{l_int}{l_int_num}")
            remote_value = (r_host, f"{r_int}{r_int_num}")
            
            result[local_key] = remote_value
            
    return result
