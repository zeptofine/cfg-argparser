import unittest

from cfg_argparser import wrap_config, CfgDict


def basic_function(s: str, num: int, is_real: bool):
    """a basic function to test the wrapper with"""
    return f"{s} x {num} x {is_real}"

class WrappingTest(unittest.TestCase):
    def test_base(self):
        self.assertEqual(basic_function("you", 3, True), "you x 3 x True")

    def test_basic_cfg(self):
        cfg = CfgDict("test.json")
        cfg.update({"s": "you", "num": 3, "is_real": True})
        new_func = wrap_config(cfg)(basic_function)
        self.assertEqual(new_func(), "you x 3 x True")

    def test_loading(self):
        cfg: CfgDict = CfgDict("test.json").update({"s": "you", "num": 3, "is_real": False}).save().load()
        new_func = wrap_config(cfg)(basic_function)
        self.assertEqual(new_func(), "you x 3 x False")