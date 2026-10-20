import pytest

from digient.components.physiology import (
    ComponenteFisiologiaBasica,
    ComponenteIdentidade,
)


@pytest.fixture
def turi_id():
    """Cria uma instância nova de identidade do
    digiente para cada teste que a solicitar"""
    return ComponenteIdentidade()


@pytest.fixture
def turi_fisiologia_basica():
    """Retorna uma instância nova da fisiologia
    básica do digiente para cada teste que o solicitar"""
    return ComponenteFisiologiaBasica()


def test_componente_identidade_padrao(turi_id):

    assert turi_id.nome == "Turi"
    assert turi_id.linhagem == "Neuroblast-G1"
    assert turi_id.momento_concepcao > 0


def test_componente_fisiologia_basica(turi_fisiologia_basica):

    assert turi_fisiologia_basica.energia == 100.0
    assert turi_fisiologia_basica.saude == 100.0
    assert turi_fisiologia_basica.humor == 0.0
    assert turi_fisiologia_basica.conexao == 50.0
    assert turi_fisiologia_basica.em_hibernacao is False
    assert turi_fisiologia_basica.ultima_atualizacao > 0


def test_componente_fisiologia_basica_padrao_e_customizada():
    turi = ComponenteFisiologiaBasica(energia=35.0, humor=-12.0)

    assert turi.energia == 35.0
    assert turi.humor == -12.0
