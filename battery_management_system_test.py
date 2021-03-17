import check_battery_limits as checker
import bms_temperature_handler as temp

if __name__ == '__main__':
    """ battery Health Language Based Tests"""
    """ Test Function: is_battery_overall_health_ok for German"""
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 25, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "English", "Celsius") is True)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "German", 'Celsius') is False)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 25, 'state_of_charge': 470,
                                                  'charge_rate': 0.8}, "German", 'Celsius') is False)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 25, 'state_of_charge': 70,
                                                  'charge_rate': 6.8}, "German", 'Celsius') is False)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 170,
                                                  'charge_rate': 0.8}, "German", 'Celsius') is False)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 170,
                                                  'charge_rate': 1.8}, "German", 'Celsius') is False)

    """ Test Function: is_battery_overall_health_ok English"""
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 25, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "English", 'Celsius') is True)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "English", 'Celsius') is False)


    """ Test Function: is_battery_overall_health_ok to print in English for non-supported languages"""

    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 170,
                                                  'charge_rate': 1.8}, "hebrew", 'Celsius') is False)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 170,
                                                  'charge_rate': 1.8}, "Latin", 'Celsius') is False)

    """ Test Function: is_battery_overall_health_ok for different charging temperature Units"""
    """ Charging Temperature in Fahrenheit"""
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 77, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "German", "Fahrenheit") is True)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 257, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "English", 'Fahrenheit') is False)
    """ Charging Temperature in Kelvin"""
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 298.15, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "English", "Kelvin") is True)
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 398.15, 'state_of_charge': 170,
                                                  'charge_rate': 0.8}, "German", 'Kelvin') is False)

    """ Charging Temperature for unsupported temperature units"""
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 25, 'state_of_charge': 70,
                                                  'charge_rate': 0.8}, "English", "Rankine") is True)

    """ Test Function: perform_temperature_processing """
    assert (temp.perform_temperature_processing('Rankine', 25) == 25)
    assert (temp.perform_temperature_processing('Fahrenheit', 158) == 70)
    assert (temp.perform_temperature_processing('Kelvin', 401.15) == 128)
