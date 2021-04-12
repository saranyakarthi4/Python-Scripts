import yaml
import io,os

# Define data
data = {'key_value' : 12,
	'a list': [1, 42, 3.141, 1337, 'help'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}
# Write YAML file
with io.open("/Users/skarthi/yaml_target_folders/file2/a2.yaml", "w", encoding="utf8") as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

# Read YAML file
with open("/Users/skarthi/yaml_target_folders/file2/a2.yaml", 'r') as stream:
    data_loaded = yaml.load(stream)
print (data_loaded)
