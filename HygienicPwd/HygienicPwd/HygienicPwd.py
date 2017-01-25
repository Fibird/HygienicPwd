import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'HygienicPwd.xaml')
    
    def generate_Click(self, sender, e):
        pass
class Pwd:
    def Save():
        pass


if __name__ == '__main__':
    Application().Run(MyWindow())
