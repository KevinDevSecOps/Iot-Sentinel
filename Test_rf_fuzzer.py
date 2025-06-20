import unittest
from unittest.mock import patch
from iot_sentinel.core.rf_fuzzer import HackRFFuzzer, RFProtocol

class TestHackRFFuzzer(unittest.TestCase):
    @patch("subprocess.run")
    def test_fuzz_single(self, mock_run):
        fuzzer = HackRFFuzzer()
        result = fuzzer.fuzz_single("433M", RFProtocol.OOK)
        self.assertIsInstance(result, FuzzingResult)

    def test_invalid_frequency(self):
        fuzzer = HackRFFuzzer()
        with self.assertRaises(ValueError):
            fuzzer.fuzz_single("999X", RFProtocol.OOK)

if __name__ == "__main__":
    unittest.main()
