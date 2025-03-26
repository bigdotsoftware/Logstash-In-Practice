from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader
from avro import schema
import json
import io
import avro.io

user_schema = {
    "name": "avro.example.User",
    "type": "record",
    "fields": [
        {"name": "username", "type": "string"},
        {"name": "age", "type": "int"},
        {"name": "city", "type": "string"}
    ]
}
# Parse the schema so we can use it to write the data
schema_parsed = schema.parse(json.dumps(user_schema))

records = [
    {"username": "Mike", "age":43, "city": "NYC"},
    {"username": "Ann", "age":28, "city": "London"},
    {"username": "Piotr", "age":31, "city": "Warsaw"}
]

# Write data to an avro file
with open('userdata.avro', 'wb') as f:
    writer = avro.io.DatumWriter(schema_parsed)
    #writer = DataFileWriter(f, DatumWriter(), schema_parsed)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    
    writer.write({"username": "Mike", "age":43, "city": "NYC"}, encoder)
    writer.write({"username": "Mike", "age":43, "city": "NYC"}, encoder)
    writer.write({"username": "Mike", "age":43, "city": "NYC"}, encoder)
    
    raw_bytes = bytes_writer.getvalue()
    f.write(raw_bytes)
    #writer.close()
    
#with open('userdata.avro', 'wb') as out:
#    writer(out, None, [{"username": "Mike", "age":43, "city": "NYC"}] )
#with open('userdata.avro', 'a+b') as out:
 #   writer(out, None, [{"username": "Ann", "age":28, "city": "London"}] )
#with open('userdata.avro', 'a+b') as out:
#    writer(out, None, [{"username": "Piotr", "age":31, "city": "Warsaw"}] )
