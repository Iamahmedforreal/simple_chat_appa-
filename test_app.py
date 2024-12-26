import requests

def test_hompage():
    response = requests.get('http://localhost:8081/')
    assert response.status_code == 200 , "Homepage is not loading properly"
    print("Homepage is loading properly")


if __name__ == '__main__':
    test_hompage()