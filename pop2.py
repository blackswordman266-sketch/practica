# pop2.py - Скрипт для создания уникальной топологии и визуализации
from pop1 import create_network_map
# from draw_network_graph import draw_topology # Предполагается, что этот модуль существует

def unique_network_map(topology_dict):
    """
    Удаляет дубликаты из общей топологии.
    
    Дубликаты возникают, когда связь A-B и B-A присутствует в словаре.
    Для устранения дубликатов, кортеж-ключ и кортеж-значение
    сортируются, и только один вариант (например, с меньшим первым элементом)
    добавляется в новый словарь.
    """
    network_map = {}
    for key, value in topology_dict.items():
        # Сортируем кортежи, чтобы получить уникальный ключ для каждой пары
        sorted_key = tuple(sorted((key, value)))
        
        # Добавляем в словарь только если такой пары еще нет
        if sorted_key not in network_map:
            network_map[sorted_key] = None # Значение не важно, важен ключ
            
    # Преобразуем ключи обратно в формат {key: value} для удобства
    final_map = {}
    for key in network_map:
        # key - это кортеж из двух кортежей: ((dev1, int1), (dev2, int2))
        final_map[key[0]] = key[1]
        
    return final_map

if __name__ == "__main__":
    # Список файлов с выводом show cdp neighbors (примеры)
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]
    
    # 1. Создание общей топологии
    topology = create_network_map(infiles)
    
    # 2. Удаление дубликатов
    unique_topology = unique_network_map(topology)
    
    # 3. Визуализация (закомментировано, так как нет модуля draw_network_graph)
    # draw_topology(unique_topology, output_filename="topology.svg")
    
    print("Уникальная топология (без дубликатов):")
    pprint(unique_topology)
