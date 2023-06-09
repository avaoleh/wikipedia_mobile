## Проект Mobile автотестов для приложения Wikipedia

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo_stacks/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo_stacks/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Appium" src="images/logo_stacks/appium.png"></code>
  <code><img width="5%" title="Browserstack" src="images/logo_stacks/browserstack.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo_stacks/tg.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяем
* Test empty search
* Test search
* Test search html tag
* Test search numbers
* Test search special symbols

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo_stacks/jenkins.png">  Запуск проекта в Jenkins
### [Job](https://jenkins.autotests.cloud/job/avaoleg_qa_guru_mobile_app/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/screenshots/jenkins.png)


<!-- Browserstack -->

### <img width="3%" title="Browserstack" src="images/logo_stacks/browserstack.png"> Запуск проекта в [Browserstack](https://www.browserstack.com)
##### После запуска сборки в Jenkins, тесты начинают проходить удаленно через Browserstack. Где в реальном времени можно следить за прохождением теста через логи.

![This is an image](images/screenshots/browserstack.png)

##### Для интеграции c Browserstack, в настройке сборки, в разделе .env указать необходимые креды. Пример кред, можно посмотреть в файле [.env_examples](https://github.com/avaoleh/wikipedia_mobile/blob/main/.env_examples)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo_stacks/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshots/allure_suites.png)

##### Видео прохождение теста
![This is an image](images/screenshots/tests_mobile.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2096/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/logo_stacks/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo_stacks/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/tg_bot.png)
