class Phone:
    def __init__(self, phone_model):
        self.model = phone_model
        self._loading()
        self._serial_number = 5555555

    def call(self):
        print('calling')

    def _loading(self):
        print(self.model, 'loading')

    def get_serial_number(self):
        return self._serial_number


# my_phone_1 = Phone('nokia')
# my_phone_2 = Phone('samsung')
#
# print(my_phone_1.get_serial_number())
class SmartPhone(Phone):

    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')


class IPhone(SmartPhone):

    def __init__(self, phone_model):
        super().__init__(phone_model)
        print('Showing logo')

    def sms(self):
        print('Imessgage sending')

    def player(self):
        print('music')

    def browser(self):
        print('serfing')


iphone = IPhone('6')

class NextGenSmartPhone(IPhone):
    def touch_id(self):
        print('hold finger')

    def pay(self):
        print('pay is working')


class Samsung(NextGenSmartPhone):
    def call(self):
        print('samsung call')


class Huawei(NextGenSmartPhone):
    def call(self):
        print('huawei call')

my_sams = Samsung('s10')
my_huaw = Huawei('MDL')

def my_call(phone):
    phone.call()


my_call(my_sams)
my_call(my_huaw)
my_call(iphone)
