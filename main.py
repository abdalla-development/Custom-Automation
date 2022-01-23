from selenium import webdriver
import smtplib
import datetime as dt

yahoo_email = "python_test_stmp@yahoo.com"  # Yahoo Account
yahoo_app_password = "ulvcorpqhtzwptgj"
yahoo_get_way = "smtp.mail.yahoo.com"


# Initializing selenium
chrome_driver_path = "C:/Code Devolopment/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/")

# Get Beginners
beginners_title = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/a').text

beginners_first = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/ul/li[2]/a').text.split(".")[1]
beginners_first_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/ul/li[2]/a').get_attribute("href")

beginners_second = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/ul/li[2]/a').text.split(".")[1]
beginners_second_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/ul/li[3]/a').get_attribute("href")

beginners_third = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/ul/li[2]/a').text.split(".")[1]
beginners_third_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[2]/ul/li[4]/a').get_attribute("href")


# Get Intermediate
intermediate_title = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/a').text

intermediate_first = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/ul/li[1]/a').text.split(".")[1]
intermediate_first_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/ul/li[1]/a').get_attribute("href")

intermediate_second = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/ul/li[2]/a').text.split(".")[1]
intermediate_second_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/ul/li[2]/a').get_attribute("href")

intermediate_third = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/ul/li[3]/a').text.split(".")[1]
intermediate_third_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[3]/ul/li[3]/a').get_attribute("href")

# Get Advanced
advanced_title = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/a').text

advanced_first = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/ul/li[1]/a').text.split(".")[1]
advanced_first_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/ul/li[1]/a').get_attribute("href")

advanced_second = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/ul/li[2]/a').text.split(".")[1]
advanced_second_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/ul/li[2]/a').get_attribute("href")

advanced_third = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/ul/li[3]/a').text.split(".")[1]
advanced_third_link = driver.find_element_by_xpath('//*[@id="ez-toc-container"]/nav/ul/li[4]/ul/li[3]/a').get_attribute("href")

driver.quit()
saved = f"Subject: Top Python Projects Ideas\n\n {beginners_title}\n{beginners_first}\nlink: {beginners_first_link}\n" \
        f"{beginners_second}\nlink: {beginners_second_link}\n{beginners_third}\nlink: {beginners_third_link}\n" \
        f"{intermediate_title}\n{intermediate_first_link}\nlink: {intermediate_first_link}\n{intermediate_second}\n" \
        f"link: {intermediate_second_link}\n{intermediate_third}\nlink: {intermediate_third_link}\n{advanced_title}\n" \
        f"{advanced_first}\nlink: {advanced_first_link}\n{advanced_second}\nlink: {advanced_second_link}\n" \
        f"{advanced_third}\nlink: {advanced_third_link}\n"
# print(saved)
with smtplib.SMTP(yahoo_get_way) as connection:
    connection.starttls()
    connection.login(user=yahoo_email, password=yahoo_app_password)
    connection.sendmail(from_addr=yahoo_email, to_addrs=yahoo_email, msg=f"{saved}")

