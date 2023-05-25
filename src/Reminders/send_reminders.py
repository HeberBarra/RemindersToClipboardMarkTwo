from Dates.get_dates import GetDates


dates_utilities = GetDates()

class SendReminders:

    def create_reminders_list(self, file, date=None) -> list:
        if date is None:
            date = dates_utilities.get_today_date()
        
        reminders_list = []

        for index, section in enumerate(file):
            not_changed = True

            reminders_list.append({
                'section_title': section['section_title'],
                'reminders': []
            })

            for reminder in section['reminders']:
                first_date = dates_utilities.get_date_from_string(reminder['first_date'])
                last_date = dates_utilities.get_date_from_string(reminder['last_date'])
                if date >= first_date and date <= last_date:
                    not_changed = False
                    reminders_list[index]['reminders'].append(reminder['message'])

            if not_changed:
                reminders_list.pop()
        
        return reminders_list

    def paste_reminder_list(self, reminders: list) -> None:
        for section in reminders:
            if type(section) != dict:
                print(section)
                continue

            print(section['section_title'].upper() + ':')
            for reminder in section['reminders']:
                print(f'\n\t-> {reminder}')
