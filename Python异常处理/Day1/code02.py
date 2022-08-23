class TestError(Exception):
    def __init__(self,msg,code=0):
        super().__init__(msg)
        self.code = code



raise TestError("1234")