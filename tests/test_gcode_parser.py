import unittest
import app.core.gcode_parser as gcode_parser

gcode_simple = 'G0X165.979Y234.986Z15.000'
gcode_without_begin_g_code = 'X455.904Y1809.898'
gcode_without_x = 'G0Y234.986Z15.000'
gcode_without_y = 'G0X165.979Z15.000'
gcode_without_z = 'G0X165.979Y234.986'

class TestGcodeParser(unittest.TestCase):

    def test_parser_gcode_line_simple(self):
        result = ('G0', {'X': 165.979, 'Y': 234.986, 'Z': 15.0})
        self.assertEqual(result, gcode_parser.parse_gcode_line(gcode_simple))

    def test_parser_gcode_line_without_begin_g(self):
        result = (None, {'X': 455.904, 'Y': 1809.898})
        self.assertEqual(result, gcode_parser.parse_gcode_line(gcode_without_begin_g_code))

    def test_parser_gcode_line_without_y(self):
        result = ('G0', {'X': 165.979, 'Z': 15.0})
        self.assertEqual(result, gcode_parser.parse_gcode_line(gcode_without_y))

    def test_parser_gcode_line_without_z(self):
        result = ('G0', {'X': 165.979, 'Y': 234.986})
        self.assertEqual(result, gcode_parser.parse_gcode_line(gcode_without_z))
