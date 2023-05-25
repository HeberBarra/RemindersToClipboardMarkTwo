import datetime
from GenericUtils.generic_utils import ReadWriteUtils, InputUtils 

read_write_json= ReadWriteUtils()
input_utilities = InputUtils()

PROGRAM_LANGUAGE = read_write_json.read_json_file('src/config.json')['language']
MESSAGES = {
    'PT': [
        # Mensagem de erro #1
        'Formato de data inválido',
        # Escolha de formato
        'Escolha o formato de data desejado \n> ',
        # Mensagem de erro #2
        'Index selecionado fora do intervalo! Tente de novo!',
        # Mensagem de erro #3
        'Um formato de data inválido foi escolhido! Tente de novo!',
        # Data final do lembrete
        'Qual a data final do lembrete? \n> '
    ],
    'EN': [
        # Error message #1
        'Invalid date format',
        # Choose format
        'Choose the desired date format \n> ',
        # Error message #2
        'Select index is out of range! Try again!',
        # Error message #3
        'An invalid date format was chosen! Try again',
        # Reminder last date
        'What is the final date of the reminder? \n> '
    ]
}

class GetDates:

    # formatos de data permitidos
    allowed_formats: tuple[dict] = (
        {'format': '%Y/%m/%d', 'desc': 'YYYY/MM/DD'},
        {'format': '%Y-%m-%d', 'desc': 'YYYY-MM-DD'},
        {'format': '%d/%m/%Y', 'desc': 'DD/MM/YYYY'},
        {'format': '%d-%m-%Y', 'desc': 'DD-MM-YYYY'},
        {'format': '%d/%m/%y',  'desc': 'DD/MM/YY'},
        {'format': '%d-%m-%y', 'desc': 'DD-MM-YY'},
        {'format': '%m/%d/%Y', 'desc': 'MM/DD/YYYY'},
        {'format': '%m-%d-%Y', 'desc': 'MM-DD-YYYY'},
        {'format': '%m/%d/%y', 'desc': 'MM/DD/YY'},
        {'format': '%m-%d-%y', 'desc': 'MM-DD-YY'}
    )

    def get_today_date(self) -> datetime.date:
        return datetime.date.today()

    def get_date_string(self, date: datetime.date) -> str:
        return datetime.date.isoformat(date)

    def get_date_from_string(self, date_string: str, date_format: int = 1) -> datetime.date:

        try:
            return datetime.datetime.strptime(date_string, self.allowed_formats[date_format]['format']).date()

        except IndexError:
            raise Exception(MESSAGES[PROGRAM_LANGUAGE][0])

    def choose_date_format(self) -> int:
        for index, data in enumerate(self.allowed_formats):
            print(f'[{index}] - {data["desc"]}')

        while True:
            try:
                chosen_date_format = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][1])

                if chosen_date_format < len(self.allowed_formats):
                    return chosen_date_format

                print(MESSAGES[PROGRAM_LANGUAGE][2])

            except ValueError:
                print(MESSAGES[PROGRAM_LANGUAGE][3])

    def get_first_and_last_date(self):
        today_date_string = self.get_date_string(self.get_today_date())
        final_date = input_utilities.is_str_input_right(MESSAGES[PROGRAM_LANGUAGE][4])
        date_format = self.choose_date_format()
        final_date_string = self.get_date_string(self.get_date_from_string(final_date, date_format))

        return today_date_string, final_date_string
