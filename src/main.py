#! python3.11.2
import os
from GenericUtils.generic_utils import InputUtils, ReadWriteUtils
from Dates.get_dates import GetDates
from Reminders import (create_reminder, delete_reminder, send_reminders,
                       show_reminders)


read_write_utilities = ReadWriteUtils()
input_utilities = InputUtils()
date_utilities = GetDates()
show_utilities = show_reminders.ShowReminders()
send_utilities = send_reminders.SendReminders()
create_utilities = create_reminder.CreateReminder()
delete_utilities = delete_reminder.DeleteReminder()

CONFIG_FILE = read_write_utilities.read_json_file('src/config.json')
PROGRAM_LANGUAGE = CONFIG_FILE['language']
BULETIN_HEADER = CONFIG_FILE['header']
MESSAGES = {
    'PT': [
        # Menu de opções
        """
    Opções:
    [0] Mostrar lembretes
    [1] Mostrar seções
    [2] Enviar lembretes
    [3] Criar lembrete
    [4] Criar seção
    [5] Apagar lembrete
    [6] Apagar seção
    [7] Sair do do programa
        """,
        # Selecionar opção
        'Qual a opção desejada? \n> ',
        # Mostrar seção específica
        'Deseja ver o conteúdo de uma seção específica? \n[0] Sim \n[1] Não \n> ',
        # Mensagem de erro #1
        'Opção inválida selectionada!',
        # Usar data de hoje
        'Usar a data de hoje para criar a mensagem? \n[0] Sim \n[1] Não \n> ',
        # Data desejada
        'Qual a data desejada? \n> ',
        # Mensagem de saída (teclado)
        'Finalizando o programa...',
        # Tipo de apagamento
        'Apagar apenas um lembrete ou todos os ultrapassados? \n[0] Apenas um \n[1] Todos os ultrapassados \n> '
    ],
    'EN': [
        # Options menu
        """
    Options:
    [0] Show reminders
    [1] Show sections
    [2] Send reminders
    [3] Create reminder
    [4] Create section
    [5] Delete reminder
    [6] Delete section
    [7] Exit program
       """,
       # Select option
       'What\'s the desired option? \n> ',
       # Show a specific section
        'Do you wish to see the content of a specific section? \n [0] Yes \n [1] No \n> ',
        # Error message #1
        'An invalid option was selected!',
        # Use today's date
        'Use today\'s  to  create the message? \n [0] Yes \n [1] No \n> ',
        # Desired date
        'What\'s the desired date? \n> ',
        # Exit message (keyboard)
        'Finishing the program...',
        # Delete type
        'Delete just one reminder ou all outdated reminders? \n[0] Just one \n[1] All outdated \n> '
    ]
}

reminders_file = read_write_utilities.read_json_file(CONFIG_FILE['reminders_file'])


def show_stored_reminders(file: list[dict]) -> None:
    show_utilities.show_all_reminders(file)


def show_sections(file: list[dict]) -> None:
    show_full_section = input_utilities.is_int_input_right(
        MESSAGES[PROGRAM_LANGUAGE][2])

    if show_full_section == 1:
        show_utilities.show_all_sections(file)

    elif show_full_section == 0:
        show_utilities.show_section(file)

    else:
        print(MESSAGES[PROGRAM_LANGUAGE][3])


def create_reminder_bulletin(file: list[dict]) -> None:
    use_today_date = input_utilities.is_int_input_right(
        MESSAGES[PROGRAM_LANGUAGE][4])
    date = date_utilities.get_today_date()

    if use_today_date not in (0, 1):
        print(MESSAGES[PROGRAM_LANGUAGE][3])
        return

    if use_today_date == 1:
        date_string = input_utilities.is_str_input_right(
            MESSAGES[PROGRAM_LANGUAGE][5])
        date_format = date_utilities.choose_date_format()
        date = date_utilities.get_date_from_string(date_string, date_format)

    print(BULETIN_HEADER.format(date.strftime('%d/%m/%Y')))

    send_utilities.paste_reminder_list(
        send_utilities.create_reminders_list(file, date))


def create_one_reminder(file: list[dict]) -> None:
    create_utilities.create_reminder(file)


def create_one_section(file: list[dict]) -> None:
    create_utilities.create_section(file)


def delete_one_or_outdated(file: list[dict]) -> None:
    chosen_input = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][7])

    if chosen_input == 0:
        delete_utilities.select_reminder_to_delete(file)

    elif chosen_input == 1:
        delete_utilities.outdated_reminders(file)
    
    else:
        print(MESSAGES[PROGRAM_LANGUAGE][2])


def delete_one_section(file: list[dict]) -> None:
    delete_utilities.delete_section(file)


def main():
    options_functions = {
        0: show_stored_reminders,
        1: show_sections,
        2: create_reminder_bulletin,
        3: create_one_reminder,
        4: create_one_section,
        5: delete_one_or_outdated,
        6: delete_one_section
    }
    try:
        while True:
            print(MESSAGES[PROGRAM_LANGUAGE][0])
            chosen_option = input_utilities.is_int_input_right(MESSAGES[PROGRAM_LANGUAGE][1], 7)

            if chosen_option == 7:
                return

            options_functions[chosen_option](reminders_file)

    except KeyboardInterrupt:
        print(MESSAGES[PROGRAM_LANGUAGE][6])

if __name__ == '__main__':
        main()
