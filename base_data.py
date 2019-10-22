from faker import Faker
class get_data():
    fake = Faker(locale='zh_CN')
    def get_num(self,m,n):
        return self.fake.random_int(min=m,max=n)
    def get_string(self):
        return self.fake.sentence()[:-1]
    def get_address(self):
        return self.fake.province()+'-'+self.fake.city()
    def get_datetime(self):
        return self.fake.future_datetime()
    def get_name(self):
        return self.fake.name()