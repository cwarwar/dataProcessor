def process(facts: list, schemas: list):

    result = []
    schemasDict = {}
    allowedAttribute = 'cardinality'
    allowedAttributeValues = ['one', 'many']

    #Verificando o tipo dos parâmetros
    if not isinstance(facts, list) or not isinstance(schemas, list):
        raise TypeError

    #Criando um dicionário com as cardinalidades
    for schema in schemas:
        if schema[1] != allowedAttribute:
            raise Exception('Atributo não reconhecido')
        if schema[2] not in allowedAttributeValues:
            raise Exception('Valor do atributo não reconhecido')
        schemasDict[schema[0]] = schema[2]

    #Montando o resultado
    for fact in facts:

        try:
            schemasDict[fact[1]]
        except: 
            raise Exception('Tipo do atributo do schema difere do fact')

        if fact[3] == True:

            if schemasDict[fact[1]] == allowedAttributeValues[1]:
                result.append(fact)
            else:
                [result.remove(element) for element in result if element[0] == fact[0] and element[1] == fact[1]]
                result.append(fact)

        elif fact[3] == False:
                [result.remove(element) for element in result if element[0] == fact[0] and element[1] == fact[1] and element[2] == fact[2]]

    return result