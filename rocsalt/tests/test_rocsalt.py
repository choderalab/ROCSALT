"""
Unit and regression test for the rocsalt package.
"""

# Import package, test suite, and other packages as needed
import rocsalt
import pytest
import sys

def test_rocsalt_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "rocsalt" in sys.modules
