
from pydantic import HttpUrl, ValidationError


def isJenkinsUrlFieldGood(urlField: str, timeout: int = 5) -> bool:
    print(str(urlField))

    try:
        HttpUrl(urlField)
        return True
    except ValidationError:
        #print(traceback.format_exc())
        return False    

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
        status =  True    
    else:
        status =  False

    return status


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

