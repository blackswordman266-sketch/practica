# parse_cdp_neighbors.py - Вспомогательный модуль для парсинга вывода 'show cdp neighbors'
import re

def parse_cdp_neighbors(command_output):
    """
    Обрабатывает вывод команды 'show cdp neighbors' и возвращает словарь
    с информацией о соединениях.

    Ключ словаря - кортеж (имя_локального_устройства, локальный_интерфейс).
    Значение - кортеж (имя_удаленного_устройства, удаленный_интерфейс).
    """
    result = {}
    # Разделяем вывод на строки
    for line in command_output.split("\n"):
        line = line.strip()
        # Ищем имя локального устройства в строке с приглашением (prompt)
        if ">" in line or "#" in line:
            # Предполагаем, что имя устройства - это часть до первого ">" или "#"
            hostname = line.split(">")[0].split("#")[0]
        
        # Парсим строки с соседями
        # Пропускаем строки, которые не содержат информацию о соседе
        # 3-й столбец (индекс 3) - Holdtime, он всегда должен быть числом
        columns = line.split()
        if len(columns) >= 5 and columns[3].isdigit():
            # Пример строки: R1 Eth 0/1 120 R S I C3750 Eth 0/0
            # columns[0] - Remote Device ID (r_host)
            # columns[1] - Local Intrfce (l_int)
            # columns[2] - Local Intrfce number (l_int_num)
            # columns[6] - Remote Port ID (r_int)
            # columns[7] - Remote Port ID number (r_int_num)
            
            r_host = columns[0]
            l_int = columns[1]
            l_int_num = columns[2]
            r_int = columns[6]
            r_int_num = columns[7]
            
            # Формируем ключи и значения в виде кортежей
            local_key = (hostname, f"{l_int}{l_int_num}")
            remote_value = (r_host, f"{r_int}{r_int_num}")
            
            result[local_key] = remote_value
            
    return result
