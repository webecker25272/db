queries1 = [
    ['PUT','123','city','tucson'],
    ['PUT','123','state','arizona'],
    ['PUT','123','name','wilson'],
    ['PUT','123','name','jed'],
    ['GET','123','name'],
    ['DELETE','123','name'],
    ['GET','123','name']
]

queries2 = [
    ['DELETE','123','city','tucson'],
    ['GET','123','state','arizona'],
    ['PUT','123','cat','george'],
    ['GET','123','cat',],
    ['PUT','333','name']
]

queries3 = [
    ['PUT','111','car','honda'],
    ['PUT','111','car','crv'],
    ['GET','111','car']
]

class Database(dict):
    def __init__(self):
        self.data = {}

    class Record(dict):
        pass

    class Field(dict):
        pass

    class Value(str):
        pass

    # class Message(str):
    #     def __init__(self) -> None:
    #         self._value = '-1'

    #     def setValue(self, value):
    #         self._value = value

    def put_transaction(self, key, field, value):
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = value
        return ''

    def get_transaction(self, key, field): #-> Message:
        if self.data == {}:
            return 'NO DATA!'
        if field not in self.data[key]:
            message = 'false'
        else:
            message = self.data[key][field]
        return message
    
    def delete_field_transaction(self, key, field): #-> Message:
        if self.data == {}:
            return 'NO DATA!'
        if field not in self.data[key]:
            message = 'false'
        else:
            del self.data[key][field]
            message = 'true'
        return message
    
    def process_batch_queries(self, queries): #-> list[Message]:

        messages = []
        for query in queries:
            transaction_type = query[0]
            key = query[1]
            field = query[2]

            if transaction_type == 'PUT':
                try:
                    value = query[3]
                    message = self.put_transaction(key=key, field=field, value=value)
                except:
                    message = 'false'
                messages.append(message)
            
            if transaction_type == 'GET':
                message = self.get_transaction(key=key, field=field)
                messages.append(message)

            if transaction_type == 'DELETE':
                message = self.delete_field_transaction(key=key, field=field)
                messages.append(message)
        
        return messages
        

db = Database()
msg1 = db.process_batch_queries(queries=queries1)
msg2 = db.process_batch_queries(queries=queries2)
msg3 = db.process_batch_queries(queries=queries3)
