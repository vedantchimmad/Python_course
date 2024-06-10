
class Dept():
    def __init__(self):
        self.depts={"hr":"Human resource department",
                   "acc":"Account department",
                   "sd":"sales and market department",
                   "mf":"manufactring department"}

    def __call__(self, dept):
        return self.depts[dept]

a=Dept()
b=a("hr")
print(b)