from Dates import get_dates
from GenericUtils import generic_utils
from Reminders import show_reminders

input_utilities = generic_utils.InputUtils()
read_write_utilities = generic_utils.ReadWriteUtils()
show = show_reminders.ShowReminders()

CONFIG_FILE = read_write_utilities.read_json_file('src/config.json')
REMINDERS_FILE_PATH = CONFIG_FILE['reminders_file']
PROGRAM_LANGUAGE = CONFIG_FILE['language']
MESSAGES = {
    "PT": [
        # Messagem do lembrete
        'Qual é a messagem do lembrete? \n> ',
        # Seção do lembrete
        'Em qual seção o lembrete deve ser guardado? \n> ',
        # Título da seção
        'Qual é o título da seção? \n> '
    ],
    "EN": [
        # Reminder message
        'What\'s the reminder\'s message? \n> ',
        # Reminder section
        'In which section should the reminder be stored? \n> ',
        # Section title
        'What\'s the section title? \n> '
    ]
}


class CreateReminder:

    def create_reminder(self, file) -> None:

        dates_functions = get_dates.GetDates()

        reminder_message = input_utilities.is_str_input_right(MESSAGES[PROGRAM_LANGUAGE][0])
        date_interval = dates_functions.get_first_and_last_date()
        show.show_all_reminders(file)
        show.show_all_sections(file)
        reminder_section = input_utilities.is_int_input_right(
            MESSAGES[PROGRAM_LANGUAGE][1],
            max_value=len(file) - 1
        )

        file[reminder_section]['reminders'].append({
            'first_date': date_interval[0],
            'last_date': date_interval[1],
            'message': reminder_message
        })

        show.show_all_reminders(file)
        read_write_utilities.write_to_json_file(REMINDERS_FILE_PATH, file)

    def create_section(self, file) -> None:
        section_title = input_utilities.is_str_input_right(MESSAGES[PROGRAM_LANGUAGE][2])
        file.append({'section_title': section_title, 'reminders': []})
        read_write_utilities.write_to_json_file(REMINDERS_FILE_PATH, file)
