import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from client import BoundingBoxTableReconstructor

class CoreTests(unittest.TestCase):
    def setUp(self):self.c=BoundingBoxTableReconstructor()

    def test_variable_width_columns(self):
        boxes=[{'x0':x,'x1':x+w,'y0':y,'y1':y+10,'text':t} for x,w,y,t in [(10,80,0,'Name'),(150,100,0,'Value'),(10,20,30,'A'),(150,20,30,'2')]]
        self.assertEqual(self.c.reconstruct_table_grid(boxes)['grid'],[['Name','Value'],['A','2']])
        self.assertEqual(self.c.reconstruct_table_grid([])['grid'],[])
    def test_markdown_and_invalid_box(self):
        self.assertIn('a\\|b',self.c.format_to_markdown([['a|b']]))
        with self.assertRaises(ValueError):self.c.reconstruct_table_grid([{'x0':3,'x1':1,'y0':0,'y1':5,'text':'x'}])
