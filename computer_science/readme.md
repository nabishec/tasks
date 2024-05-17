В этой папке будут выполняться задания из учебника :

Computer science - Роберт Седжвик, Кевин Уэйн

# 1.Первая глава основы программирования:

## 1.1 Ваша первая программа:
1 [HelloWorld](src/FirstProgram/HelloWorld.java) program

2 [UseArgument](src/FirstProgram/UseArgument.java) program

### Упражнения

#### 1.1.2 Опишите, что произойдет, если пропустить в программе [HelloWorld](src/FirstProgram/HelloWorld.java)

a. public - если убрать перед функцией то выдаст ошибку, что компилятор не нашел 

главного метода класса. А если убрать перед классом то ничего не изменится

b. static - программа не запуститься так как нет статического метода в классе

c. void - выдает ошибку что нет типа метода

d. args - выдает ошибку, что ожидалось закрытие скобки класса

#### 1.1.3 Опишите, что произойдет, если совершить ошибку в след. словах  в программе [HelloWorld](src/FirstProgram/HelloWorld.java)

a. public - синтаксическая ошибка, ожидалось паблик

b. static - также выдает синтиаксическую ошибку

c. void - выдает ошибку что  типа метода с ошибкой

d. args - программа работает корректно

#### 1.1.4 Что произойдет в программе, если в файле [HelloWorld](src/FirstProgram/HelloWorld.java) перенести строку вывода таким обиразом :

>     System.out.println("Hello,
>                        World");

Ответ: выведет ошибку, что строковый литерал не закрыт

#### Опишите, что произойдет при попытке выполнить программу UseArgument каждой из следующих командных строк:

a. java UseArgument java - HI, java. How are you?

b. java UseArgument  @!&^% - HI, @!&^%. How are you?

c. java UseArgument  1234 - HI, 1234 How are you?

d. java UseArgument.java Bob - не найден или не загружен класс UseArgument.java

e. java UseArgument  Alice Bob - HI, Alice. How are you?

#### 1.1.6 Модифицируйте программу [UseArgument.java](src/FirstProgram/UseArgument.java) — создайте на ее основе про грамму UseThree.java. Новая программа должна получать три имени в аргументах командной строки и выводить предложение, в котором эти имена перечисляются в обратном порядке, —например, для команды javaUseThree Alice Bob Carol долж но выводиться сообщение Hi Carol, Bob, and Alice.

Ответ: [UseThree](src/FirstProgram//UseThree.java)

## Встроенные типы данных
