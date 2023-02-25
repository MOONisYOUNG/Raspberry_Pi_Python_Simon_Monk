class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor
        
    def description(self):
        return 'Convert ' + self.units_from + ' to ' + self.units_to
    
    def convert(self, value):
        return value * self.factor

    
class ScaleAndOffsetConverter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        # 객체 상속 표기법 1
        # super().__init__(units_from, units_to, factor)
        
        # 객체 상속 표기법 2
        ScaleConverter.__init__(self, units_from, units_to, factor)
        
        self.offset = offset
        
    def convert(self, value):
        return value * self.factor + self.offset
    
    
if __name__ == '__main__':
    c1 = ScaleConverter('inches', 'mm', 25)
    print(c1.description())
    print('converting 2 inches')
    print(str(c1.convert(2)) + c1.units_to)
    
    print('\n')
    
    c2 = ScaleAndOffsetConverter('C', 'F', 1.8, 32)
    print(c2.description())
    print('converting 20C')
    print(str(c2.convert(20)) + c2.units_to)
    