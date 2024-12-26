import requests

def test_homepage():
    url = "http://localhost:82"  # Ensure the port matches your running Docker container
    expected_title = "<title>WebSocket Chat</title>"  # The specific part of HTML to check

    try:
        # Send a GET request to the server
        response = requests.get(url)
        response_content = response.text.strip()

        if response.status_code == 200:
            print("Server Response:")
            print(response_content[:500])  # Print the first 500 characters for debugging

            # Check if the title exists in the response content
            if expected_title in response_content:
                print("Test passed: Title matches!")
            else:
                print("Test failed: Title does not match.")
        else:
            print(f"Test failed: Status code {response.status_code}")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_homepage()
