# Picture Analyzer 
Тестовое задание команды **Moscow Dynamics** от лаборатории [KRUZHOK.PRO](https://KRUZHOK.PRO) по треку **Проверка согласий**

Последний коммит перед дедлайном: 
[7445472](https://github.com/teslaistra/kruzhok_picture_analyzer/commit/7445472b9432539768f1b1a8b9afea92014af272)

## Содержание
* [Описание](#описание)
* [Установка](#установка)
* [Использование](#использование)
* [Тестирование](#тестирование)
* [TODO](#todo)
* [Авторы](#авторы)
* [Ссылки](#ссылки)
* [Лицензия](#лицензия)

## Описание

## Установка
Скачайте репозиторий с помощью `git clone` в удобное место

Для использования программы, необходимо иметь интерпретатор 
[Python](https://www.python.org) **не ниже версии 3.8**.

Зависимости можно установить как глобально
```console
user@kruzhok:~$ pip3 install --upgrade pip
user@kruzhok:~$ pip3 install -r requirements.txt
```

Так и воспользоваться [virutalenv](https://virtualenv.pypa.io/en/latest/)
```console
user@kruzhok:~$ python3 -m pip install --upgrade pip
user@kruzhok:~$ python3 -m pip install virtualenv
user@kruzhok:~$ python3 -m venv venv
user@kruzhok:~$ source venv/bin/activate
(venv) user@kruzhok:~$ python3 -m pip install -r requirements.txt
```

## Использование
Базовый пример использования скрипта [checker.py](checker.py)
```console
user@kruzhok:~$ python3 checker.py image --template logo.jpg
```
Для полного описания возможностей используйте `python3 checker.py --help`

## Тестирование
Для запуска тестирования всех возможных методов, используйте [test.sh](test.sh)
```console
user@kruzhok:~$ bash test.sh
```

## TODO
- [x] ORB
- [x] AKAZE
- [ ] BRISK
- [x] Template Matching
- [ ] Haar Cascades
- [ ] CNN

## Авторы
- [teslaistra](https://github.com/teslaistra)
- [sostema](https://github.com/sostema)
- [sofary](https://github.com/sofary)
  
## Ссылки
  - [OpenCV](https://opencv.org)
  - [ORB: an efficient alternative to SIFT or SURF](http://www.willowgarage.com/sites/default/files/orb_final.pdf)
  

## Лицензия
[GPL-3.0 License](LICENSE)
