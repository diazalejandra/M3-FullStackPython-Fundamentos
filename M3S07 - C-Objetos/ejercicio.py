class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = False
        self.app = []
    
    def power_on(self):
        self.status = True
    
    def power_off(self):
        self.status = False
    
    def install_app(self, app):
        self.app.append(app)
    
    def uninstall_app(self, app):
        self.app.remove(app)

iphone = MobilePhone('Apple', 10.2, 8)
print(vars(iphone))

iphone.power_on()
print(vars(iphone))

iphone.install_app('Teams')
print(vars(iphone))

iphone.install_app('Whatsapp')
print(vars(iphone))

iphone.uninstall_app('Whatsapp')
print(vars(iphone))

iphone.power_off()
print(vars(iphone))



