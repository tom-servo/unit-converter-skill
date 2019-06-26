from mycroft import MycroftSkill, intent_file_handler, util as mutil
from pint import UnitRegistry

class UnitConverter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.units = UnitRegistry()
        self.Q_ = self.units.Quantity
        
    @intent_file_handler('converter.unit.intent')
    def handle_converter_unit(self, message):
        try:
            d = message.data
            (firstu, secondu, seconda) = (d['firstunit'], d['secondunit'], d['secondamount'])
            seconda = '1' if seconda == "a" else seconda
            qfrom = self.Q_(seconda + " * " + secondu);
            qTo = qfrom.to(firstu)
            resDict = {
                'firstAmount': mutil.nice_number(qTo.magnitude),
                'firstUnit': firstu,
                'secondAmount': seconda,
                'secondUnit': secondu
            }
            self.speak_dialog('converter.unit', resDict)
        except:
            self.speak_dialog('converter.unit.failed')

def create_skill():
    return UnitConverter()

