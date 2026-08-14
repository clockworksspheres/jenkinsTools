import traceback
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse

from pydantic import HttpUrl, ValidationError

#from django.core.validators import URLValidator
#from django.core.exceptions import ValidationError
#from django.conf import settings

def isJenkinsUrlFieldGood(urlField: str, timeout: int = 5) -> bool:
    print(str(urlField))

    try:
        HttpUrl(urlField)
        return True
    except ValidationError:
        return False

""" no good for http://localhost:8080
    if not settings.configured:
        settings.configure(
            USE_I18N=False,          # or False
            USE_L10N=False,
            USE_TZ=True,
            # add anything else you need
    )
    ####
    # Check for a valid URL using the dango.core library
    validator = URLValidator(schemes=["http", "https"])
    try:
        validator(urlField)
        print(f"URL field '{urlField}' ok...")
    except ValidationError as e:
        print(f"URL field '{urlField}' exception...")
        print(f"FAIL: {urlField} -> {e}")
        print(traceback.format_exc())
        return False
    except Exception as e:
        print(f"URL field '{urlField}' exception...")
        print(f"FAIL: {urlField} -> {e}")
        print(traceback.format_exc())
        return False
 
    ####
    # Check if the url is available
    try:
        # Send a HEAD request to check connectivity
        response = requests.head(urlField, timeout=timeout)
    except requests.exceptions.ConnectionError:
        return False
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.RequestException:
        return False    
    else:
        # Check if status code is 2xx or 3xx (successful or redirect)
        return response.status_code < 400
    """
    

def isJenkinsUsernameFieldGood(usernameField: str) -> bool:
    print(str(usernameField))
    # create an allowed set of characters
    allowed_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    # if each of the characters is in the allowed set
    return set(usernameField).issubset(allowed_set)

def isJenkinsTokenFieldGood(tokenField: str) -> bool:
    print(str(tokenField))
    # create an allowed set of characters
    allowed_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    # if each of the characters is in the allowed set
    if set(tokenField).issubset(allowed_set):
        return True    
        ####
        # remove the above return if you want to check if the token is valid with the server
        try:
            # The /whoAmI/ endpoint is lightweight and confirms auth status
            response = requests.get(
                f"{url}/whoAmI/", 
                auth=HTTPBasicAuth(username, token),
                timeout=5
            )
        except requests.exceptions.RequestException:
            return False
        else:
            # 200 OK means the token is valid
            return response.status_code == 200
    else:
        return False


if __name__=="__main__":
    urls = [ "https://google", "https://scholar.google",
             "https://scholar.google.com", "gttp://scholar.google.com",
             "not ; a url", "; /bin/bash", "http://google.com ; /bin/bash",
             "http://google.com;/bin/bash", "http://google.com|/bin/bash",
             "http://google.com| /bin/bash", "http://github.com/2>&1>filename",
             ";/bin/bash", "http://github.com/1|12341223", "http://google.com/a:23523446",
             "http://localhost:65521/", "http://localhost:8080", "http://127.0.0.1:8080"]

    for url in urls:
        print(isJenkinsUrlFieldGood(f"{url}"))

    print("=" * 10)

    tokens = ["123afg", "3*&32rhz", "|[]&", "bash", ";bash"]

    for token in tokens:
        print(isJenkinsTokenFieldGood(f"{token}"))

    print("=" * 10)

    usernames = ["admin", "sarah", "connor", "123afg", "3*&32rhz", "|[]&", "bash", ";bash"]

    for username in usernames:
        print(isJenkinsUsernameFieldGood(f"{username}"))

