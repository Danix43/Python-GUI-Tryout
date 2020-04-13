import requests
import json


class DataHandler:

    def __init__(self):
        """ Need to think about this constructer"""
        self.__content = ""

    def send_request(self, name_of_target=None, id_of_target=None):
        """ sends the request to HerculesAPI and returns the response as a json"""
        if id_of_target is not None:
            response = requests.get(
                'http://danix43.go.ro:8080/termometru/{}/status'.format(id_of_target),
                headers={'Accept': 'application/json'},
                timeout=15
            )
        elif name_of_target is not None:
            response = requests.get(
                'http://danix43.go.ro:8080/termometru',
                params={'name': name_of_target},
                headers={'Accept': 'application/json'},
                timeout=15
            )
        else:
            raise Exception("Error when sending the request")
        
        if response:
            print("Got something:\n{}".format(response.json()))
        elif response.status_code == 404:
            print("The data requested may not be available")
            return
        elif response.status_code == 500:
            print("There is a problem with the server")
            return

        self.__content = response.json()

    def process_response(self, payload):
        """ process the response and returns an object """
        data = HerculesResponse(payload["name"], payload["location"], payload["lastInsert"]
                            , payload["temperatureInCelsius"], payload["heatIndexCelsius"]
                            , payload["temperatureInKelvin"], payload["heatIndexKelvin"]
                            , payload["temperatureInFahrenheit"], payload["heatIndexFahrenheit"]
                            , payload["humidity"])
        return data

class HerculesResponse:

    def __init__(self, name, location, lastInsert, temperatureInCelsius, heatIndexCelsius, temperatureInKelvin, heatIndexKelvin, temperatureInFahrenheit, heatIndexFahrenheit, humidity):
        self.name = name
        self.location = location
        self.last_insert = lastInsert
        self.temperature_in_celsius = temperatureInCelsius
        self.heat_index_celsius = heatIndexCelsius
        self.temperature_in_kelvin = temperatureInKelvin
        self.heat_index_kelvin = heatIndexKelvin
        self.temperature_in_fahrenheit = temperatureInFahrenheit
        self.heat_index_fahrenheit = heatIndexFahrenheit
        self.humidity = humidity

    def __str__(self):
        # return "Got termometru " + self.name + " at " + self.location + "\nLast updated at " + self.last_insert + "\n\tTemperature: " + self.temperature_in_celsius + " °C" + "\n\tHeat index: " + self.heat_index_celsius + "\n\tTemperature: " + self.temperature_in_kelvin + "K" + "\n\tHeat index: " + self.heat_index_kelvin + "\n\tTemperature: " + self.temperature_in_fahrenheit + " °F" + "\n\tHeat index: " + self.heat_index_fahrenheit + "\n\tRelative humidity: " + self.humidity + "%" 
        return """ Got termometru {0.name} at {0.location}
        Last updated at {0.last_insert}
            Temperature: {0.temperature_in_celsius:.2f} °C
            Heat index: {0.heat_index_celsius:.2f} °C
            Temperature: {0.temperature_in_kelvin:.2f}K
            Heat index: {0.heat_index_kelvin:.2f}K
            Temperature: {0.temperature_in_fahrenheit:.2f} °F
            Heat index: {0.heat_index_fahrenheit:.2f} °F
            Relative humidity: {0.humidity}% """.format(self)
           

if __name__ == "__main__":
    grabber = DataHandler()
    data = grabber.send_request(name_of_target="Adam01")
    print(grabber.process_response(data))
