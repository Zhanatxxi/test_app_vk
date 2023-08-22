<h2> Тестовое задание </h2>

Сперва для запуска нужно переименовать файль .env_example на .env
для получения SERVICE_KEY, нужно  создать приложение на сайте https://vk.com/editapp?act=create
обязательно выбрать опцию Standalone.
Для TOKEN нужно перейти по ссылке https://vkhost.github.io/


<strong> first_command: docker build --tag 'vk_app:0.0.1' . <br/>
second_command: docker run -p 8000:8000 --name app vk_app:0.0.1 </strong>
