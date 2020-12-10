from textwrap import dedent

from shared_localization.localizable_strings import load_localizable_strings_from_yaml


def test_load_strings_from_yaml():
    yaml = dedent('''
        someKey: Some Value
        someList:
          - First Item
          - Second Item
        someDict:
          someNestedKey: Some Nested Value
          someNestedList:
            - First Nested Item
            - Second Nested Item
    ''')
    expected = {
        'someKey': 'Some Value',
        'someList': [
            'First Item',
            'Second Item',
        ],
        'someDict': {
            'someNestedKey': 'Some Nested Value',
            'someNestedList': [
                'First Nested Item',
                'Second Nested Item',
            ]
        }
    }
    strings = load_localizable_strings_from_yaml(yaml)
    assert strings == expected
