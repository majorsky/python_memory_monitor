# python_memory_monitor
Скрипт на Python, будет полезен тем, кто использует LiveCD, SDCard прочие носители с разными диструбутивами Debian.

Этот скрипт предназначен для мониторинга использования оперативной памяти и автоматического завершения процесса, который занимает больше всего памяти, если использование памяти превышает установленный порог.

Для мониторинга используется библиотека psutil, которая позволяет получить информацию о системе, включая использование памяти процессами.

Параметры, которые можно настроить:

MIN_FREE_PERCENT - минимальный процент свободной памяти, который необходимо поддерживать;
LOG_FILE - путь к файлу лога.
При запуске скрипта лог-файл будет инициализирован.

В цикле скрипта получается информация о памяти и рассчитывается процент свободной памяти. Если свободная память падает ниже установленного порога, происходит выборка процессов, сортировка их по использованию памяти и завершение процесса, занимающего больше всего памяти. Информация о завершенном процессе записывается в лог-файл.

Между проверками скрипт ждет 5 секунд.