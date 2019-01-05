from rasa_nlu.model import Metadata, Interpreter
from teststack import log_evaluation_table

class TestClass(object):
    interpreter = Interpreter.load('./models/current/nlu')
    def test_greet(self):
        intent = self.interpreter.parse(u"hi")['intent']['name']
        assert intent == 'greet'

    def test_bye(self):
        intent = self.interpreter.parse(u"bye")['intent']['name']
        assert intent == 'goodbye'
    
    def test_joke(self):
        intent = self.interpreter.parse(u"Tell me a joke")['intent']['name']
        assert intent == 'joke'
    
    def test_thank(self):
        intent = self.interpreter.parse(u"Thank you")['intent']['name']
        assert intent == 'thanks'
        
    def test_greet1(self):
        intent = self.interpreter.parse(u"hello")['intent']['name']
        assert intent == 'greet'
