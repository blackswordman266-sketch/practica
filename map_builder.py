# map_builder.py - Скрипт для создания общей карты топологии
from net_parser import extract_cdp_data
from pprint import pprint

def build_full_map(filenames):
    """
    Обрабатывает вывод команды 'show cdp neighbors' из нескольких файлов
    и объединяет его в одну общую топологию.
    """
    network_map = {}
    for filename in filenames:
        with open(filename) as show_command:
            # Используем функцию из вспомогательного модуля
            parsed = extract_cdp_data(show_command.read())
            network_map.update(parsed)
    return network_map

if __name__ == "__main__":
    # Список файлов с выводом show cdp neighbors (примеры)
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]
    
    # Создание общей топологии
    topology = build_full_map(infiles)
    
    # Вывод общей топологии на экран
    print("Общая топология (может содержать дубликаты):")
    pprint(topology)
