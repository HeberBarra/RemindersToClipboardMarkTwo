from Reminders import show_reminders
from GenericUtils.generic_utils import InputUtils, ReadWriteUtils
from Dates.get_dates import GetDates


read_write_json = ReadWriteUtils()
show = show_reminders.ShowReminders()
input_utilities = InputUtils()
date_utilities = GetDates()

CONFIG_FILE = read_write_json.read_json_file('src/config.json')
PROGRAM_LANGUAGE = CONFIG_FILE['language']
REMINDERS_FILE_PATH = CONFIG_FILE['reminders_file']
MESSAGES = {
    'PT': [
        # Deletar
        'Deletamento de lembrete:',
        # Id do lembrete,
        'Qual o id do lembrete? \n> ',
        # Index da seção
        'Qual o index da seção? \n> ',
        # Confirmação
        'Seção não está vazia. Remover forçadamente? \n[0] Não \n[1] Sim \n> '
    ],
    'EN': [
        # Delete
        'Reminder deletion: ',
        # Reminder id
        'What\'s the reminder id? \n> ',
        # Section index
        'What\'s the section index? \n> ',
        # Confirmation
        'Section is not empty. Forcefully remove? \n[0] No \n[1] Yes \n> '
    ]
}


class DeleteReminder:

    def select_reminder_to_delete(self, file: list[dict]):
        print(MESSAGES[PROGRAM_LANGUAGE][0])
        section_index = show.show_section(file)
        reminder_id = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][1])
        file[section_index]['reminders'].pop(reminder_id)
        read_write_json.write_to_json_file(REMINDERS_FILE_PATH, file)

    def outdated_reminders(self, file: list[dict]):
        today_date = date_utilities.get_today_date()

        for section in file:
            for index, reminder in enumerate(section['reminders']):
                if date_utilities.get_date_from_string(reminder['last_date']) < today_date:
                    section['reminders'].pop(index)

        read_write_json.write_to_json_file(REMINDERS_FILE_PATH, file)

    def delete_section(self, file: list[dict]):
        show.show_all_sections(file)
        section_index = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][2], len(file) - 1)
        
        if len(file[section_index]['reminders']) != 0:
            force = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][3], 1)

        if len(file[section_index]['reminders']) == 0 or force == 1:
            file.pop(section_index)
        
        show.show_all_sections(file)
        read_write_json.write_to_json_file(REMINDERS_FILE_PATH, file)
