@patch("iot_sentinel.core.rf_fuzzer.HackRFFuzzer.fuzz_single")
def test_fuzz_range(self, mock_fuzz):
    mock_fuzz.return_value = FuzzingResult("433M", RFProtocol.OOK, True)
    fuzzer = HackRFFuzzer(min_freq="300M", max_freq="500M")
    results = fuzzer.fuzz_range(RFProtocol.OOK, step="100M")
    self.assertTrue(any(r.is_vulnerable for r in results))
