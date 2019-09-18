

import allure
class TestJen:
    @allure.step("测试步骤登录")
    def test_001(self):
        allure.attach("用户名","13344440000")
        assert True