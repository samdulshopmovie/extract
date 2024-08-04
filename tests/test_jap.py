from extract.jap import echo, ice_breaking

def test_echo():
    msg = "ABCdef"
    r = echo(msg)
    assert r == msg
