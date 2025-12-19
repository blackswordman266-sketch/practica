# pop1.py - Основной скрипт для создания общей карты топологии
from parse_cdp_neighbors import parse_cdp_neighbors
from pprint import pprint

def create_network_map(filenames):
    """
    Обрабатывает вывод команды 'show cdp neighbors' из нескольких файлов
    и объединяет его в одну общую топологию.
    """
    network_map = {}
    for filename in filenames:
        with open(filename) as show_command:
            # Используем функцию из вспомогательного модуля
            parsed = parse_cdp_neighbors(show_command.read())
            network_map.update(parsed)
    return network_map

if __name__ == "__main__":
    # Список файлов с выводом show cdp neighbors (примеры)
    # Для запуска этого скрипта вам потребуются файлы sh_cdp_n_sw1.txt, sh_cdp_n_r1.txt и т.д.
    # Я не могу создать эти файлы, но предоставляю логику.
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]
    
    # Создание общей топологии
    topology = create_network_map(infiles)
    
    # Вывод общей топологии на экран
    print("Общая топология (может содержать дубликаты):")
    pprint(topology)
