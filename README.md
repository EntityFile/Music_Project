Призначення та коротка характеристика програми

Програма дозволяє спростити підбір музики. Спрощення здійснюється за допомогою гнучкого чорного списку, який забирає непотрібні користувачеві треки.

Вхідні та вихідні дані програми

Користувач вводить назву треку і/або автора, які його цікавлять. Програма виводить на екран найпопулярніші треки, які пов'язані з введеним рядком. Потім, залежно від операцій, які користувач буде виконувати, його пошук буде змінюватись.

Структура програми з коротким описом модулів, функцій, класів та методів

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

Коротка інструкція по користуванню програмою

На початку потрібно ввести назву треку і/або автора, які вам подобаються. Програма видасть найпопулярніші треки за вашим запитом та запропонує ввести одну з комманд: playlist-переглянути плейлист, blacklist, track № - на місці № потрібно ввести номер треку, який вас зацікавив(програма переведе вас до меню для операцій з треком), search - зробити наступний пошук, find - підбір музики за вашим плейлистом, exit - вихід. У меню плейлиста в можете: clear - очистити його, remove № - видалити певний трек з нього, return - повернути плейлист до його попереднього стану, back - повернутися в головне меню. У blacklist'а меню подібне. У меню треку ви можете: add to playlist - добавити його до плейлиста, add to blacklist, add genre to blacklist, add artist to blacklist, lyrics - згенерувати слова до треку, find by genre - здійснити підбір музики за жанром, find by artist.

Опис тестових прикладів для первірки працездатності програми
