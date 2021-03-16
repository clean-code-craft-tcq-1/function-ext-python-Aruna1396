import bms_alert_definitions as constant

SUPPORTED_LANGUAGES = ['English', 'German']


def set_bms_language(selected_language):
    if selected_language not in SUPPORTED_LANGUAGES:
        print('\n ALERT!!! Report is not available in', selected_language, '!!!', 'Switching to Default Language')
        bms_language = "English"
    else:
        bms_language = selected_language
    return bms_language


def report_normal_health_status(bms_language):

    print(constant.battery_health_status_message[bms_language]['normal'])


def report_consolidated_battery_breach_status(out_of_range_battery_parameters, bms_language):
    if len(out_of_range_battery_parameters) >= 2:
        print(constant.battery_health_status_message[bms_language]['high'], ', '.join(out_of_range_battery_parameters))
    else:
        print(constant.battery_health_status_message[bms_language]['low'], ', '.join(out_of_range_battery_parameters))
