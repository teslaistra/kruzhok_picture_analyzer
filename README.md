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
Для выполнения поставленной задачи нами была выбрана open-source библиотека OpenCV, которая позволила бы нам реализовать различные методы поиска логотипа Кружкового Движения на изображении. Так например первоначально нами были протестированы три метода(BRISK, AZAKE, OBR) для поиска "фич" на изображениях и их дальнейшего сопоставления. Недостатком подхода “поиск фич” оказалась то, что логотип КД геометрически правильный и во многом состоит из прямых линий. Это приводило к множеству ложных срабатываний, например при сопоставлении логотипа и, например, фотографии где люди находятся на фоне прямых геометрических объектов, так как никакой алгоритм не в состоянии четко отличить уникальность небольшого участка прямой линии. 
Далее мы воспользовались методом template_matching, который в свою очередь смог демонстрировать определенные результаты. Основная сложность этого метода в корректной предобработке изображения для проведения сравнения шаблона(логотипа) и самой фотографии. После экспериментов с различными типами масок и их параметрами нами был подобран набор, позволяющий добиться максимальных результатов, из полученных нами. 


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

## Перспективы
В будущем возможно реализовать более сложные процессы предобработки изображения для снижения количества ложных срабатываний. Также мы выдвигаем гипотезу, что другие параметры предобработки изображения могут отфильтровать лишние геометрические объекты, что позволит вновь вернутся к тестам алгоритмов поиска “фич”.

## Авторы
- [teslaistra](https://github.com/teslaistra)
- [sostema](https://github.com/sostema)
- [sofary](https://github.com/sofary)
  
## Ссылки
  - [OpenCV](https://opencv.org)
  - [ORB: an efficient alternative to SIFT or SURF](http://www.willowgarage.com/sites/default/files/orb_final.pdf)
  

## Лицензия
[GPL-3.0 License](LICENSE)
