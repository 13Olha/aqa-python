# # import time
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from webdriver_manager.chrome import ChromeDriverManager
# #
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# #
# # # driver.get("http://selenium.dev")
# # #
# # # driver.quit()
# # time.sleep(10)
from selenium import webdriver
import time

mobile_emulation = { "deviceName": "iPhone SE" }

chrome_options = webdriver.ChromeOptions()


driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=chrome_options.to_capabilities()
)


driver.get("https://youtube.com")

time.sleep(10)
driver.quit()
