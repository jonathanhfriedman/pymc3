from __future__ import division

from .helpers import SeededTest


class TestClassThatShouldFail(SeededTest):
    def test_that_should_fail(self):
        assert 0
        for i in [1/0]:
            assert 0
            yield self.failing_check
        assert 0

    def failing_check(self):
        assert 0
