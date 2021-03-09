normal_status = "\n Battery Health is Good. No breach occurred"

low_alert = "\n Battery Breach Alert \n Severity_level : Low \n BMS detected abnormal condition,"\
            "Notified the authorized personnel \n Abnormal readings obtained for parameter:\t "

critical_alert = "\n Battery Breach Critical Alert \n Severity_level : High \n BMS detected abnormal condition, " \
                 "Please unplug the charger immediately \n Abnormal readings obtained for parameter:\t "

normaler_status = " \n Batteriezustand ist gut. Es ist kein Verstoß aufgetreten "

niedrige_alarmstufe = "\n Batteriebruchwarnung \n Schweregrad : niedrig \n BMS hat einen abnormalen Zustand " \
                      "festgestellt. Das autorisierte Personal benachrichtigt \n Abnormale Messwerte für Parameter:\t "

kritischer_alarm = "\n Kritischer Alarm bei Batteriebruch \n Schweregrad : hoch \n BMS hat abnormale Zustände " \
                   "festgestellt. Bitte ziehen Sie sofort den Netzstecker aus der Steckdose \n " \
                    "Abnormale Messwerte für Parameter:\t "

battery_health_status_message = {'English': {'normal': normal_status, 'low': low_alert, 'high': critical_alert},
                                 'German': {'normal': normaler_status, 'low': niedrige_alarmstufe, 'high': kritischer_alarm}}
