SUPPORTED_TEMPERATURE_UNITS = ['Celsius', 'Fahrenheit', 'Kelvin']
KELVIN_CONSTANT = 273.15
charging_temperature_unit = 'Celsius'


def set_charging_temperature_unit(temperature_unit):
    if temperature_unit not in SUPPORTED_TEMPERATURE_UNITS:
        print('\n ALERT!!! Charging temperature in', temperature_unit, ' is not supported!!!',
              'Proceeding with default Celsius Unit')
        global charging_temperature_unit
        charging_temperature_unit = 'Celsius'
    else:
        charging_temperature_unit = temperature_unit


def perform_temperature_conversion_to_celsius(charging_temperature):
    if charging_temperature_unit is 'Kelvin':
        return charging_temperature - KELVIN_CONSTANT
    else:
        return (charging_temperature - 32) * (5 / 9)


def perform_temperature_processing(temperature_unit, charging_temperature):
    set_charging_temperature_unit(temperature_unit)
    if charging_temperature_unit is not 'Celsius':
        return perform_temperature_conversion_to_celsius(charging_temperature)
    else:
        return charging_temperature
