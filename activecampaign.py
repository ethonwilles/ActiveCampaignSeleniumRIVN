from selenium import webdriver

class Active():
    
        

    def start(self, account, username, password):
        self.driver = webdriver.Chrome()
        xpath = self.driver.find_element_by_xpath
        self.account = account
        self.username = username
        self.password = password


        self.driver.get("https://www.activecampaign.com/login/?section=privacy&s=ccpa")
        account_input = xpath('//*[@id="accountname"]')
        account_input.send_keys(self.account)

        login_btn = xpath('//*[@id="loginform"]/input[1]')
        login_btn.click()

        try:
            state_input = xpath('//*[@id="_form_5_"]/div[1]/div[3]/div/select')
            utah = xpath('//*[@id="_form_5_"]/div[1]/div[3]/div/select/option[59]')
            state_input.click()
            utah.click()
            rights = xpath('//*[@id="_form_5_"]/div[1]/div[3]/div/select/option[59]')
            rights.click()
            rights.click()
            rights = xpath('//*[@id="_form_5_"]/div[1]/div[4]/div/select')
            rights.click()
            delete = xpath('//*[@id="_form_5_"]/div[1]/div[4]/div/select/option[4]')
            delete.click()
        except:
            email_box = xpath('//*[@id="user"]')
            email_box.send_keys(self.username)

            pass_box = xpath('//*[@id="pass"]')
            pass_box.send_keys(self.password)

            login = xpath('//*[@id="log_user"]/div[4]/input')
            login.click()

            state_input = xpath('//*[@id="_form_5_"]/div[1]/div[3]/div/select')
            utah = xpath('//*[@id="_form_5_"]/div[1]/div[3]/div/select/option[59]')
            state_input.click()
            utah.click()
            rights = xpath('//*[@id="_form_5_"]/div[1]/div[3]/div/select/option[59]')
            rights.click()
            rights.click()
            rights = xpath('//*[@id="_form_5_"]/div[1]/div[4]/div/select')
            rights.click()
            delete = xpath('//*[@id="_form_5_"]/div[1]/div[4]/div/select/option[4]')
            delete.click()

            desc = xpath('//*[@id="_form_5_"]/div[1]/div[5]/div/textarea')
            submit = xpath('//*[@id="_form_5_submit"]')

            desc.send_keys("CCPA Compliance")
            submit.click()
            
            print("Success!")
            self.driver.quit()

    def docs(self):
        print("""
        HOW TO USE:
            activecampaign.start({CLIENT_EMAIL}, {CLIENT_USERNAME}, {CLIENT_PASSWORD})
        """)
activecampaign = Active()
