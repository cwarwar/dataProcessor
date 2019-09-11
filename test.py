from dataProcessor import process
import unittest


class testDataProcessor(unittest.TestCase):

    facts = [('gabriel', 'endereço', 'av rio branco, 109', True), ('joão', 'endereço', 'rua alice, 10', True), ('joão', 'endereço', 'rua bob, 88', True),   
        ('joão', 'telefone', '234-5678', True), ('joão', 'telefone', '91234-5555', True), ('joão', 'telefone', '234-5678', False), ('gabriel', 'telefone', '98888-1111', True), ('gabriel', 'telefone', '56789-1010', True) ]

    schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

    def testBasicScenario(self):

        expectedResult = [('gabriel', 'endereço', 'av rio branco, 109', True), 
        ('joão', 'endereço', 'rua bob, 88', True),  
        ('joão', 'telefone', '91234-5555', True), 
        ('gabriel', 'telefone', '98888-1111', True), 
        ('gabriel', 'telefone', '56789-1010', True)]

        result = process(self.facts, self.schema)

        self.assertEqual(result, expectedResult)

    def testAllFactsTrue(self):

        facts = [('gabriel', 'endereço', 'av rio branco, 109', True), ('joão', 'endereço', 'rua alice, 10', True), ('joão', 'endereço', 'rua bob, 88', True),   
        ('joão', 'telefone', '234-5678', True), ('joão', 'telefone', '91234-5555', True), ('joão', 'telefone', '234-5678', True), ('gabriel', 'telefone', '98888-1111', True), ('gabriel', 'telefone', '56789-1010', True) ]

        schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

        expectedResult = [('gabriel', 'endereço', 'av rio branco, 109', True), 
        ('joão', 'endereço', 'rua bob, 88', True), 
        ('joão', 'telefone', '234-5678', True), 
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', True),
        ('gabriel', 'telefone', '98888-1111', True), 
        ('gabriel', 'telefone', '56789-1010', True)]

        result = process(facts, schema)
        self.assertEqual(result, expectedResult)

    def testAllFactsFalse(self):

        facts = [('gabriel', 'endereço', 'av rio branco, 109', False), ('joão', 'endereço', 'rua alice, 10', False), ('joão', 'endereço', 'rua bob, 88', False),   
        ('joão', 'telefone', '234-5678', False), ('joão', 'telefone', '91234-5555', False), ('joão', 'telefone', '234-5678', False), ('gabriel', 'telefone', '98888-1111', False), ('gabriel', 'telefone', '56789-1010', False) ]

        schema = [('endereço', 'cardinality', 'one'), ('telefone', 'cardinality', 'many')]

        expectedResult = []

        result = process(facts, schema)
        self.assertEqual(result, expectedResult)


    def testDiferentAttributeName(self):

        facts = [('gabriel', 'endereço2', 'av rio branco, 109', True), ('joão', 'endereço2', 'rua alice, 10', True), ('joão', 'endereço2', 'rua bob, 88', True),   
        ('joão', 'telefone2', '234-5678', True), ('joão', 'telefone2', '91234-5555', True), ('joão', 'telefone2', '234-5678', False), ('gabriel', 'telefone2', '98888-1111', True), ('gabriel', 'telefone2', '56789-1010', True) ]

        schema = [('endereço2', 'cardinality', 'one'), ('telefone2', 'cardinality', 'many')]

        expectedResult = [('gabriel', 'endereço2', 'av rio branco, 109', True), 
        ('joão', 'endereço2', 'rua bob, 88', True), 
        ('joão', 'telefone2', '91234-5555', True), 
        ('gabriel', 'telefone2', '98888-1111', True), 
        ('gabriel', 'telefone2', '56789-1010', True)]

        result = process(facts, schema)

        self.assertEqual(result, expectedResult)

    def testInvalidAttributeName(self):

        schemaWithInvalidType = [('tipo invalido', 'cardinality', 'one'), ('tipo invalido2', 'cardinality', 'many')]
        with self.assertRaises(Exception):
            process(self.facts, schemaWithInvalidType)

    def testInvalidAtribbute(self):

        schemaWithInvalidAttribute = [('endereço', 'atributo invalido', 'one'), ('telefone', 'atributo invalido', 'many')]

        with self.assertRaises(Exception):
            process(self.facts, schemaWithInvalidAttribute)

    def testInvalidAtribbuteValue(self):

        schemaWithInvalidAttributeValue = [('endereço', 'cardinality', 'valor invalido'), ('telefone', 'cardinality', 'valor invalido')]

        with self.assertRaises(Exception):
            process(self.facts, schemaWithInvalidAttributeValue)

    def testInvalidParameter(self):

        invalidFacts = 'facts'
        invalidSchema = 'schema'

        with self.assertRaises(TypeError):
            process(invalidFacts, invalidSchema)

        with self.assertRaises(TypeError):
            process(self.facts, invalidSchema)
        
        with self.assertRaises(TypeError):
            process(invalidFacts, self.schema)

if __name__ == '__main__':
    unittest.main()