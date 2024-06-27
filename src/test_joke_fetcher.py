from joke_fetcher import should_fetch_joke


def test_should_fetch_joke_within_duration():
    assert should_fetch_joke(10, 0, 0, None, 0) is True
    assert should_fetch_joke(10, 5, 0, None, 0) is True
    assert should_fetch_joke(10, 11, 0, None, 0) is False


def test_should_fetch_joke_within_count():
    assert should_fetch_joke(0, 0, 0, 5, 0) is True
    assert should_fetch_joke(0, 0, 0, 5, 3) is True
    assert should_fetch_joke(0, 0, 0, 5, 5) is False

    # If duration and total are both set, the function should ignore duration
    assert should_fetch_joke(10, 0, 0, 5, 0) is True
    assert should_fetch_joke(10, 0, 0, 5, 3) is True
    assert should_fetch_joke(10, 0, 0, 5, 5) is False
