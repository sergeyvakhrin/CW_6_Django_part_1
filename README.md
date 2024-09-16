добавить проверку на создание дублей электронной почты


# CW_6_Django_part_1

1. Условие проекта
1 из 2
Вы познакомились с основами Django и теперь можете выполнить серьезную задачу — создать сервис управления рассылками. Это первая часть курсовой работы, в которой вы закрепите полученные знания и научитесь применять их на практике. После выполнения этой части курсовой работы вы продолжите изучать Django, будете совершенствовать свой проект и добавлять новые функции.

Контекст
Чтобы удержать текущих клиентов, часто используют вспомогательные, или «прогревающие», рассылки для информирования и привлечения клиентов.

Разработайте сервис управления рассылками, администрирования и получения статистики.

Описание задач
Реализуйте интерфейс заполнения рассылок, то есть CRUD-механизм для управления рассылками.
Помните, что CRUD состоит из просмотра списка, просмотра, создания, редактирования и удаления одной сущности.

Реализуйте скрипт рассылки, который работает как из командной строки, так и по расписанию.

Подсказка

Добавьте настройки конфигурации для периодического запуска задачи при необходимости.

Подсказка

Сущности системы
Клиент сервиса:
контактный email,
Ф. И. О.,
комментарий.
Обратите внимание, что клиенты сервиса — это не пользователи сервиса. Клиенты — это те, кто получает рассылки, а пользователи — те, кто создает эти рассылки.

Клиенты — неотъемлемая часть рассылки. Для них также необходимо реализовать CRUD-механизм!

Рассылка (настройки):
дата и время первой отправки рассылки;
периодичность: раз в день, раз в неделю, раз в месяц;
статус рассылки (например, завершена, создана, запущена).
Рассылка внутри себя должна содержать ссылки на модели «Сообщения» и «Клиенты сервиса». Сообщение у рассылки может быть только одно, а вот клиентов может быть много. Выберите правильные типы связи между моделями.

Пример: компания N захотела создать на нашем сервисе рассылку. Создала для нее сообщение, которое будет отправлено клиентам, наполнила базу клиентов своими данными с помощью графического интерфейса сайта, затем перешла к созданию рассылки: указала необходимые параметры, сообщение и выбрала клиентов, которым эта рассылка должна быть отправлена.

Сообщение для рассылки:
тема письма,
тело письма.
Сообщения — неотъемлемая часть рассылки. Для них также необходимо реализовать CRUD-механизм!

Попытка рассылки:
дата и время последней попытки;
статус попытки (успешно / не успешно);
ответ почтового сервера, если он был.

Подсказка

Примечание:

Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей либо добавлять вспомогательные модели.

Логика работы системы
После создания новой рассылки, если текущие дата и время больше даты и времени начала и меньше даты и времени окончания, должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
Если создается рассылка с временем старта в будущем, отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя сервиса.
По ходу отправки рассылки должна собираться статистика (см. описание сущностей «Рассылка» и «Попытка» выше) по каждой рассылке для последующего формирования отчетов. Попытка создается одна для одной рассылки. Формировать попытки рассылки для всех клиентов отдельно не нужно.
Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.
‍Рекомендации

Реализовать интерфейс можно с помощью UI kit Bootstrap.
Для работы с периодическими задачами можно использовать либо crontab-задачи в чистом виде, либо изучить дополнительно библиотеку: https://pypi.org/project/django-crontab/.
‍Периодические задачи — задачи, которые повторяются с определенной частотой, которая задается расписанием.

‍crontab — классический демон, который используется для периодического выполнения заданий в определенное время. Регулярные действия описываются инструкциями, помещенными в файлы crontab и в специальные каталоги.

‍Рекомендации

Служба crontab не поддерживается в Windows, но может быть запущена через WSL. Поэтому, если вы работаете на этой ОС, то решите задачу запуска периодических задач с помощью библиотеки https://pypi.org/project/django-apscheduler/.
Подробную информацию, что такое crontab-задачи, найдите самостоятельно.
