from GenericUtils.generic_utils import InputUtils, ReadWriteUtils


input_utilities = InputUtils()
read_write_utilities = ReadWriteUtils()

PROGRAM_LANGUAGE = read_write_utilities.read_json_file('src/config.json')['language']
MESSAGES = {
    'PT': [
        # Título da seção
        'Título da seção: ',
        # Lembretes
        'Lembretes: ',
        # Primeira data do lembrete
        'Primeira data: ',
        # Última data do lembrete
        'Última data: ',
        # Mensagem do lembrete
        'Mensagem: ',
        # Index da seção
        'Qual o index da seção? \n> ',
        # Mensagem de erro #1
        'Seção inválida! Tente de novo!'
    ],
    'EN': [
        # Section title
        'Section title: ',
        # Reminders
        'Reminders: ',
        # Reminder first date
        'First date: ',
        # Reminder last date
        'Last date: ',
        # Reminder message
        'Message: ',
        # Section index
        'What\'s the section index? \n> ',
        # Error message #1
        'Invalid section! Try again!' 
    ]
}

class ShowReminders:

    def show_all_reminders(self, file: list[dict]):
        for section in file:
            print(f'{MESSAGES[PROGRAM_LANGUAGE][0]}{section["section_title"]}')
            print(MESSAGES[PROGRAM_LANGUAGE][1])
            for reminder in section['reminders']:
                print(f'\n{MESSAGES[PROGRAM_LANGUAGE][2]} {reminder["first_date"]}')
                print(f'{MESSAGES[PROGRAM_LANGUAGE][3]} {reminder["last_date"]}')
                print(f'{MESSAGES[PROGRAM_LANGUAGE][4]} {reminder["message"]}')

    def show_section(self, file: list[dict]):
        self.show_all_sections(file)
        section_index = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][5])
        while True:
            try:
                print(f'{MESSAGES[PROGRAM_LANGUAGE][0]} {file[section_index]["section_title"]}')
                print(MESSAGES[PROGRAM_LANGUAGE][1])
                for index, reminder in enumerate(file[section_index]['reminders']):
                    print(f'\nId: {index}')
                    print(f'{MESSAGES[PROGRAM_LANGUAGE][2]} {reminder["first_date"]}')
                    print(f'{MESSAGES[PROGRAM_LANGUAGE][3]} {reminder["last_date"]}')
                    print(f'{MESSAGES[PROGRAM_LANGUAGE][4]} {reminder["message"]}')

                return section_index
            except IndexError:
                print(MESSAGES[PROGRAM_LANGUAGE][6])

    def show_all_sections(self, file: list[dict]) -> None:
        for index, section in enumerate(file):
            print(f'[{index}] - {section["section_title"]}')
