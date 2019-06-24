from mycroft import MycroftSkill, intent_file_handler


class UnitConverter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('converter.unit.intent')
    def handle_converter_unit(self, message):
        self.speak_dialog('converter.unit')


def create_skill():
    return UnitConverter()

