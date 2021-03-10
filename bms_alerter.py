import bms_alert_definitions as constant

BMS_language = "English"
SUPPORTED_LANGUAGES = ['English', 'German']


def set_language_for_report_and_alerts(selected_language):
    global BMS_language
    if selected_language not in SUPPORTED_LANGUAGES:
        print('\n ALERT!!! Report is not available in', selected_language, '!!!', 'Switching to Default Language')
    else:
        BMS_language = selected_language


def report_normal_health_status():

    print(constant.battery_health_status_message[BMS_language]['normal'])


def report_severity_of_battery_health_breach(out_of_range_battery_parameters):
    if len(out_of_range_battery_parameters) >= 2:
        print(constant.battery_health_status_message[BMS_language]['high'], ', '.join(out_of_range_battery_parameters))
    else:
        print(constant.battery_health_status_message[BMS_language]['low'], ', '.join(out_of_range_battery_parameters))
