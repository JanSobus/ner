import pytest
from modules.ner_inference import Entity

def test_entity():  
    entity = Entity("O", 0.9, "John", 0, 4)
    assert entity.entity_group == "O"
    assert entity.score == 0.9
    assert entity.word == "John"
    assert entity.start == 0
    assert entity.end == 4
    with pytest.raises(ValueError):
        Entity("Z", 0.9, "John", 0, 4)