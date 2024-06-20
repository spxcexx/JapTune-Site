# Продаж японських машин з тюнінгом та без

Цей проєкт спрямований на продаж японських автомобілів, як з тюнингом, так і без нього. Ми пропонуємо широкий асортимент машин для всіх любителів японських авто, від класичних моделей до сучасних спортивних автомобілів з професійним тюнингом.

# Швидка карта по файлу README.md
- [Учасники проєкту](#учасники-проєкту)
- [Figma проєкт](#figma-проєкт)
- [Сторінки](#сторінки)
- [Технології](#технології)
- [Моделі](#моделі)
  - [Brand](#brand)
  - [CarModel](#carmodel)
  - [CarVariant](#carvariant)
- [Функції відображення](#функції-відображення)
  - [main](#main)
  - [registration](#registration)
  - [login_user](#login_user)
  - [show_successfull_login](#show_successful_login)
  - [logout_user](#logout_user)

## Учасники проєкту

1. **Данило Колосов / Danylo Kolosov** (Team Lead)
   - GitHub профіль: https://github.com/spxcexx

2. **Богдан Рубанов / Bohdan Rubanov** (Full Stack Developer)
   - GitHub профіль: https://github.com/BohdanRubanov

3. **Рінат Ткаченко / Rinat Tkachenko** (Full Stack Developer)
   - GitHub профіль: https://github.com/RinatUA

4. **Ярослав Єрмаков / Yaroslav Ermakov** (Full Stack Developer)
   - GitHub профіль: https://github.com/ZenPickk

## Figma проєкт
   - https://www.figma.com/design/Vi09s9VDNOCxzVR8TT3KbQ/Untitled?node-id=0-1&t=ROwet0lwuOx6WUSf-1

## Сторінки

- **Головна**: Основна сторінка з інформацією про нашу корпорвцію та пропозиції.
- **Про нас**: Сторінка з описом наших послуг та можливостей.
- **Наша адреса**: Сторінка з картою та адресою нашого магазину.
- **Шукаємо спеціалістів**: Інформація про відкриті вакансії та вимоги до кандидатів.
- **Екскурсії**: Організація та запис на екскурсії по нашій майстерні.
- **Наші роботи**: Галерея тюнінгованих автомобілів.
- **Сторінка для зв'язку**: Контактна форма для зв'язку з нами.
- **Сторінки з марками**: Окрема сторінка для 5 марок автомобілів, які ми продаємо.
- **Сторінки докладніше**: Детальні сторінки для кожної машини (5 сторінок для кожної марки).
- **Сторінка з партнерами**: Сторінка, де показані бренди наших партнерів з котрими у нас є контракт.

## Технології

- HTML (HyperText Markup Language)
  - HTML використовується для створення структури і вмісту веб-сторінок. Він визначає елементи, такі як заголовки, абзаци, зображення і посилання.
- CSS (Cascading Style Sheets)
  - CSS використовується для стилізації і зовнішнього оформлення веб-сторінок. Він визначає зовнішній вигляд елементів, включаючи кольори, шрифти, відступи і розташування.
- JavaScript
  - JavaScript є мовою програмування, яка додає інтерактивність на веб-сторінки. Він використовується для створення динамічних елементів, анімацій, обробки подій і взаємодії з користувачем.
- Python
  - Python — це універсальна мова програмування, яка використовується для веб-розробки, наукових обчислень, автоматизації завдань та багатьох інших цілей.
- Django
  - Django — це фреймворк на Python для швидкої розробки веб-додатків. Він надає готові інструменти і шаблони для роботи з базами даних, обробки форм, аутентифікації та іншого
- MySQL
  - MySQL — це реляційна база даних, яка використовується для зберігання даних у веб-додатках. Вона забезпечує ефективне управління та доступ до даних.
- Bootstrap
  - Bootstrap — це фреймворк CSS і JavaScript, який спрощує створення адаптивних і стильних інтерфейсів користувача. Він включає готові компоненти, сітки, типографіку та багато іншого.
- jQuery
  - jQuery — це бібліотека JavaScript, яка спрощує маніпулювання DOM, обробку подій, анімацію і взаємодію з сервером. Вона допомагає писати менш об'ємний і більш зрозумілий код.
- AJAX (Asynchronous JavaScript and XML)
  - це технологія, що дозволяє взаємодіяти з сервером без перезавантаження сторінки. Вона використовується для асинхронної передачі даних між веб-браузером і сервером.

## <a name="section5"></a>Моделі

### Brand

Модель для назв брендів машин, які ми пропонуємо.

```python
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
```
- **name:** Назва бренду машини.
- **max_length**: максимальна кількість символів для назви бренду.
- **unique=True**: дає цьому рядку унікальність. Це означає, що створити два записи з однаковим значенням поля **name** - неможливо.

###

### CarModel

Модель для назв моделей машин, які ми пропонуємо.

```python 
from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, related_name='models', on_delete=models.CASCADE)
```

- **name:** Назва моделі машини.
- **max_length:** Максимальна кількість символів для назви моделі.
- **brand:** Зовнішній ключ, що посилається на модель Brand.
- **related_name='models':** Дозволяє доступ до всіх моделей, що належать до конкретного бренду через атрибут models у моделі Brand.
- **on_delete=models.CASCADE:** Визначає, що станеться з моделями машин при видаленні відповідного бренду. У даному випадку, всі моделі машин будуть видалені разом з брендом.

###

### CarVariant

Модель для різних варіантів (версій) машин.

```python
from django.db import models

class CarVariant(models.Model):
    model = models.ForeignKey(CarModel, related_name='variants', on_delete=models.CASCADE)
    year = models.IntegerField()
    generation = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
```

- **model:** Зовнішній ключ, що посилається на модель CarModel.
- **related_name='variants':** Дозволяє доступ до всіх варіантів, що належать до конкретної моделі через атрибут variants у моделі CarModel.
- **on_delete=models.CASCADE:** Визначає, що станеться з варіантами машин при видаленні відповідної моделі. У даному випадку, всі варіанти машин будуть видалені разом з моделлю.
- **year:** Рік випуску варіанту машини.
- **generation:** Покоління варіанту машини.
- **max_length:** Максимальна кількість символів для назви покоління.
- **image:** Поле для завантаження зображення варіанту машини.
- **null=True:** Дозволяє зберігати порожні значення у базі даних.
- **blank=True:** Дозволяє форму залишати це поле порожнім.

(Поле **image** було створено після проведення міграцій, тому має атрибути **null=True** та **blank=True**)

## Функції відображення

### main

Функція відображення головної сторінки

```python

def main(request):
    return render(request, 'japtuneapp/index.html')

```
- Оператор def у мові програмування Python - виконує створення функції, куди ми повинні передати назву функції та її аргументи, у нашому випадку аргумент **request** - це запит на веб-сторінку на яку хоче потрапити користувач, і якщо запит без помилок - виконується код внутри функції, де **return** - повертає користувачу сторінку в HTML вигляді, за відображення сторінки відповідає рядок **render(request, 'japtune/index.html')** де **request** - це і є запит користувача який він надсилав, а **'japtune/index.html'** - це шлях до файлу, який буде повернутий користувачу.

### registration

Функція для реєстрації нового користувача

```python
def registration(request):
    if request.method == "POST":
        first_name = request.POST.get("name")
        last_name = request.POST.get("surname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        text_error = None
        print(f"Ім'я: {first_name}; Фамілія {last_name}; Email: {email}; Юзернейм: {username}; Пароль: {password}; Підтв. пароля:{password_confirm}")
        if password == password_confirm:
            try:
                print("Спроба створити юзера")
                User.objects.create_user(first_name=first_name, last_name=last_name ,email=email, username=username, password=password)
                print("Користувача створено")
                return redirect('login_user')
            except IntegrityError:
                print("Користувач існує")
                text_error = "Такий користувач вже існує"
                return render(request, "registrationapp/registration.html", context={"text_error" : text_error})
        elif password != password_confirm:
            text_error = "Паролі не збігаються"
            return render(request, "registrationapp/registration.html", context={"text_error" : text_error})

        else:
            text_error = "Помилка"
            return render(request, "registrationapp/registration.html", context={"text_error" : text_error})

    return render(request, 'registrationapp/registration.html')
```

- Функція приймає запит користувача як аргумент (request).
- Якщо метод запиту `POST`, функція витягує дані з форми (ім'я, прізвище, електронну пошту, ім'я користувача, пароль, підтвердження пароля).
- Перевіряється, чи збігаються паролі. Якщо так, функція намагається створити нового користувача.
- Якщо користувача успішно створено, виконується перенаправлення на сторінку входу. У разі помилки (наприклад, якщо користувач вже існує), повертається сторінка реєстрації з повідомленням про помилку.
- Якщо метод запиту не `POST`, повертається сторінка реєстрації.

### login_user

Функція для входу користувача

```python
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        text_error = None
        print(f"Аунтифікація користувача. Юзернейм: {username}; Пароль: {password}")
        user = authenticate(request, username=username, password=password)
        print("Користувач аунтифікувався. Перевірка у базі данних")
        if user is not None:
            print("Користувача знайдено")
            login(request, user)
            return redirect("successful_login")
        else:
            print("Користувача не знайдено")
            text_error = "Такого користувача не знайдено"
            return render(request, "registrationapp/autorization.html", context={"text_error" : text_error})
    return render(request, 'registrationapp/autorization.html')
```

- Функція приймає запит користувача як аргумент **(request)**.
- Якщо метод запиту `POST`, функція витягує дані з форми (ім'я користувача, пароль).
- Виконується спроба аутентифікації користувача за допомогою функції `authenticate`.
- Якщо користувач існує та аутентифікація успішна, виконується вхід користувача і перенаправлення на сторінку успішного входу.
- Якщо користувача не знайдено, повертається сторінка авторизації з повідомленням про помилку.
- Якщо метод запиту не `POST`, повертається сторінка авторизації.

### show_successful_login

Функція для відображення сторінки успішного входу

```python
def show_successful_login(request):
    if request.user.is_authenticated:
        return render(request, "japtuneapp/index.html")
    else:
        return redirect("login_user")
```

- Функція приймає запит користувача як аргумент **(request)**.
- Якщо користувач аутентифікований, повертається основна сторінка.
- Якщо користувач не аутентифікований, виконується перенаправлення на сторінку входу.

### logout_user

Функція для виходу користувача

```python
def logout_user(request):
    logout(request)
    return redirect("login")
```

- Функція приймає запит користувача як аргумент **(request)**.
- Виконується вихід користувача за допомогою функції `logout`.
- Після виходу виконується перенаправлення на сторінку входу.
