"Tests for utility functions"""

import unittest
import logging

from __future__ import annotations

from cerise.utils import nanojanskyToABMagnitude

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.level = logging.DEBUG


class TestModel(unittest.TestCase):

    def test_nanoJanskyToABMagnitude(self) -> None:
        """Check that proper value is returned."""
        multiplier = 11
        value = 10
        expected_result = 110
        logger.debug(f'Multiplier is {multiplier}, value is {value}')
        result = nanojanskyToABMagnitude(value, multiplier=multiplier)
        self.assertTrue(result, expected_result)

    def test_nanoJanskyToABMagnitude_input_error(self) -> None:
        """Test that error handling raises an error when a string is declared."""
        value = '10'  # strings are not supported
        with self.assertRaises(IOError):
            nanojanskyToABMagnitude(value)
