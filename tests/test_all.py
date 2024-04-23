from importlib_resources import files

import jaraco.docker


def test_mountinfo():
    info_file = files().joinpath('mountinfo')
    assert jaraco.docker.text_in_file('docker|overlay', info_file)
