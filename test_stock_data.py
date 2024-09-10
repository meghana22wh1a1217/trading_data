import unittest
import pandas as pd
import numpy as np
from datetime import datetime

class TestStockData(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.data = {
            'datetime': [datetime(2024, 9, 1), datetime(2024, 9, 2)],
            'open': [100.5, 101.0],
            'high': [102.0, 102.5],
            'low': [99.5, 100.0],
            'close': [101.5, 101.8],
            'volume': [1000, 1500],
            'instrument': ['AAPL', 'AAPL']
        }
        self.df = pd.DataFrame(self.data)

    def test_datetime(self):
        """ Test if 'datetime' column contains datetime objects """
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df['datetime']))

    def test_open_high_low_close(self):
        """ Test if 'open', 'high', 'low', 'close' columns contain float values """
        for column in ['open', 'high', 'low', 'close']:
            self.assertTrue(pd.api.types.is_float_dtype(self.df[column]))

    def test_volume(self):
        """ Test if 'volume' column contains integer values """
        self.assertTrue(pd.api.types.is_integer_dtype(self.df['volume']))

    def test_instrument(self):
        """ Test if 'instrument' column contains string values """
        self.assertTrue(pd.api.types.is_string_dtype(self.df['instrument']))

if __name__ == '__main__':
    unittest.main()
