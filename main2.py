from colorama import Fore as color

class Aplication:
    def __init__(self, name, version):
        self.name = name
        self.version = version

class Youtube(Aplication):
    def __init__(self, name, version):
        super().__init__(name=name, version=version)
        

    def password_youtube(self):
        a = int(input("Pls write your password>>> "))
        if a == 228:
             print(f"{color.GREEN}Hello user!Successful login! :)")
        else:
            print(f"{color.RED}Wrong password :( ")

    def watch(self):
            print(f"{color.LIGHTRED_EX}__wacthing video__")
     
    def yt_notifications(self):
        print(f"{color.GREEN}You have 5 new notifications)")

class Telegram(Aplication):
    def __init__(self, name, version):
        super().__init__(name=name, version=version)

    def send_messege(self):
        print(f"{color.MAGENTA} message sended!")
    
    
    def tg_notifications(self):
        print(f"{color.GREEN}You have 3 new notifications)")
    

class Phone:
    
        

    def __init__(self, youtube_name = None, youtube_version = None, telegram_name = None, telegram_version = None, youtube = None, telegram = None):
        if None not in [youtube_name, youtube_version]:
            self.youtube = Youtube(name=youtube_name, version=youtube_version)
        else:
            if youtube:
                self.youtube = youtube
            else:
                self.youtube = None
        if None not in [telegram_name, telegram_version]:
            self.telegram = Telegram(name=telegram_name, version=telegram_version)
        else:
            if telegram:
                self.telegram = telegram
            else:
                self.telegram = None
    
    def __str__(self):
        return f"{color.YELLOW}App#1:{color.LIGHTRED_EX} {self.youtube.name} {self.youtube.version}\t{color.YELLOW}App#2: {color.BLUE}{self.telegram.name} {self.telegram.version}"
    
app1 = Youtube(name="Yotube", version=18.17)
app2 = Telegram(name="telegram", version=4.8)
xiaomi = Phone(youtube=app1, telegram=app2)

# Команди програми

# print(xiaomi) - виводе дані о програмах на телефоні
# xiaomi.telegram.send_messege() - відправляє повідомлення у телеграм
# xiaomi.youtube.password_youtube() - вмикає авторизацію( треба вести вірний пароль)
# xiaomi.youtube.watch() - вмикає прегляд відео



xiaomi.youtube.password_youtube()
# xiaomi.youtube.watch()
