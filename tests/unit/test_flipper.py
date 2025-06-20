import unittest
from unittest.mock import MagicMock
from iot_sentinel.core.flipper import FlipperAudit, NFCTag

class TestFlipperAudit(unittest.TestCase):
    def setUp(self):
        self.flipper = FlipperAudit()
        self.flipper.port = MagicMock()

    def test_scan_nfc_vulnerable(self):
        self.flipper.port.read_until.return_value = b"UID: 00000000\nDone"
        tag = self.flipper.scan_nfc()
        self.assertTrue(tag.is_vulnerable)

if __name__ == "__main__":
    unittest.main()
