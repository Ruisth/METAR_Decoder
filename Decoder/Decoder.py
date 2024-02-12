class Decoder:

    def decode_metar(self, metar):
        decoded_metar = {}

        # Split METAR string into individual components
        components = metar.split()

        # Extracting basic information
        decoded_metar['station'] = components[0]
        decoded_metar['time'] = components[1]
        decoded_metar['wind_direction'] = components[3]
        decoded_metar['wind_speed'] = components[4]
        decoded_metar['visibility'] = components[5]
        decoded_metar['weather'] = components[6]

        # If present, extract temperature and dew point
        if 'M' in components[7] or 'M' in components[8]:
            temperature_index = 7
            decoded_metar['temperature'] = components[7]
            decoded_metar['dew_point'] = components[8]
        else:
            temperature_index = 8
            decoded_metar['temperature'] = components[8]
            decoded_metar['dew_point'] = components[9]

        # Convert wind direction and speed to more readable format
        decoded_metar['wind_direction'] = decoded_metar['wind_direction'] + ' degrees'
        decoded_metar['wind_speed'] = decoded_metar['wind_speed'] + ' knots'

        # Convert visibility to more readable format
        if decoded_metar['visibility'].startswith('M'):
            decoded_metar['visibility'] = 'Less than ' + decoded_metar['visibility'][1:] + ' meters'
        else:
            decoded_metar['visibility'] = decoded_metar['visibility'] + ' meters'

        return decoded_metar


# Example usage:
if __name__ == '__main__':
    decoder = Decoder()
    metar_string = input("Insert METAR: ")
    string = metar_string
    decoded_metar = decoder.decode_metar(string)
    print(decoded_metar)
