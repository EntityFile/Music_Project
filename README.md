# Призначення та коротка характеристика програми

Програма дозволяє спростити підбір музики. Спрощення здійснюється за допомогою гнучкого чорного списку, який забирає непотрібні користувачеві треки.

# Вхідні та вихідні дані програми

Користувач вводить назву треку і/або автора, які його цікавлять. Програма виводить на екран найпопулярніші треки, які пов'язані з введеним рядком. Потім, залежно від операцій, які користувач буде виконувати, його пошук буде змінюватись.

# Структура програми з коротким описом модулів, функцій, класів та методів

Модулі:
* data_module - Модуль, який містить клас Song та класи YouTube та Itunes, які потрібні для завантаження даних з інтернету
* adt_blacklist - Модуль з BlackList ADT
* adt_playlist - Модуль з PlayList ADT
* test_module - Модуль для запуску програми
  Його функції:
  * input_track_name - Функція для введеня інформації
  * iri_converter - Функція для конвертації звичайних рядків до рядків для використання у веб-посиланнях
  * create_search_list - Функція, яка створює список треків з введеного рядка
  * track_information - Функція, яка відображає інформацію про трек
  * show_search_results - Робить запит на введеня інформації та виводить на екран сформований список треків з отриманої інформації
  * find_by_playlist - Робить підбір музики на основі треків, які є в спуску улюблених треків
  * maiin - main функція

# Коротка інструкція по користуванню програмою

На початку потрібно ввести назву треку і/або автора, які вам подобаються. Програма видасть найпопулярніші треки за вашим запитом та запропонує ввести одну з комманд: playlist-переглянути плейлист, blacklist, track № - на місці № потрібно ввести номер треку, який вас зацікавив(програма переведе вас до меню для операцій з треком), search - зробити наступний пошук, find - підбір музики за вашим плейлистом, exit - вихід. У меню плейлиста в можете: clear - очистити його, remove № - видалити певний трек з нього, return - повернути плейлист до його попереднього стану, back - повернутися в головне меню. У blacklist'а меню подібне. У меню треку ви можете: add to playlist - добавити його до плейлиста, add to blacklist, add genre to blacklist, add artist to blacklist, lyrics - згенерувати слова до треку, find by genre - здійснити підбір музики за жанром, find by artist.

# Опис тестових прикладів для первірки працездатності програми

1) Якщо ввести 'hello', то програма виведе на екран наступний список треків:

1 Adele : Hello

2 Lionel Richie : Hello

3 HELLO : New York Groove

4 Martin Solveig & Dragonette : Hello

5 HELLO : Tell Him

6 Karmin : Brokenhearted

7 J. Cole : Hello

8 HELLO : Teenage Revolution

9 HELLO : Keep Us Off the Streets

10 HELLO : Another School Day

11 OMfG : Hello

12 HELLO : Star Studded Sham

13 HELLO : Little Miss Mystery

14 HELLO : Out of Our Heads

15 HELLO : Ask Your Mama

16 HELLO : C'mon

17 HELLO : Games Up

18 HELLO : Heart Get Ready for Love

19 HELLO : Love Stealer

20 Karmin : Hello

21 HELLO : You Move Me

22 HELLO : C'mon Get Together

23 HELLO : Voodoo Eyes

24 HELLO : Lightning

25 HELLO : Bend Me Shape Me

26 HELLO : Do It All Night

27 HELLO : Gotta Lotta Soul

28 HELLO : Shine On Silver Light

29 HELLO : Jenny Dream

30 HELLO : We Gotta Go

31 Zooey Deschanel : Hello

32 HELLO : The Wench

33 Lil Wayne : Hello (feat. Shane Heyl)

34 Kelly Clarkson : Hello

35 Eminem : Hello

36 Lionel Richie : Hello (feat. Jennifer Nettles)

37 Glee Cast : Hello (Glee Cast Version) [feat. Jonathan Groff]

38 T.I. : Hello (feat. CeeLo Green)

39 Glee : Hell-O

40 Prince : Hello

41 Evanescence : Hello

42 T.I. : Hello (feat. Governor)

43 Disturbed : The Sound of Silence

44 The Game : Hello (feat. Lloyd)


2) Тоді можемо додати певного автора до чорного списк, щоб оптимізувати пошук. Наприклад введемо track 3. Тоді ми отримаємо наступне поле:


Artist: HELLO

Track name: New York Groove

Genre: Rock

YouTube video title: New York Groove - Hello

YouTube video URL: https://www.youtube.com/watch?v=Zox2qo-wzb0





back - Back to the main menu

add to playlist - Add this song to the playlist

add to blacklist - Add this song to the blacklist

add genre to blacklist - Add the genre of this song to the blacklist

add artist to blacklist - Add the artist to the blacklist

lyrics - Get the lyrics

find by genre - Shows potentially interesting songs by genre

find by artist - Shows potentially interesting songs by artist



3) Додамо автора до чорного списку. Вводимо add artist to blacklist.

4) Тепер спробуємо знову зробити запит на пошук. Вводимо back, потім search і знову 'hello'. Отримуємо наступний список треків( вже без 
групи HELLO):



1 Adele : Hello

2 Lionel Richie : Hello

3 Martin Solveig & Dragonette : Hello

4 Karmin : Brokenhearted

5 J. Cole : Hello

6 OMfG : Hello

7 Karmin : Hello

8 Zooey Deschanel : Hello

9 Lil Wayne : Hello (feat. Shane Heyl)

10 Kelly Clarkson : Hello

11 Eminem : Hello

12 Lionel Richie : Hello (feat. Jennifer Nettles)

13 Glee Cast : Hello (Glee Cast Version) [feat. Jonathan Groff]

14 T.I. : Hello (feat. CeeLo Green)

15 Glee : Hell-O

16 Prince : Hello

17 Evanescence : Hello

18 T.I. : Hello (feat. Governor)

19 Disturbed : The Sound of Silence

20 The Game : Hello (feat. Lloyd)


