# CharStat


Программа со стандартного входного потока (с консоли) считывает текст
и подсчитывает символы a, b, c - латинские, в нижнем регистре. Через каждые
прочитанные 1000 символов, выводит статистику по количеству встретившихся в
тексте символов a, b, c.


##### Пример:
```
name@machine:~$ python counter.py
Enter text: aaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccddddddddddddddddddddddddd
a:21, b:0, c:21
```
Имеется возможность указать произвольное ограничение для вывода промежуточной 
статистики с помощью аргумента `--limit`.

##### Пример:

```
name@machine:~$ python counter.py --limit 10
Enter text: kjahjhgshgvhgcdagfscdgfacgsdghcahgdschagcdhghacshdgcajghcdjgacsdjac
a:1, b:0, c:0

a:2, b:0, c:1

a:3, b:0, c:3

a:4, b:0, c:5

a:6, b:0, c:7

a:7, b:0, c:9

a:9, b:0, c:11
