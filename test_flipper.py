import unittest
from unittest.mock import MagicMock, patch
from iot_sentinel.core.flipper import FlipperNFC, NFCTag

class TestFlipperNFC(unittest.TestCase):
    @patch("serial.Serial")
    def test_scan_tag(self, mock_serial):
        mock_serial.return_value.read_until.return_value = b"UID: DEADBEEF\nDone"
        flipper = FlipperNFC()
        result = flipper.scan_tag()
        self.assertEqual(result.uid, "DEADBEEF")

if __name__ == "__main__":
    unittest.main()
