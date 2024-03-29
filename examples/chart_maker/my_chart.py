from seleniumbase import BaseCase


class MyChartMakerClass(BaseCase):
    def test_chart_maker(self):
        self.create_presentation()
        self.create_pie_chart(title="Automated Tests")
        self.add_data_point("Passed", 4, color="#95d96f")
        self.add_data_point("Untested", 2, color="#eaeaea")
        self.add_data_point("Failed", 1, color="#f1888f")
        self.add_data_point("Persik", 5, color="#f1475f")
        self.add_slide("<p>Results</p>" + self.extract_chart())
        self.begin_presentation(filename="my_chart.html")
