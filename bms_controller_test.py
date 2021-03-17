import check_battery_limits as checker


if __name__ == '__main__':

    'Test for upper limit breaches'
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': 90,
                                                  'charge_rate': 6.8}, "English", 'Celsius') is False)
    'Test for lower limit breaches'
    assert (checker.is_battery_overall_health_ok({'charging_temperature': -125, 'state_of_charge': -170,
                                                  'charge_rate': -0.8}, "English", 'Celsius') is False)
    'Test for upper & lower limit breaches'
    assert (checker.is_battery_overall_health_ok({'charging_temperature': 125, 'state_of_charge': -20,
                                                  'charge_rate': 0.8}, "English", 'Celsius') is False)
