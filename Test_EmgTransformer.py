import unittest
import EmgTransformer
from EmgReader import *
from ActionEnum import ActionEnum
from DTO_Action import DTO_Action


class TransformerTest(unittest.TestCase):
    # Naming convention: test_<testmethod>_<doing>_<expected result>
    def test_handleSensorValues_sendingClose2sensors_CloseActions(self):
        # In order to receive close, sensor 2 must send over 2V and sensor 1 should send under 2V

        # Arrange
        configPath = '2sensors.ini'
        sensorValues = {0: 0.01, 1: 2.53}
        enum = ActionEnum
        dto = DTO_Action()

        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)

        # Act
        result = transformer.handleSensorValues()
        dto.actions[0] = enum.close
        dto.actions[1] = enum.close
        dto.actions[2] = enum.close
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.stop

        # Assert
        print(result)
        print(dto.actions)
        self.assertEqual(result, dto.actions)

        # Når jeg tester metoderne, er det ikke nødvendigt at teste de private metoder. De er kun til for at gøre koden mere overskuelig.
        # Assert på hvad du forventer at få tilbage når du tester metoden.
        # Ved denne metode skal der returneres noget, alt efter hvad ADC'en sender tilbage.
        # For at kunne styre adc'en er det derfor nødvendigt med en fake adc.
        # Evt. også en fake config file, der sendes ind gennem dependency injection, sådan at man kan have forskellige filer med forskellige antal sensorer osv.

        # Mangler at teste: 1, 3, 4 sensorer
        # open, close metoder
        # not applicable
        # ingen sensorer
        # for mange sensorer?
        # begge sensorer under 2V
        # begge sensorer +2V

        # ------------------ Andre tests ----------------
        # sender kun når der modtages nyt greb
        # Errors
        # serialiserer korrekt
        # error handling on uneven sensornumbers


if __name__ == '__main__':
    unittest.main()
