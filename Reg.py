'''


    [+] All Rights To Mexaw Alotebi [+]
        - Falcon Digital Community -
'''
try:
    import sys
    import requests
    import random
    import uuid
    import threading
    import time
    import queue
except:
    print("[+] Install Requests Please [+]")
    input()
    sys.exit()

prox = open('proxy.txt', 'r').read().splitlines()


head = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTBw==',
            'User-Agent': 'Instagram 35.0.0.20.96 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; Li0N; vbox86p; vbox86; en_US; 95414347)',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'Accept': '*/*'
}

url = 'https://i.instagram.com/api/v1/accounts/create/'
my_lock = threading.Lock()
class KingMexawChecker():
    def __init__(self,target,password,email,thread,timeout,qa):
        self.target = target
        self.password = password
        self.email = email
        self.thread = thread
        self.timeout = timeout
        self.counter = 0
        self.banned = 0 
        self.qa = qa
        self.q = queue.Queue()
        
        print("[+] Falcon Digital Checker © [+]")
        if self.qa == 1:
            for _ in range(self.thread+1):
                t = threading.Thread(target=self.checker_registry).start()
                time.sleep(0.0)
        else:
            try:
                list_open = open("list.txt","r").read().splitlines()
                for i in list_open:
                    if i =="":
                        continue
                    self.q.put(i)

                for _ in range(self.thread+1):
                    t = threading.Thread(target=self.checker_14_days).start()
                    time.sleep(0.0)

            except:
                print("Please Create list.txt")
                input()
                sys.exit()

    def randomProxies(self):
        proxy1 = str(random.choice(prox))
        pro2 = {
            'http': 'http://{}'.format(proxy1),
            'https': 'https://{}'.format(proxy1)
        }
        return pro2
    def count(self):
        self.counter+=1
    def bann(self):
        self.banned+=1
    def checker_14_days(self):
        while 1:
            user = str(self.q.get)
            try:
                r = requests.Session()
                my_own = uuid.uuid1()
                Falcon = r.post(url, data={
                    'email': "mexaw@gmail.com",
                    'password': "14_days_lol?",
                    'username': user,
                    'first_name': 'Falcon Digital Checker',
                    'phone_id':my_own,
                    'device_id':my_own
                    },
                    proxies=self.randomProxies(),
                    headers=head)
    
                if ('"error_type": "username_held_by_others"') in Falcon.text:
                    print(f'Catch 14 Days :{self.target}')
                    with open("list_14_days.txt","a") as wr:
                        wr.write(self.target+"\n")
                self.count() if not Falcon.status_code == 429 else self.bann()
                with my_lock:
                    print(f"Target:{user} , Attempts: {self.counter}, Spam:{self.banned}",end="\r",flush=True)
            except:
                self.q.put(user)
                

            
    def checker_registry(self):
        while 1:
            try:
                r = requests.Session()
                my_own = uuid.uuid1()
                Falcon = r.post(url, data={
                    'email': self.email,
                    'password': self.password,
                    'username': self.target,
                    'first_name': 'Falcon Digital Checker',
                    'phone_id':my_own,
                    'device_id':my_own
                    },
                    proxies=self.randomProxies(),
                    headers=head)
                if ('"message": "challenge_required"') in Falcon.text:
                    print(f'Fucked {self.target}')
                    with open('Reg_Done_FalconDigitalC.txt', 'a') as wr:
                        wr.write('Username:' + self.target + ',' + 'Email:' + self.email + ',' + 'password:' + self.password + '\n')




                self.count() if not Falcon.status_code == 429 else self.bann()
                with my_lock:
                    print(f"Attempts: {self.counter}, Spam:{self.banned}",end="\r",flush=True)
            
            
            except:
                print('Time Out Or ')

if __name__ == "__main__":
    print("""
    
        [+] Falcon Digital Checker Open Source [+]
    - Dont Be Script Kid and Steal it , Just Learn And Wish Me luck 
    - Not Resp for Bad Use , Falcon Digital Community Invite Any Programmer To Our Community :) 
    - Instagram @31421 - @FalconDigitalCommunity

    """)
    print("[+] 1 - Checker Reg 2 - 14 Days [+]")
    question = int(input("Chooce:"))
    threads = int(input("threads:"))
    timeout = int(input("timeout 1-5:"))

    if question == 2:
        KingMexawChecker(None,None,None,threads,timeout,2)

    else:
        email = str(input("email:"))
        password = str(input("password:"))
        target = str(input("target:"))
        KingMexawChecker(target,password,email,threads,timeout,1)

