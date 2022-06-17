from seleniumbase import BaseCase


class MyTourClass(BaseCase):
    def test_google_tour(self):
        self.open("https://google.com/ncr")
        self.wait_for_element('input[title="Search"]')


        self.create_tour(theme="dark")
        self.add_tour_step("Добро пожаловать в Google!", title="Тур-заглушка")
        self.add_tour_step("Введите свой запрос здесь.", 'input[title="Search"]')
        self.play_tour()

        self.highlight_type('input[title="Search"]', "Google")
        self.wait_for_element('[role="listbox"]')

        self.create_tour(theme="light")
        self.add_tour_step("Нажмите на кнопку поиска.", '[value="Google Search"]')
        self.add_tour_step("Или нажмите [ENTER].", '[title="Search"]')
        self.play_tour()

        self.highlight_type('input[title="Search"]', "GitHub kocteban\n")
        self.ad_block()
        self.wait_for_element("#search")


        self.create_tour(theme="bootstrap")
        self.add_tour_step("Другой тур:")
        self.play_tour(interval=3)

        self.open("https://www.google.com/maps/@42.3591234,-71.0915634,15z")
        self.wait_for_element("#searchboxinput")
        self.wait_for_element("#minimap")
        self.wait_for_element("#zoom")


        self.create_tour(theme="introjs")
        self.add_tour_step("Добро пожаловать в Google Maps", title="Заглушка")
        self.add_tour_step(
            "Локацию вводить сюда.", "#searchboxinput", title="Поле ввода"
        )
        self.add_tour_step(
            "Нажмите сюда чтобы отобразить запрос на карте.",
            "#searchbox-searchbutton",
            alignment="bottom",
        )
        self.add_tour_step(
            "Здесь можно выбрать направления.",
            'button[aria-label="Directions"]',
            alignment="bottom",
        )
        self.add_tour_step(
            "Вид со спутника.",
            'button[jsaction*="minimap.main;"]',
            alignment="right",
        )
        self.add_tour_step(
            "Приблизить.", "#widget-zoom-in", alignment="left"
        )
        self.add_tour_step(
            "Отдалить.", "#widget-zoom-out", alignment="left"
        )
        self.add_tour_step(
            "Кнопка 'Меню'..",
            'button[jsaction*="settings.open;"]',
            alignment="right",
        )
        self.add_tour_step(
            "Кликните сюда чтобы увидеть больше Google приложений.",
            '[title="Google apps"]',
            alignment="left",
        )
        self.add_tour_step(
            "Спасибо за использование!", title="Конец тура"
        )
        self.export_tour()
        self.play_tour()
