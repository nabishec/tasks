# Ask_ans
## Как добавить подсказки при вводе в юпипке? - Добавить nbextentions, если не получается классически то использовать:
1) Откройте prompt Anaconda.
2) Введите -
```conda install -c conda-forge jupyter_contrib_nbextensions```
 Введите 'y' для установки.
 Bведите ```jupyter contrib nbextension install --sys-prefix```
3) Выйдите из запроса Anacodna
4) Перезапустите Jupyter notebook. (Теперь вы увидите вкладку nbextensions)

## Как скачать рэйлиб на убунту,используя vscode

Пошаговая инструкция:

Шаг 1: Установите raylib и необходимые зависимости

Откройте терминал и выполните следующие команды:

```sudo apt-get update```

```sudo apt-get install build-essential git libasound2-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev```

Затем склонируйте репозиторий raylib и перейдите в его каталог:

```git clone https://github.com/raysan5/raylib.git```

```cd raylib/src```

Соберите и установите библиотеку:

```make PLATFORM=PLATFORM_DESKTOP```

```sudo make install```

Шаг 2: Скачайте "tasks.json" добавьте его в папку с будущим проектом, где исполняемый файл будет называться main (или измените "tasks.json", изменив название исполняемого файла)

Шаг 3: Соберите проект

Нажмите Ctrl + Shift + B (или выберите Build Task в меню Terminal), чтобы запустить задачу построения. Это создаст исполняемый файл main в каталоге вашего проекта.

Шаг 4: Запустите проект

Откройте терминал и перейдите в каталог вашего проекта. Затем запустите исполняемый файл:

```./main```

Это все! Теперь вы можете создавать свои собственные игры и приложения с помощью raylib в VSCode на Ubuntu.
