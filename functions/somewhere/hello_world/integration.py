import pytest
import requests


@pytest.mark.integration(method="GET", endpoint="/somewhere")
def test_hello_world_status_code_is_200():

    response = requests.get(url="")

    assert response.status_code == 200
