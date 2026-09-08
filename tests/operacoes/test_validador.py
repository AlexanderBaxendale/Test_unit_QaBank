import pytest
from tech.operacoes.validador_conta import validar_abertura_conta


@pytest.fixture
def cenarios():
    return [
        {
            "nome": "idade abaixo de 18 com score alto",
            "idade": 17,
            "score_credito": 800,
            "resultado_esperado": ValueError,
        },
        {
            "nome": "idade abaixo de 18 com score baixo",
            "idade": 17,
            "score_credito": 300,
            "resultado_esperado": ValueError,
        },
        {
            "nome": "idade acima de 18 com score alto",
            "idade": 18,
            "score_credito": 800,
            "resultado_esperado": "Aprovado",
        },
        {
            "nome": "idade acima de 18 com score baixo",
            "idade": 18,
            "score_credito": 500,
            "resultado_esperado": "Recusado",
        },
    ]


@pytest.mark.parametrize(
    "indice, nome_cenario",
    [
        pytest.param(0, "idade abaixo de 18 com score alto", id="idade abaixo de 18 com score alto"),
        pytest.param(1, "idade abaixo de 18 com score baixo", id="idade abaixo de 18 com score baixo"),
        pytest.param(2, "idade acima de 18 com score alto", id="idade acima de 18 com score alto"),
        pytest.param(3, "idade acima de 18 com score baixo", id="idade acima de 18 com score baixo"),
    ],
)
def test_validar_abertura_conta(cenarios, indice, nome_cenario):
    cenario = cenarios[indice]

    assert cenario["nome"] == nome_cenario

    if isinstance(cenario["resultado_esperado"], type) and issubclass(cenario["resultado_esperado"], Exception):
        with pytest.raises(cenario["resultado_esperado"], match="Menor de idade não permitido"):
            validar_abertura_conta(cenario["idade"], cenario["score_credito"])
        return

    assert validar_abertura_conta(cenario["idade"], cenario["score_credito"]) == cenario["resultado_esperado"]
