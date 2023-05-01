import psutil
import time

# Установите здесь минимальный процент свободной памяти, который вы хотите поддерживать
MIN_FREE_PERCENT = 5

# Установите здесь путь для файла лога
LOG_FILE = "memory_monitor_log.txt"

# Инициализируем лог-файл
with open(LOG_FILE, "w") as f:
    f.write("Memory Monitor Log\n\n")

while True:
    # Получаем информацию о памяти
    mem = psutil.virtual_memory()
    free_percent = 100 * mem.available / mem.total

    # Проверяем, достигло ли использование памяти порогового значения
    if free_percent < MIN_FREE_PERCENT:
        # Получаем список процессов, сортируем его по использованию памяти
        processes = [(p.pid, p.info['name'], p.info['memory_info'].rss)
                     for p in psutil.process_iter(['pid', 'name', 'memory_info'])]
        sorted_processes = sorted(processes, key=lambda p: p[2], reverse=True)

        # Выбираем процесс, который занимает больше всего памяти и остановим его
        pid, name, memory_usage = sorted_processes[0]
        process = psutil.Process(pid)
        process.terminate()

        # Записываем информацию о процессе в лог-файл
        with open(LOG_FILE, "a") as f:
            f.write(f"Process {name} (PID {pid}) was terminated. Memory usage: {memory_usage / 1024 / 1024:.2f} MB\n")

    # Ждем 5 секунд перед следующей проверкой
    time.sleep(5)

