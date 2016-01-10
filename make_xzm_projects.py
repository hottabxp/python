import os


def make_projects(name, path, icon, cat):
    os.makedirs(name + '/usr/bin')
    os.makedirs(name + '/opt')
    os.makedirs(name + '/usr/share/applications')

    file = open(name+'/usr/share/applications/' + name + '.desktop', 'w')
    file.writelines('[Desktop Entry]\n'
                    'Encoding=UTF-8\n'
                    'Type=Application\n'
                    'Exec=' + path + '\n'
                    'Icon=' + icon + '\n'
                    'Terminal=false\n'
                    'Name=' + name + '\n'
                    'Categories='+ cat)


# make_projects(param)

name = input("Введите имя программы:\n")
path = input("Введите путь к исполняемому файлу:\n")
icon = input("Введить путь к иконке:\n")
сategories = input("Выберете категорию\n"
                   "     1)Аудио\n"
                   "     2)Видео\n"
                   "     3)Разработка\n"
                   "     4)Учеба\n"
                   "     5)Игры\n"
                   "     6)Графика\n"
                   "     7)Итернет\n"
                   "     8)Офис\n"
                   "     9)Наука\n"
                   "     10)Настройки\n"
                   "     11)Система\n"
                   "     12)Инструменты\n")

print('cat = '+сategories)

if сategories == 'a':
    cat = 'Audio'
elif сategories == '2':
    cat = 'Video'
elif сategories == '3':
    cat = 'Development'
elif сategories == '4':
    cat = 'Education'
elif сategories == '5':
    cat = 'Game'
elif сategories == '6':
    cat = 'Graphics'
elif сategories == '7':
    cat = 'Network'
elif сategories == '8':
    cat = 'Office'
elif сategories == '9':
    cat = 'Science'
elif сategories == '10':
    cat = 'Settings'
elif сategories == '11':
    cat = 'System'
elif сategories == '12':
    cat = 'Utility'
else:
    cat = 'error'

make_projects(name, path, icon, cat)
print("Имя=", name, '\n',
      "Путь=", path, '\n',
      "Иконка=", icon, '\n',
      "Категория=", cat)
