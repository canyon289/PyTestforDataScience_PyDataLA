import bill_split

# pytest autodiscovers tests through module, class, function names
# https://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/naming_conventions.html


def test_bill_splitting():
    """Test that bill splitting works"""
    bill_cost = 5
    split = bill_split.split_bill(bill_cost)

    # Check result with assert statement and conditional
    assert split == 2.5
