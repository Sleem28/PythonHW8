from GUI.write_to_phonebook import write_to_book


def import_person(info: str):
    person = info
    write_to_book(person=person)

