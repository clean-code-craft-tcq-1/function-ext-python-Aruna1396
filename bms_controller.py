controller_actions = {
    'charging_temperature': {'lower': 'Battery Warming System Activated', 'upper': 'Battery Cooling System Activated'},
    'state_of_charge': {'lower': 'Stopping Charging: Low Battery', 'upper': 'Stopping Charging: Battery Almost Full'},
    'charge_rate': {'lower': 'Stopping Charging: Charge rate low', 'upper': 'Stopping Charging: Charge rate high'}}


def controller_normal_action():
    print(' Start Charging: Battery Health is normal ')


def print_heading(message):
    print(' \n *************', message, '***************')


def execute_control_measures(out_of_range_battery_parameters, breach_limit):
    print_heading('Controller Operation Start')
    for i in range(len(out_of_range_battery_parameters)):
        print(controller_actions[out_of_range_battery_parameters[i]][breach_limit[i]])
    print_heading('Controller Operation END')
