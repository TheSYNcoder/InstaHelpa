from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os



class App:
    def __init__( self, username , password, path):

        self.username = username
        self.password = password
        self.path  =path

        self.url = 'https://www.instagram.com/'
        chromedriver = self.path
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.error =False
        self.following=[]
        self.followers=[]
        self.unfollow=[]
        self.webelem=[]

    def open(self):
        try:
            self.driver.get("https://www.instagram.com/")
            sleep(3)
        except Exception as e:
            error = True
            print("Page won't open , you may need to update google chrome")

    def LogInPage(self):
        if self.error is False:
            try:
                login_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
                login_element.click()
                sleep(5)
            except Exception as e:
                print('Feature not available')
                self.error = True

    def LogIn(self ):
        if self.error is False:
            try:
                username_field = self.driver.find_element_by_xpath('//label[@class="f0n8F "]/input[@aria-label="Phone number, username, or email"]')
                username_field.clear()
                username_field.send_keys(self.username)
                password_field = self.driver.find_element_by_xpath('//label[@class="f0n8F "]/input[@aria-label="Password"]')
                password_field.clear()
                password_field.send_keys(self.password)
                password_field.submit()
                sleep(5)
            except Exception as e:
                print(e)
                self.error = True
                print('Cant log in ')

    def closePopUp(self):
        if self.error is False:
            try:
                notNow =self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
                notNow.click()
            except:
                self.error = True
                print('Something wrong ..')

    def openProfile(self):
        if self.error is False:
            try:
                profile =self.driver.find_element_by_xpath('//div[@class="XrOey"]/a[@href="/{}/"]'.format(self.username))
                profile.click()
                sleep(4)
            except Exception as e:
                print('Wrong')
                print(e)
                self.error =True

    def openFollowingPage(self):
        if self.error is False:
            try:
                follower = self.driver.find_element_by_xpath('//a[@href="/{}/following/"]'.format(self.username))
                follower.click()
                sleep(2)
            except Exception as e:
                print('Wrong with follower page')
                self.error = True

    def openFollowersPage(self):
        if self.error is False:
            try:
                follower = self.driver.find_element_by_xpath('//a[@href="/{}/followers/"]'.format(self.username))
                follower.click()
                sleep(2)
            except Exception as e:
                print('Wrong with follower page')
                self.error = True

    def getFollowers(self):
        count =1
        if self.error is False:
            while count <2:
                try:
                    self.ScrollDownFoll()
                    sleep(1)
                    print('Scrolling complete')
                    lis = self.driver.find_elements_by_xpath('//div[@class="PZuss"]/li')
                    # print(div)
                    # lis = div.find_elements_by_xpath('//li//div[@class="                  Igw0E     IwRSH      eGOV_     ybXk5    _4EzTm                                                                                                              "]/a')
                    # items= div.find_elements_by_tag_name("li")
                    print(len(lis))
                    print(lis)
                    # items = items.
                    for item in lis:
                        # i = item.find_element_by_xpath('//div[@class="                  Igw0E     IwRSH      eGOV_     ybXk5    _4EzTm                                                                                                              "]')
                        item = item.find_element_by_xpath('.//a')
                        # self.following.append(item.get_attribute("href"))
                        self.followers.append(item.get_attribute("href"))
                    # print(self.following)
                    button = self.driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]')
                    self.driver.execute_script('document.getElementsByClassName(\'dCJp8 afkep\')[1].click();')
                    # button.click()
                    sleep(1)
                except Exception as e:
                    print(e)
                    print('Wrong')
                    # self.error = True
                count+=1

    def getFollowing(self):
        count =1
        if self.error is False:
            while count <2:
                try:
                    self.ScrollDownFoll()
                    sleep(1)
                    print('Scrolling complete')
                    lis = self.driver.find_elements_by_xpath('//div[@class="PZuss"]/li')
                    # print(div)
                    # lis = div.find_elements_by_xpath('//li//div[@class="                  Igw0E     IwRSH      eGOV_     ybXk5    _4EzTm                                                                                                              "]/a')
                    # items= div.find_elements_by_tag_name("li")
                    print(len(lis))
                    print(lis)
                    # items = items.
                    for item in lis:
                        # i = item.find_element_by_xpath('//div[@class="                  Igw0E     IwRSH      eGOV_     ybXk5    _4EzTm                                                                                                              "]')

                        item = item.find_element_by_xpath('.//a')
                        # self.following.append(item.get_attribute("href"))
                        self.following.append(item.get_attribute("href"))
                    # print(self.following)
                    button =self.driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]')
                    self.driver.execute_script('document.getElementsByClassName(\'dCJp8 afkep\')[1].click();')
                    # button.click()
                    sleep(1)
                except Exception as e:
                    print(e)
                    print('Wrong')
                    # self.error = True
                count+=1

    def ScrollDownFoll(self):

        try:
                #                             We 'll scroll down 10 times
                #             OR   CAN BE DONE BY COUNTING THE NO OF IMAGES FIND XPATH OF THE NUMBER.text.replace(",","")
                #                 THEN SCROLLING ACCORDING NO OF IMAGES LOADED IN A SCROLL
            js_code ='function sleep(sec){var start =new Date().getTime();for (var i =0; i < 1e7; i++){if ((new Date().getTime()- start) > sec)break;}} ' \
                     'for ( var i =0 ; i < 1000; ) {' \
                     'var x = document.querySelector("div[class=\'isgrP\']");' \
                     'x.scrollTo(0,i+100);' \
                     'i=i+100;' \
                     'sleep(1000)}'
            js_cc ='var x = document.querySelector("div[class=\'isgrP\']");' \
                    'x.scrollTo(0,x.scrollHeight);'
            js_init = 'var x = document.querySelector("div[class=\'isgrP\']");' \
                        'x.scrollTo(0,12*40);'
            js_start = 'var x = document.querySelector("div[class=\'isgrP\']");' \
                          'x.scrollTo(0,0);'
            js_he = 'var x = document.querySelector("div[class=\'isgrP\']");' \
                    'return x.scrollHeight;'

            # for i in range(15):
            #     self.driver.execute_script(js_code)
            #     sleep(4)
            #
            print('Scrolling ...')
            self.driver.execute_script(js_init)
            self.driver.implicitly_wait(2)
            sleep(2)

            # for i in range(10):
            #     self.driver.execute_script(js_cc)
            #
            #     print('Scrolling {}-th time'.format(i+1))
            SCROLL_PAUSE_TIME = 3

                # Get scroll height
            last_height = self.driver.execute_script(js_he)
            while True:
                    # Scroll down to bottom
                self.driver.execute_script(js_cc)

                    # Wait to load page
                self.driver.implicitly_wait(2)
                sleep(SCROLL_PAUSE_TIME)

                # self.driver.execute_script(js_start)

                    # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script(js_he)
                print(new_height)
                if new_height == last_height:
                    break
                last_height = new_height
            sleep(3)
            self.driver.execute_script(js_cc)
            # sleep(3)
            # self.driver.execute_script(js_cc)
            self.driver.execute_script(js_start)
        except Exception as e:
            print(e)

            print("Can't scroll")


    def equal(self , following , follower):
        

        if  following == follower:
            return 1
        return 0

    def performUnfollow(self):
        pass
    def UnFollow(self):
        count = 1
        if self.error is False:
            while count < 2:
                try:
                    self.openFollowingPage()
                    sleep(1)
                    self.ScrollDownFoll()
                    sleep(1)
                    print('Scrolling complete')
                    lis = self.driver.find_elements_by_xpath('//div[@class="PZuss"]/li')
                    # print(div)
                    # lis = div.find_elements_by_xpath('//li//div[@class="                  Igw0E     IwRSH      eGOV_     ybXk5    _4EzTm                                                                                                              "]/a')
                    # items= div.find_elements_by_tag_name("li")
                    print(len(lis))
                    print(lis)
                    # items = items.
                    for item in lis:
                        # i = item.find_element_by_xpath('//div[@class="                  Igw0E     IwRSH      eGOV_     ybXk5    _4EzTm                                                                                                              "]')
                        i = item.find_element_by_xpath('.//a').get_attribute("href")
                        # self.following.append(item.get_attribute("href"))
                        print(len(self.unfollow))
                        if i in self.unfollow:
                            # self.driver.execute_script('document.getElementByClassName(\'sqdOP  L3NKy   _8A5w5    \')')
                            button = item.find_element_by_xpath('.//button[@class="sqdOP  L3NKy   _8A5w5    "]')
                            button.click()
                            self.driver.implicitly_wait(2)
                            sleep(2)
                            print('do you want to unfollow {} , press y/n'.format(i))
                            ans = input()
                            if ( ans == 'y'):
                                self.driver.execute_script('document.getElementsByClassName(\'aOOlW -Cab_   \')[0].click();')
                            #unfollow = self.driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]')
                            # cancel = self.driver.find_element_by_xpath('//button[class="aOOlW   HoLwm "]')
                            else:
                                self.driver.execute_script('document.getElementsByClassName(\'aOOlW   HoLwm \')[0].click();')
                            sleep(2)


                    # print(self.following)
                    button = self.driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]')
                    self.driver.execute_script('document.getElementsByClassName(\'dCJp8 afkep\')[1].click();')
                    # button.click()
                    sleep(1)
                except Exception as e:
                    print(e)
                    print('Wrong')
                    self.error = True
                count += 1

    def write(self , person):
        # item = person.find_element_by_xpath('.//a')
        print('Need to unfollow ', end="")
        print(person)

    def iterate(self):

        for following in self.following:
            check =0
            for follower in self.followers:
                if self.equal(following , follower):
                    check =1
                    print('{} found in followers'.format(following))
                    break
            if check == 0: # need to unfollow
                self.write(following)
                self.unfollow.append(following)





def check():
    if (Inst.error):
        exit(0)
def run():
    print('Enter username')
    username = input()
    print('enter password')
    password =input()
    print('Please download chromedriver version according to your chrome can be found in settings and provide the path to it')
    path = input()
    Inst = App(username , password , path)
    Inst.open()
    check()
    print('Page opened')
    Inst.LogInPage()
    check()
    print('auth login done .')
    Inst.LogIn()
    check()
    print('Logged in')
    Inst.closePopUp()
    check()
    print('dialog box closed')
    Inst.openProfile()
    check()
    print('Profile opened')
    Inst.openFollowingPage()
    check()
    print('Following page opened')
    Inst.getFollowing()
    check()
    print('following fetched')
    Inst.openFollowersPage()
    check()
    print('Followers page opened')
    Inst.getFollowers()
    check()
    print('Followers fetched')
    Inst.iterate()
    check()
    print('values written')
    Inst.UnFollow()
    check()




run()

