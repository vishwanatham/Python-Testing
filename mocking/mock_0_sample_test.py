from unittest import mock


class MockSample:

    def func1(self):
        # some line 1
        # some line 2
        # .......
        # some line n
        return "hello"

    def func2(self):
        return len(self.func1())


def test_func2():
    f1 = mock.Mock()
    f1.return_value = "xyz"
    ms = MockSample()
    ms.func1 = f1
    assert 3 == ms.func2()
