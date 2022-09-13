## cookies操作

cookies 是识别用户登录与否的关键，爬虫中常常使用 selenium + requests 实现 cookie持久化，即先用 selenium 模拟登陆获取 cookie ，再通过 requests 携带 cookie 进行请求。

webdriver 提供 cookies 的几种操作：读取、添加删除。

- get_cookies：以字典的形式返回当前会话中可见的 cookie 信息。
- get_cookie(name)：返回 cookie 字典中 key == name 的 cookie 信息。
- add_cookie(cookie_dict)：将 cookie 添加到当前会话中
- delete_cookie(name)：删除指定名称的单个 cookie。
- delete_all_cookies()：删除会话范围内的所有 cookie。

下面看一下简单的示例，演示了它们的用法。

```python
from selenium import webdriver 

driver = webdriver.Chrome()
driver.get("https://blog.csdn.net/")

# 输出所有cookie信息
print(driver.get_cookies())

cookie_dict = {
    'domain': '.csdn.net',
     'expiry': 1664765502,
     'httpOnly': False,
     'name': 'test',
     'path': '/',
     'secure': True,
     'value': 'null'}

# 添加cookie
driver.add_cookie(cookie_dict)
# 显示 name = 'test' 的cookie信息
print(driver.get_cookie('test'))
# 删除 name = 'test' 的cookie信息
driver.delete_cookie('test')
# 删除当前会话中的所有cookie
driver.delete_all_cookies()
```

<img src='https://img-blog.csdnimg.cn/bfc879ed759a41ed8fe86a6444976972.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBARHJlYW3kuLZLaWxsZXI=,size_20,color_FFFFFF,t_70,g_se,x_16'>

<img src='https://img-blog.csdnimg.cn/550183ae5dbb4e89ba5211386346874e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBARHJlYW3kuLZLaWxsZXI=,size_19,color_FFFFFF,t_70,g_se,x_16'>

### **localStorage**

```python
class LocalStorage:

    def __init__(self, driver):
        self.driver = driver

    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self):
        return self.driver.execute_script( \
            "var ls = window.localStorage, items = {}; " \
            "for (var i = 0, k; i < ls.length; ++i) " \
            "  items[k = ls.key(i)] = ls.getItem(k); " \
            "return items; ")

    def keys(self):
        return self.driver.execute_script( \
            "var ls = window.localStorage, keys = []; " \
            "for (var i = 0; i < ls.length; ++i) " \
            "  keys[i] = ls.key(i); " \
            "return keys; ")

    def get(self, key):
        return self.driver.execute_script("return 		window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        return key in self.keys()

    def remove(self, key):
        self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()


```

