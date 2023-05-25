import json


class ReadWriteUtils:

    def read_json_file(self, file_path: str) -> dict | list:
        with open(file_path, encoding='utf-8') as file:
            return json.load(file)

    def write_to_json_file(self, file_path: str, data: list[dict]) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, fp=file, ensure_ascii=False)


read_write_json = ReadWriteUtils()
PROGRAM_LANGUAGE = read_write_json.read_json_file('src/config.json')['language']
MESSAGES = {
    'PT': [
        # Mensagem de erro #1
        'Sem mensagem!',
        # Confirmação
        'Está correto? \n[0] Sim \n[1] Não \n> ',
        # Mensagem de erro #2
        'Valor inválido!'
    ],
    'EN': [
        # Error message #1
        'No message!',
        # Confirmation
        'Is it right? \n[0] Yes \n[1] No \n> ',
        # Error message #2,
        'Invalid value!'
    ]
}


class InputUtils:

    def is_str_input_right(self, message=None) -> str:
        if message is None:
            print(self, message)
            raise Exception(MESSAGES[PROGRAM_LANGUAGE][0])

        while True:
            text_input = input(message)
            is_right = input(MESSAGES[PROGRAM_LANGUAGE][1])

            if is_right == '0':
                return text_input

    def is_int_input_right(self, message=None, max_value=None) -> int:
        while True:
            input_value = self.is_str_input_right(message)
            try:
                input_value = int(input_value)
            except ValueError:
                print(MESSAGES[PROGRAM_LANGUAGE][2])

            if max_value is None or input_value <= max_value:
                return input_value

            print(MESSAGES[PROGRAM_LANGUAGE[2]])
