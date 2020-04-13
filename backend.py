from requests import get, exceptions

class Grabber:

    __url = "http://danix43.go.ro:8080/api/termometru"

    def __init__(self):
        self._headers = {'Accept': "application/json"}
        self._timeout = 10
        self.content = {}

    def send_request(self, name=None, id=None):
        if name is not None:
            response = get(
                self.__url, 
                params={"name": name}, 
                headers=self._headers, 
                timeout=self._timeout)
        elif id is not None:
            url_id = self.__url + "/{}/status".format(id)
 
            response = get(
                url_id,
                headers = self._headers,
                timeout=self._timeout)
        else:
            print("Invalid arguments have been provided")

        try:        
            response.raise_for_status()
        except exceptions.HTTPError:
            print("Something went wrong")

        self.content = response.json()
        print("Got something:\n{}".format(self.content))


if __name__ == "__main__":
    grabber = Grabber()
    grabber.send_request(name="Adam01")
    print(grabber.content["name"])
