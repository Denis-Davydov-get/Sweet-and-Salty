# **`Проект “Сайт рецептов” на Django`**


Используя фреймворк Django создан сайт https://Sweet-and-Salty.pythonanywhere.com/, на котором пользователи смогут добавлять свои рецепты блюд и просматривать рецепты других пользователей.

В рамках реализации проекта сделаны следующие шаги:
1. Создано приложение recipeapp, отвечающее за создание, редактирование и хранение рецептов. В рамках приложения созданы:
   - модели Recipe, Ingredient, Category. Между моделями реализованы связи многие ко многим: то есть в одном рецепте может быть много ингредиентов и категорий. И один и то же ингредиент и категории могут быть у других рецептов;
   - также модель Recipe свазана через связь один ко многим со встроенным классом User;
   - на основе моделей построены формы для создания и отображения объектов;
   - через представления и пути организована обработка советующих запросов и взаимодействие с базой данных;
   - через шаблоны организован соответствующий вывод информации из базы данных пользователю.
2. Создано приложение userapp, отвечающее за аутентификацию и регистрацию пользователей:
   - используется встроенная модель User для авторизации и регистрации пользователя;
   - так же настроен профиль пользователя для смены пароля и запрос на восстановление пароль (правда без почтового сервера, с выводом в консоль).
3. Функционал сайта включает в себя:
   - главную страницу: выводит пять наиболее просматриваемых рецептов;
   - страницу рецепты: отражены все занесенный рецепты расположенные по количеству просмотров (поле в модели view), настроено постраничное отображение рецептов;
   - при нажатии на рецепт, для авторизованных пользователей открывается страница с полным описание рецепта и возможностью редактирования ее автором данного рецепта;
   - страница добавить рецепт доступна также для авторизованных пользователей, для остальных перекинет на страницу авторизации;
   - на страница Категории рецептов и Ингредиенты отображаются все существующие категории и ингредиенты в алфавитном порядке с постраничным отображением;
   - при выборе категории или ингредиента для авторизованных пользователей отразятся рецепты, отобранные по соответствующему признаку;
   - при необходимости можно добавить категорию или ингредиент для этого на странице добавить рецепт есть соответствующие кнопки;
   - страницы Войти/Профиль и Зарегистрироваться / Выйти осуществляют взаимодействие с пользователем
  4. Для развертывания проекта необходимо установить в виртуальное окружение пакеты из файла requirements.txt:
     - asgiref==3.8.1
     - Django==5.0.6
     - pillow==10.3.0
     - sqlparse==0.5.0
     - tzdata==2024.1
     - mysqlclient
     - python-dotenv       
   5. Далее связать приложение с БД, осуществить миграции и запустить на сервере.
     
   

