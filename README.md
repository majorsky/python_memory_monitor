📋 Memory Monitor Script Description

This Python script is a memory usage monitor that automatically terminates a process exceeding a specified threshold. It utilizes the psutil library to gather memory and process information.

🔒 Settings

MIN_FREE_PERCENT: Set this variable to the minimum percentage of free memory you want to maintain on your system. If the free memory falls below this value, the script will take action.
LOG_FILE: Set the path to the log file where events and process information will be recorded.
📝 Logging

The script initializes the log file specified in the LOG_FILE variable and records information about processes that were terminated due to low memory.

⚙️ Main Loop

The main loop of the script operates as follows:

Retrieve memory information using the psutil library.
Calculate the percentage of free memory relative to the total memory.
Check if the memory usage has reached the threshold (MIN_FREE_PERCENT).
If the free memory percentage is below the threshold, the script takes action.
Retrieve a list of processes and sort them by memory usage.
Terminate the process with the highest memory usage.
Write information about the process to the log file, including the process name, process ID (PID), and memory usage.
Sleep for 5 seconds before the next check.
🔍 Monitor Memory Usage

With this script, you can effectively monitor and prevent exceeding the specified memory threshold on your system. The log file will contain valuable information about the terminated processes, enabling you to analyze and optimize memory usage.

⚠️ Important

Make sure to properly configure the MIN_FREE_PERCENT and LOG_FILE variables according to your requirements before running the script. Additionally, note that terminating a process may impact your system's operation, so exercise caution when selecting the free memory threshold and analyze the logs to make informed decisions.

📋 Описание скрипта Memory Monitor

Этот Python скрипт представляет собой мониторинг использования памяти на вашей системе и автоматически останавливает процесс, который превышает заданный пороговый уровень. Он использует библиотеку psutil для получения информации о памяти и процессах.

🔒 Настройки

MIN_FREE_PERCENT: Установите эту переменную на минимальный процент свободной памяти, который вы хотите поддерживать на вашей системе. Если свободный процент памяти падает ниже этого значения, скрипт будет принимать меры.
LOG_FILE: Установите путь к файлу лога, в котором будут записываться события и информация о процессах.
📝 Логирование

Скрипт инициализирует лог-файл, указанный в переменной LOG_FILE, и будет записывать в него информацию о процессах, которые были остановлены из-за недостатка свободной памяти.

⚙️ Основной цикл

В основном цикле скрипта происходит следующее:

Получение информации о памяти с использованием библиотеки psutil.
Вычисление процента свободной памяти относительно общего объема.
Проверка, достигло ли использование памяти порогового значения (MIN_FREE_PERCENT).
Если свободный процент памяти ниже порогового значения, скрипт приступает к действиям.
Получение списка процессов и сортировка его по использованию памяти.
Остановка процесса, который занимает больше всего памяти.
Запись информации о процессе в лог-файл, включая имя процесса, его идентификатор (PID) и использование памяти.
Ожидание 5 секунд перед следующей проверкой.
🔍 Следите за использованием памяти

С помощью этого скрипта вы можете эффективно контролировать использование памяти на вашей системе и предотвращать превышение заданного порога. Лог-файл будет содержать полезную информацию о процессах, которые были остановлены, что поможет вам анализировать и оптимизировать использование памяти.

⚠️ Важно

Убедитесь, что вы правильно настроили переменные MIN_FREE_PERCENT и LOG_FILE в соответствии с вашими потребностями перед запуском скрипта. Также обратите внимание, что остановка процесса может повлиять на работу вашей системы, поэтому будьте внимательны при выборе порогового значения свободной памяти и анализируйте логи для принятия информированных решений.
