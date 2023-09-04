# Blog drf project

## Project description

This project is an api written in the DRF framework. 
The frontend is made with NuxtJS, it is stored in another [repository](https://github.com/saltitc/nuxtjs_blog). 
You can use Postman to test it, or you can clone an additional repository with the frontend.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them


+ [Python](https://www.python.org/downloads/)
+ [PyCharm IDE](https://www.jetbrains.com/ru-ru/pycharm/download/?section=windows)
+ [Postman](https://www.postman.com/downloads/)


### Installing

A step by step series of examples that tell you how to get a development env running

+ Create a folder for the repository and create a virtual environment in it. To do this, launch a terminal(or cmd) and enter the following commands
```
mkdir drf-blog
cd drf-blog
python3 -m venv drfvenv  # for macOS
python -m venv drfvenv  # for Windows
```
+ Open this project in Pycharm IDE and enter the following commands in the built in terminal to clone the repository and install the packages
```
git clone https://github.com/saltitc/drf-blog.git
pip install --upgrade pip
pip install -r drf-blog/requirements.txt
```
+ Create a drf-blog/.env file and create variables
```
DEBUG=on
SECRET_KEY=$s!5te285=l%92yce#ul=vy+c2*f4_s5y8aq-(fu%m24^

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_HOST_USER=your_email_adress
EMAIL_HOST_PASSWORD=your_email_password
```
> + You can generate secret key [here](https://djecrety.ir).
> + Emails (you can use yandex, gmail and others, the instruction will be on setting up the Yandex server):
>>   1. Create a yandex account.
>>   2. Go to settings > mail programs and tick all the boxes
>>    <img width="1244" alt="image" src="https://github.com/saltitc/booking/assets/114296895/6e1723e5-8afc-48ae-a7ce-afc9bbae50f5">
>>   3. Up-to-date information about the email host, port and the use of ssl(specify True if ssl connection security) is available [here](https://yandex.ru/support/mail/mail-clients/others.html#smtpsetting__smtp-config-prog)
>>   4. Email host user and password is your email address and password


+ Make database migrations and load fixtures
  ```
  python3 drf-blog/manage.py makemigrations
  python3 drf-blog/manage.py migrate
  python3 drf-blog/manage.py createsuperuser
  python3 drf-blog/manage.py loaddata posts.json
  ```
  > If you get ImportError: cannot import name 'ugettext_lazy' from 'django.utils.translation'
  follow this [link](https://forum.djangoproject.com/t/importerror-cannot-import-name-ugettext-lazy-from-django-utils-translation/10943)

+ Run the server with this command and go to the [address](http://127.0.0.1:8000/) in your browser
  ```
  python3 drf-blog/manage.py runserver
  ```

If you did everything according to the instructions, now you can use the site and check its functionality.
___

## Built With

* [Django Rest Framework](https://www.django-rest-framework.org)
