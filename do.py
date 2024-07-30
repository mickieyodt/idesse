# Function to replace repeaters in field definition
def replace_repeater_in_field_def(def, repeater):
    # Assuming def is a dictionary and we want to replace some placeholder with the repeater value
    for key in def:
        if isinstance(def[key], str):
            def[key] = def[key].replace('REPEATER_PLACEHOLDER', repeater)
    return def

# Example usage
field_def = {
    'name': 'field_name_REPEATER_PLACEHOLDER',
    'type': 'string',
    'label': 'Label for REPEATER_PLACEHOLDER'
}

repeater_value = 'example'

updated_field_def = replace_repeater_in_field_def(field_def, repeater_value)
print(updated_field_def)

# Expected Output:
# {
#   'name': 'field_name_example',
#   'type': 'string',
#   'label': 'Label for example'
# }
