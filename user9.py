def user9():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    from user10 import user10

    # Opens the Chrome browser and go to the login Instagram page.
    driverPath = 'D:\Programming\Python Projects\Personal Projects\chromedriver.exe'
    webdriver = webdriver.Chrome(executable_path=driverPath)
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(2)

    # Holds the user's username and password that will be used.
    username = ''
    password = ''

    # Find the username and password elements and fills them in with the user's login.
    userElement = webdriver.find_element_by_name('username')
    userElement.send_keys(username)
    passElement = webdriver.find_element_by_name('password')
    passElement.send_keys(password)

    # Find the login button element and click it to login into the user's account.
    login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
    login.click()
    sleep(3)

    # Find the "Not Now" element of the notification popup and click it to make it go away.
    notNow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notNow.click()
    sleep(1)

    # Direct the browser to Blanson's Chick-fil-a page.
    webdriver.get('https://www.instagram.com/p/B2epau2FUiI/')
    sleep(1)

    # Find the comment box on the page and click on it.
    commentBox = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea')
    commentBox.click()

    # This will be the comment that will be posted.
    comment = 'Blanson Bold! Blanson Gold!'

    # Comment infinitely (will be stopped inevitably by Instagram however).
    while True:
        # Find the comment box again to let the program know we are working with it again.
        commentBox = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea')
        # Input the comment in the comment box.
        commentBox.send_keys(comment)
        # Enter to post the comment.
        commentBox.send_keys(Keys.ENTER)
        sleep(.5)
        # Try to scan the page for the popup that blocks the user from commenting.
        try:
            webdriver.find_element_by_css_selector('body > div.Z2m7o > div > div > div > p')
            sleep(2)
            # If it gets to this point then it has blocked the user, and we close this browser.
            webdriver.close()
            # Call the next function to start another browser and user.
            user10()
        # If it is not there, then it will cause an error and we will let the program run normally.
        except:
            pass
        # Wait 7 seconds to give the comment time to be uploaded.
        sleep(7)
user9()