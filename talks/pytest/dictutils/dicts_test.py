
import dicts

def test_dicts():
    d = {'name': 'python', 'type': 'dynamic'}
    
    assert dicts.add_prefix(d, 'language_') == {
        'language_name': 'python',
        'language_type': 'dynamic',
    }

