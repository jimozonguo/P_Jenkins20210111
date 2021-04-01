#案例：研究pytest框架中的setup_class、teardown_class！
#1.某测试类中只允许一份！
#2.不管测试类中有个N个测试函数，这两个函数都只会运行一次！
#3.setup_class/普通测试函数/teardown_class的执行顺序！


class TestLogin:
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_01(self):
        print("test01")

    def test_02(self):
        print("test02")

