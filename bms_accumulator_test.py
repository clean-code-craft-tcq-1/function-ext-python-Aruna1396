import check_battery_limits as checker

" Test Function: collect_out_of_range_battery_parameters accumulator"

if __name__ == '__main__':

    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': 25, 'state_of_charge': 170,
                                                             'charge_rate': 1.8}) == (['state_of_charge', 'charge_rate'], ['upper', 'upper']))
    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': 25, 'state_of_charge': 170,
                                                             'charge_rate': 0.8}) == (['state_of_charge'], ['upper']))
    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': -5, 'state_of_charge': 70,
                                                             'charge_rate': 0.8}) == (['charging_temperature'], ['lower']))
    assert (checker.collect_out_of_range_battery_parameters({'charging_temperature': -5, 'state_of_charge': 10,
                                                             'charge_rate': 1.8}) == (['charging_temperature',
                                                                                      'state_of_charge', 'charge_rate'], ['lower', 'lower', 'upper']))
    """SubFunctionality Tests"""
    """ Test Function: check_is_battery_parameter_out_of_range """
    out_of_range_parameters = []
    breach_limit = []
    checker.check_is_battery_parameter_out_of_range(out_of_range_parameters, breach_limit, 'charging_temperature', 125,
                                                    checker.battery_parameters_normal_range['charging_temperature'])
    assert ((out_of_range_parameters, breach_limit) == (['charging_temperature'], ['upper']))
    out_of_range_parameters = []
    breach_limit = []
    checker.check_is_battery_parameter_out_of_range(out_of_range_parameters, breach_limit, 'charge_rate', 9.8,
                                                    checker.battery_parameters_normal_range['charge_rate'])
    assert ((out_of_range_parameters, breach_limit) == (['charge_rate'], ['upper']))
