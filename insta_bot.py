from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
import time


class instaBot():
	
	def __init__(self,login, password, hashTag, photo_to_like):
		self.login = login
		self.password = password
		self.url = "https://www.instagram.com"
		self.hashTag = hashTag
		self.driver = webdriver.Firefox()
		self.photo_to_like = int(photo_to_like)
		

	def loginToAccount(self):
		
		self.driver.get(self.url)
		accept_terms_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
		time.sleep(3)
		login_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.login)
		pass_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
		login_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
		time.sleep(5)
		save_credentials = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
		time.sleep(5)
		turn_off_notifications = self.driver.find_element_by_class_name("HoLwm").click()

	def findHashTag(self):
		hastTag_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(self.hashTag)
		time.sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div").click()
		time.sleep(5)
	
	def likePhoto(self):
		
		for i in range(1,(self.photo_to_like+1)):
			if i == 1:
				photo = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[" + str(i) + "]").click()
				time.sleep(2)
				like = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
				next_photo = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
			else:
				like = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
				next_photo = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
			time.sleep(2)
		exit_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
		time.sleep(3)

	def logOut(self):
		profile_menu = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
		time.sleep(2)
		logout_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div").click()


def main():
	username = input("username: ")
	password = input("password: ")
	hashtag = input("hashtag (example: #cute): ")
	how_many = input("how many photos should I like?: ")




	user = instaBot(username,password,hashtag,how_many)
	user.loginToAccount()
	user.findHashTag()
	user.likePhoto()
	user.logOut()
	print("Thank You!")

if __name__ == "__main__":
	main()

