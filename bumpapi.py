from bs4 import BeautifulSoup
import requests
from difflib import unified_diff
import time

class BumpAPI:
    def __init__(self):
        self.target_url = None
        self.page_text = None
        print("🔬 Welcome to BumpAPI - a library by BumpAPI Labs for interacting with the site's external API.")
        print("⚠️ Before using this library to interact with any website, it is crucial to thoroughly understand and comply with the terms of service of the targeted sites. We do not assume any responsibility for the usage of this library.")
        print("⚗️ Please note that BumpAPI is currently in a testing phase and may contain bugs or errors. We are actively working to enhance its reliability and stability over time.")
        print("-" * 20)

    def notsecret(self):
            ascii_art = r'''
     _                             _    ____ ___          __  
    | |__  _   _ _ __ ___  _ __   / \  |  _ \_ _|  _____  \ \ 
    | '_ \| | | | '_ ` _ \| '_ \ / _ \ | |_) | |  |_____|  | |
    | |_) | |_| | | | | | | |_) / ___ \|  __/| |  |_____|  | |
    |_.__/ \__,_|_| |_| |_| .__/_/   \_\_|  |___|          | |
                          |_|                             /_/ 
    '''
            print(ascii_art)

    def target(self, url):
        self.target_url = url

    def executor(self, with_easter_egg=False):
        if self.target_url:
            try:
                response = requests.get(self.target_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    self.page_text = soup.get_text()
                    print(f"BumpAPI Target: {self.target_url} 🧪")
                    if with_easter_egg:
                        self.display_easter_egg()
                else:
                    print("Failed to fetch the target. Check URL or connectivity.")
            except requests.RequestException as e:
                print(f"Request Exception: {e}")
        else:
            print("No target URL set. Please use bump.target('URL') to set the target.")

    def display_easter_egg(self):
        ascii_heart = r'''




                                                                                       
                                                          
                                                          
         ##############            ##############         
       ###################      ###################       
     #######################  #######################     
    ##################################################    
   ####################################################   
   ####################################################   
   ####################################################   
   ####################################################   
   ####################################################   
   ####################################################   
   ####################################################   
    ##################################################    
     ################################################     
      ##############################################      
       ############################################       
        ##########################################        
          ######################################          
            ##################################            
              ##############################              
                ##########################                
                   ####################                   
                     ################                     
                       ############                       
                         ########                         
                           ####                           
                                                          
                                                          
                                                                                                         


                                            '''
        print(ascii_heart)
        print("\nDear User,\n\nThank you so much for using the BumpAPI library; it means a lot to us. We hope you find our library helpful, and we wish your projects great success and usefulness, as well as good health and many joyful moments in life! 💓\n\nBe kind! ❤️")

    def text(self):
        if self.target_url:
            try:
                response = requests.get(self.target_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Виділення тексту без HTML-тегів
                    text = soup.get_text()
                    print(text)
                else:
                    print("Failed to fetch the target. Check URL or connectivity.")
            except requests.RequestException as e:
                print(f"Request Exception: {e}")
        else:
            print("No target URL set. Please use bump.target('URL') to set the target.")

    def cut(self, start_keyword, end_keyword):
        if self.target_url:
            try:
                response = requests.get(self.target_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Виділення тексту без HTML-тегів
                    text = soup.get_text()
                    start_index = text.find(start_keyword)
                    if start_index != -1:
                        end_index = text.find(end_keyword, start_index + len(start_keyword))
                        if end_index != -1:
                            # Виділення тексту між ключовими словами
                            selected_text = text[start_index + len(start_keyword):end_index]
                            print(selected_text)
                        else:
                            print(f"End keyword '{end_keyword}' not found after '{start_keyword}' on the page.")
                    else:
                        print(f"Start keyword '{start_keyword}' not found on the page.")
                else:
                    print("Failed to fetch the target. Check URL or connectivity.")
            except requests.RequestException as e:
                print(f"Request Exception: {e}")
        else:
            print("No target URL set. Please use bump.target('URL') to set the target.")

    def find(self, search_text):
        if self.page_text:
            count = self.page_text.count(search_text)
            if count > 0:
                print(f"Found '{search_text}' {count} times on the page.")
                # Додайте інші операції, якщо потрібно
            else:
                print(f"'{search_text}' not found on the page.")
        else:
            print("No page text available. Use bump.executor() first.")

    def code(self, language):
        if self.page_text:
            soup = BeautifulSoup(requests.get(self.target_url).content, 'html.parser')
            if language.lower() == 'html':
                print(soup.prettify())
            elif language.lower() == 'css':
                print('oops, bumpAPI dont support css scratch')
                pass
            elif language.lower() == 'js':
                print('oops, bumpAPI dont support JavaScript scratch')
                pass
            else:
                print("Invalid language. Please use 'html'.")
        else:
            print("No page text available. Use bump.executor() first.")

    def refresh(self, refresh_type):
        if refresh_type.lower() == 'type':
            if self.target_url:
                try:
                    response = requests.get(self.target_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        self.page_text = soup.get_text()
                        soup = BeautifulSoup(requests.get(self.target_url).content, 'html.parser')
                        print('Page is refreshed! 🔑')
                        print(soup.prettify())
                    else:
                        print("Failed to fetch the target. Check URL or connectivity.")
                except requests.RequestException as e:
                    print(f"Request Exception: {e}")
            else:
                print("No target URL set. Please use bump.target('URL') to set the target.")
        elif refresh_type.lower() == 'just':
            if self.target_url:
                try:
                    response = requests.get(self.target_url)
                    if response.status_code == 200:
                        print("Page refreshed.")
                    else:
                        print("Failed to fetch the target. Check URL or connectivity.")
                except requests.RequestException as e:
                    print(f"Request Exception: {e}")
            else:
                print("No target URL set. Please use bump.target('URL') to set the target.")
        else:
            print("Invalid refresh type. Please use 'type' or 'just'.")

    def links(self):
        if self.page_text:
            soup = BeautifulSoup(requests.get(self.target_url).content, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a', href=True)]
            return links
        else:
            print("No page text available. Use bump.executor() first.")

    def images(self, download=False):
        if self.page_text:
            soup = BeautifulSoup(requests.get(self.target_url).content, 'html.parser')
            images = [img.get('src') for img in soup.find_all('img', src=True)]
            if download:
                for index, img_url in enumerate(images, start=1):
                    img_data = requests.get(img_url).content
                    with open(f"image{index}.jpg", 'wb') as img_file:
                        img_file.write(img_data)
                print("Images downloaded successfully.")
            else:
                return images
        else:
            print("No page text available. Use bump.executor() first.")

    def summary(self):
        if self.page_text:
            lines = self.page_text.split('\n')
            summary = ' '.join([line.strip() for line in lines if line.strip()])
            print(summary)
        else:
            print("No page text available. Use bump.executor() first.")

    def stats(self):
        if self.page_text:
            soup = BeautifulSoup(requests.get(self.target_url).content, 'html.parser')
            tags = [tag.name for tag in soup.find_all()]
            tag_counts = {tag: tags.count(tag) for tag in set(tags)}
            print(tag_counts)
        else:
            print("No page text available. Use bump.executor() first.")

    def headers(self):
        response = requests.head(self.target_url)
        print(response.headers)

    def compare(self, target_url):
        response1 = requests.get(self.target_url)
        response2 = requests.get(target_url)
        diff = unified_diff(response1.text.splitlines(), response2.text.splitlines(), lineterm='')
        print('\n'.join(diff))

    def extract(self, title):
        if self.page_text:
            soup = BeautifulSoup(requests.get(self.target_url).content, 'html.parser')
            elements = soup.find_all(text=title)
            extracted_data = [el.parent for el in elements]
            return extracted_data
        else:
            print("No page text available. Use bump.executor() first.")

    def wait(self, seconds):
        print(f"Waiting for {seconds} seconds... 🕐")
        time.sleep(seconds)
        print("Wait complete. 🕛")

    def click(self, element_id):
        if self.page_text:
            try:
                response = requests.get(self.target_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    target_element = soup.find(id=element_id)
                    if target_element:
                        # Використовуємо JavaScript для кліку на елементі
                        script = f"document.getElementById('{element_id}').click();"
                        response = requests.post(self.target_url, data={"script": script})
                        print(f"Clicked on element with ID '{element_id}'.")
                    else:
                        print(f"Element with ID '{element_id}' not found on the page.")
                else:
                    print("Failed to fetch the target. Check URL or connectivity.")
            except requests.RequestException as e:
                print(f"Request Exception: {e}")
        else:
            print("No page text available. Use bump.executor() first.")

    def send(self, text):
        if self.page_text:
            try:
                response = requests.post(self.target_url, data={"text": text})
                print(f"Sent text '{text}' to the target.")
            except requests.RequestException as e:
                print(f"Request Exception: {e}")
        else:
            print("No page text available. Use bump.executor() first.")