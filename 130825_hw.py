# -*- coding: utf-8 -*-
# Модуль 10: Системи контролю версій
#  Тема: Системи контролю версій. Частина 1
#  Завдання 1
#  Встановіть і налаштуйте на своєму локальному комп'ю
# тері Git.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1 (master)
# $ git config user.name
# Volodymyr Potereiko(AIPython52)
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1 (master)
# $ git config user.email
# potereyko@gmail.com
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1 (master)
#  Завдання 2
#  Створіть папку з двома файлами.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1 (master)
# $ cd main_folder_hw
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ touch file1.txt file2.txt
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ ls -l
# total 0
# -rw-r--r-- 1 user 197121 0 Aug 24 21:24 file1.txt
# -rw-r--r-- 1 user 197121 0 Aug 24 21:24 file2.txt
#  Завдання 3
#  Створіть репозиторій у цій папці.
# git init
# Завдання 4
#  Додайте два файли в індекс репозиторія за допомогою
# команди: git add.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   ../130825_hw.py
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         unindexed.txt
#         unindexed2.txt
#
# no changes added to commit (use "git add" and/or "git commit -a")
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git add .
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   unindexed.txt
#         new file:   unindexed2.txt
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   ../130825_hw.py
#  Завдання 5
#  Створіть commit на підставі файлів, доданих в індекс.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git log --oneline --graph --decorate --all
# * 1709295 (HEAD -> master, origin/master) Виконано 4 завдання
# * a6306a5 Виконано 3 завдання
# * 37a31af Виконано 2 завдання
# * e69fe40 Виконано 1 завдання
# * 343c986 Додано у файл помилку
# * bf63c42 Створено підпапку і файл з коментарем без розширення .py
# * 282d46b Git log перед цим комітом
# * ca9f6ab Git start commit
# Використайте команду: git commit.
#  Завдання 6
#  Змініть вміст одного з файлів і створіть commit з
# новими даними.
#  Завдання 7
#  Створіть новий файл, наповніть його даними. Після
# наповнення створіть commit з новим файлом.
#  user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ echo "Новий вміст файлу" > file1.txt
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ echo "Ще один рядок" >> file1.txt
# Завдання 8
#  Внесіть зміни у вміст файлу, збережіть зміни (не ство
# рюйте новий commit). Скасуйте зміни в локальній копії
# файлу за допомогою команди: git checkout.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $  echo "cl" > file.txt
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         file.txt
#
# nothing added to commit but untracked files present (use "git add" to track)
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git checkout -- file.txt
# error: pathspec 'file.txt' did not match any file(s) known to git
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git add file.txt
# warning: in the working copy of 'main_folder_hw/file.txt', LF will be replaced by CRLF the next time Git touches it
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   file.txt
#
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git checkout -- file.txt
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   file.txt
#
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git restore --staged file.txt
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         file.txt
#
# nothing added to commit but untracked files present (use "git add" to track)
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git checkout -- file.txt
# error: pathspec 'file.txt' did not match any file(s) known to git
#  Завдання 9
#  Внесіть зміни у вміст файлу, додайте зміни в індекс
# (не створюйте новий commit). Скасуйте зміни в індексі
# за допомогою команди: git reset.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git add file.txt
# warning: in the working copy of 'main_folder_hw/file.txt', LF will be replaced by CRLF the next time Git touches it
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         modified:   file.txt
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   ../130825_hw.py
#
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git reset HEAD file.txt
# Unstaged changes after reset:
# M       130825_hw.py
# M       main_folder_hw/file.txt
# Виконано 9-10 завдання
# git commit --amend -m "Виконано 9 завдання"
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git log --oneline --graph --decorate --all
# * f6eabab (HEAD -> master) Виконано 9 завдання
# | * 544affe (origin/master) Виконано 9-10 завдання
# |/
# * dcccda8 Виконано 8 завдання
# * 526176c Виконано 6-7 завдання Змінено file1.txt через echo
# * 36eb13f Виконано 5 завдання
# * 1709295 Виконано 4 завдання
# * a6306a5 Виконано 3 завдання
# * 37a31af Виконано 2 завдання
# * e69fe40 Виконано 1 завдання
# * 343c986 Додано у файл помилку
# * bf63c42 Створено підпапку і файл з коментарем без розширення .py
# * 282d46b Git log перед цим комітом
# * ca9f6ab Git start commit
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git push --force-with-lease
# Enumerating objects: 9, done.
# Counting objects: 100% (9/9), done.
# Delta compression using up to 32 threads
# Compressing objects: 100% (5/5), done.
# Writing objects: 100% (5/5), 657 bytes | 164.00 KiB/s, done.
# Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
# To https://github.com/potervi94/git130825_1.git
#  + 544affe...f6eabab master -> master (forced update)
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git log --oneline --graph --decorate --all
# * f6eabab (HEAD -> master, origin/master) Виконано 9 завдання
# * dcccda8 Виконано 8 завдання
# * 526176c Виконано 6-7 завдання Змінено file1.txt через echo
# * 36eb13f Виконано 5 завдання
# * 1709295 Виконано 4 завдання
# * a6306a5 Виконано 3 завдання
# * 37a31af Виконано 2 завдання
# * e69fe40 Виконано 1 завдання
# * 343c986 Додано у файл помилку
# * bf63c42 Створено підпапку і файл з коментарем без розширення .py
# * 282d46b Git log перед цим комітом
# * ca9f6ab Git start commit
#
#  Завдання 10
#  Внесіть зміни у вміст файлу, додайте зміни в індекс,
# створіть новий commit. Скасуйте зміни в останньому
# commit шляхом створення нового commit за допомогою
# команди: git revert.
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ echo "Тестова зміна до завдання 10" >> file.txt
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git add file.txt
# warning: in the working copy of 'main_folder_hw/file.txt', LF will be replaced by CRLF the next time Git touches it
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git commit -m "Зміни у file.txt(Завдання 10)"
# [master b510203] ╨Ч╨╝╤Ц╨╜╨╕ ╤Г file.txt(╨Ч╨░╨▓╨┤╨░╨╜╨╜╤П 10)
#  1 file changed, 2 insertions(+), 1 deletion(-)
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git log --oneline -n 3
# b510203 (HEAD -> master) Зміни у file.txt(Завдання 10)
# f6eabab (origin/master) Виконано 9 завдання
# dcccda8 Виконано 8 завдання
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git revert --no-edit HEAD
# [master 817ed50] Revert "╨Ч╨╝╤Ц╨╜╨╕ ╤Г file.txt(╨Ч╨░╨▓╨┤╨░╨╜╨╜╤П 10)"
#  Date: Sun Aug 24 22:12:24 2025 +0300
#  1 file changed, 1 insertion(+), 2 deletions(-)
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git status
# On branch master
# Your branch is ahead of 'origin/master' by 2 commits.
#   (use "git push" to publish your local commits)
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   ../130825_hw.py
#
# no changes added to commit (use "git add" and/or "git commit -a")
#
# user@CEPBEPOKK MINGW64 ~/OneDrive/__AIPYTHON52/ALL_TASKS/08_2025/130825/git130825_1/main_folder_hw (master)
# $ git log --oneline -n 3
# 817ed50 (HEAD -> master) Revert "Зміни у file.txt(Завдання 10)"
# b510203 Зміни у file.txt(Завдання 10)
# f6eabab (origin/master) Виконано 9 завдання
#  Завдання 11
#  Видаліть кілька останніх commit. Використайте ко
# манду: git reset з опцією --hard.
#  Завдання 12
#  Надішліть наявний репозиторій до сайту GitHub
