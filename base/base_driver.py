#fileName:base_driver.py
from appium import webdriver
#函数功能：封装了前置代码，并返回driver对象
def init_driver():
    # server 启动参数开始
    desired_caps = {}  # 定义一个字典变量
    # 平台的名称,不区分大小写的，即"android""Android""andROID"都是OK的！
    desired_caps['platformName'] = 'Android'  # 如果是ios平台，这里写"ios"即可
    # 手机中安卓系统的版本号，可在“设置”app中的“关于手机”UI中看到或用adb命令查看
    desired_caps['platformVersion'] = '5.1'
    # 设备名。如果是安卓平台，随便写，但是不能是空字符串！如果是IOS平台，必须正确写设备名！ 可用adb命令"adb devices"获取！
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # 指定需要运行的app的包名，app的包名就能代表这个app！可通过adb命令获取！
    desired_caps['appPackage'] = 'com.android.contacts'  # 这里打开"设置"app！
    # 指定该app的UI页，即指定需要打开的页面。可通过adb命令获取
    desired_caps['appActivity'] = '.activities.PeopleActivity'  # 这里是“设置”app的主页UI
    # 下面两行：解决无法输入中文的问题
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明driver对象，可以把driver理解为“手机”！
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
