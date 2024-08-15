pytest -v -s -n=2 --html=HtmlReports/my_report.html --alluredir=AllureReports"

allure serve "AllureReports"
