import bms_reporter
import bms_temperature_handler as temp

battery_parameters_normal_range = {'charging_temperature': {'min': 0, 'max': 45},
                                   'state_of_charge': {'min': 20, 'max': 80},
                                   'charge_rate': {'min': 0, 'max': 0.8}}


def check_is_battery_parameter_out_of_range(out_of_range_parameters, parameter_name, parameter_value,
                                            parameter_normal_range):
    if parameter_value < parameter_normal_range['min'] or parameter_value > parameter_normal_range['max']:
        out_of_range_parameters.append(parameter_name)


def collect_out_of_range_battery_parameters(battery_health_parameters):
    out_of_range_parameters = []
    for battery_parameter in battery_health_parameters:
        check_is_battery_parameter_out_of_range(out_of_range_parameters, battery_parameter,
                                                battery_health_parameters[battery_parameter],
                                                battery_parameters_normal_range[battery_parameter])
    return out_of_range_parameters


def is_battery_overall_health_ok(battery_health_parameters, selected_language, temperature_unit):
    battery_status_normal = True
    bms_language = bms_reporter.set_bms_language(selected_language)
    battery_health_parameters['charging_temperature'] = temp.perform_temperature_processing(temperature_unit,
                                                                                            battery_health_parameters[
                                                                                                'charging_temperature'])
    out_of_range_battery_parameters = collect_out_of_range_battery_parameters(battery_health_parameters)
    if len(out_of_range_battery_parameters) != 0:
        battery_status_normal = False
        bms_reporter.report_consolidated_battery_breach_status(out_of_range_battery_parameters,bms_language)
    else:
        bms_reporter.report_normal_health_status(bms_language)
    return battery_status_normal
