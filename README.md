Для запуска под Windows необходимо установить и запустить WSL

Задание
Курсовая работа состоит из двух частей. Первая часть, «Разработка сервиса», вам открылась в середине курса. Если вы уже выполнили эту часть, то сразу приступайте ко второй — «Доработке сервиса».

Если вы еще не начинали работу над курсовым проектом, тогда выполняйте первую часть, а затем переходите ко второй.

Удачи!

Критерии приемки курсовой работы
Интерфейс системы содержит следующие экраны: список рассылок, отчет проведенных рассылок отдельно, создание рассылки, удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя.
Реализовали всю требуемую логику работы системы.
Интерфейс понятен и соответствует базовым требованиям системы.
Все интерфейсы для изменения и создания сущностей, не относящиеся к стандартной админке, реализовали с помощью Django-форм.
Все настройки прав доступа реализовали верно.
Приложены фикстуры или созданы команды для заполнения базы данных (минимум — для рассылок, сообщений, клиентов, групп пользователей, блога)
Решение выложили на github.com/.
Посмотрите видео, оно поможет вам справиться с курсовой работой.


1. Разработка сервиса
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
Рассылка внутри себя должна содержать ссылки на модели «Сообщения и «Клиенты сервиса». Сообщение у рассылки может быть только одно, а вот клиентов может быть много. Выберите правильные типы связи между моделями.

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

Примечание

Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей либо добавлять вспомогательные модели.

Логика работы системы
После создания новой рассылки, если текущие дата и время больше даты и времени начала и меньше даты и времени окончания, должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
Если создается рассылка с временем старта в будущем, отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя сервиса.
По ходу отправки рассылки должна собираться статистика (см. описание сущностей «Рассылка» и «Попытка» выше) по каждой рассылке для последующего формирования отчетов. Попытка создается одна для одной рассылки. Формировать попытки рассылки для всех клиентов отдельно не нужно.
Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.
‍Рекомендации

Реализовать интерфейс можно с помощью UI kit Bootstrap.
Для работы с периодическими задачами можно использовать либо crontab-задачи в чистом виде, либо изучить дополнительно библиотеку: https://pypi.org/project/django-crontab/.
‍Периодические задачи — задачи, которые повторяются с определенной частотой, которая задается расписанием.

‍crontab — классический демон, который используется для периодического выполнения заданий в определенное время. Регулярные действия описываются инструкциями, помещенными в файлы crontab и в специальные каталоги.

Служба crontab не поддерживается в Windows, но может быть запущена через WSL. Поэтому если вы работаете на этой ОС, то решите задачу запуска периодических задач с помощью библиотеки apscheduler: https://pypi.org/project/django-apscheduler/.

Подробную информацию, что такое crontab-задачи, найдите самостоятельно.

2. Доработка сервиса
Контекст
Сервис по управлению рассылками пользуется популярностью, однако запущенный MVP уже не удовлетворяет потребностям бизнеса.

Доработайте ваше веб-приложение. А именно: разделите права доступа для различных пользователей и добавьте раздел блога для развития популярности сервиса в интернете.

Описание задач
Расширьте модель пользователя для регистрации по почте, а также верификации.
Используйте для наследования модель 
AbstractUser
.

Добавьте интерфейс для входа, регистрации и подтверждения почтового ящика.
Вы уже реализовывали такую задачу в рамках домашних работ. Попробуйте воспроизвести все шаги заново, чтобы закрепить процесс работы с кастомными пользователями в Django.

Реализуйте ограничение доступа к рассылкам для разных пользователей.
Реализуйте интерфейс менеджера.
Создайте блог для продвижения сервиса.
Функционал менеджера
Может просматривать любые рассылки.
Может просматривать список пользователей сервиса.
Может блокировать пользователей сервиса.
Может отключать рассылки.
Не может редактировать рассылки.
Не может управлять списком рассылок.
Не может изменять рассылки и сообщения.
Группу создавайте в админке. Права доступа для рассылок опишите в модели рассылки и назначьте группе через админку. Не забудьте сохранить группы фикстурой или создать команду для создания групп для отправки наставнику на проверку.

Функционал пользователя
Весь функционал дублируется из первой части курсовой работы, но теперь нужно следить за тем, чтобы пользователь не мог случайным образом изменить чужую рассылку и мог работать только со своим списком клиентов и со своим списком рассылок.


Подсказка

Продвижение
Блог

Реализуйте приложение для ведения блога. При этом отдельный интерфейс реализовывать не требуется, но необходимо настроить административную панель для контент-менеджера.

В сущность блога добавьте следующие поля:

заголовок,
содержимое статьи,
изображение,
количество просмотров,
дата публикации.
Главная страница

Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:

количество рассылок всего,
количество активных рассылок,
количество уникальных клиентов для рассылок,
три случайные статьи из блога.
Кеширование

Для блога и главной страницы самостоятельно выберите, какие данные необходимо кешировать, а также каким способом необходимо произвести кеширование.

Кеширование мы подробно разбирали в уроке «Кеширование и работа с переменными окружения». Можно вернуться к этому уроку, чтобы выбрать оптимальный способ кеширования данных и корректно произвести настройки.

Также не забудьте вынести чувствительные данные в переменные окружения и собрать шаблон для файла .env.