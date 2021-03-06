# Задания

## Вывод файла

Считать из первого файла `file_name.txt` содержимое (первую строку), оно является названием второг файла. Считать содержимое второго файла и вывести его в консоль.

Например, если в файле `file_name.txt` находится строка `readme.md`, то надо открыть файл `readme.txt` и вывести его содержимое

[Файл для решения](task1.py)

Для проверки запустить из этой же папки (`advanced_basics/files`) скрипт `check_task1.py`

## Файловый кеш

Считать файл `big_file.data` в байтовом режиме и разбить его на сегменты по 256 байт. Если в сегменте меньше 256 байт, то дополнить его нулями до 256. Каждый сегмент сохранить в файл `segment_{i}.cache`, где `{i}` -- номер сегмента начиная с 1

Например, если в файле `big_file.data` 1025 байтов, то на выходе получится 5 файлов: `segment_1.cache`, `segment_2.cache`, ..., `segment_5.cache` (в последнем файле значащим будет только первый байт, остальные -- нули).

Примечание: сегменты нужно дополнять символом `b"\x00"`

[Файл для решения](task2.py)

Для проверки запустить из этой же папки (`advanced_basics/files`) скрипт `check_task2.py`

## ПО ~~иностранного агента~~

Программа читает данные из консоли. В первой строке содержится число `n` -- количество обращений к программе. В следующих `n` строках идут команды вида `{action} {filename}`, где `{action}` -- имя операции (`hide` или `restore`), `{filename}` -- имя файла, с которым производится операция.

Если подана команда `hide`, то программа должна запомнить содержимое файла и в этот же файл записать пустую строку; если же команда `restore`, то восстановить содержимое файла. Гарантируется, что до любой команды `restore` идет команда `hide`

Например, программа получит следующий вход:

```
4
hide secret_data.txt
hide rocket_codes.list
restore secret_data.txt
restore rocket_codes.list
```

В результате выполнения программа сначала удалит содержимое файлов `secret_data.txt` и `rocked_codes.list`, а потом восстановит его.

[Файл для решения](task3.py)

Для проверки запустить из этой же папки (`advanced_basics/files`) скрипт `check_task3.py`
