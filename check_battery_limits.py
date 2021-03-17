import bms_reporter
import bms_temperature_handler as temp
import bms_controller

battery_parameters_normal_range = {'charging_temperature': {'min': 0, 'max': 45},
                                   'state_of_charge': {'min': 20, 'max': 80},
                                   'charge_rate': {'min': 0, 'max': 0.8}}


def check_is_battery_parameter_out_of_range(out_of_range_parameters, breach_limit, parameter_name, parameter_value,
                                            parameter_normal_range):
    if parameter_value < parameter_normal_range['min']:
        out_of_range_parameters.append(parameter_name)
        breach_limit.append('lower')
    elif parameter_value > parameter_normal_range['max']:
        out_of_range_parameters.append(parameter_name)
        breach_limit.append('upper')


def collect_out_of_range_battery_parameters(battery_health_parameters):
    out_of_range_parameters = []
    breach_limit = []
    for battery_parameter in battery_health_parameters:
        check_is_battery_parameter_out_of_range(out_of_range_parameters, breach_limit, battery_parameter,
                                                battery_health_parameters[battery_parameter],
                                                battery_parameters_normal_range[battery_parameter])
    return out_of_range_parameters, breach_limit


def is_battery_overall_health_ok(battery_health_parameters, selected_language, temperature_unit):
    battery_status_normal = True
    bms_language = bms_reporter.set_bms_language(selected_language)
    battery_health_parameters['charging_temperature'] = temp.perform_temperature_processing(temperature_unit,
                                                                                            battery_health_parameters[
                                                                                                'charging_temperature'])
    out_of_range_battery_parameters, breach_limit = collect_out_of_range_battery_parameters(battery_health_parameters)

    if len(out_of_range_battery_parameters) != 0:
        battery_status_normal = False
        bms_reporter.report_consolidated_battery_breach_status(out_of_range_battery_parameters, bms_language)
        bms_controller.execute_control_measures(out_of_range_battery_parameters, breach_limit)
    else:
        bms_reporter.report_normal_health_status(bms_language)
        bms_controller.controller_normal_action()
    return battery_status_normal
