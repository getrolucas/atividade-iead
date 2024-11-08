
import streamlit as st

def inicializar_estado():
    if 'respostas' not in st.session_state:
        st.session_state['respostas'] = {}
    if 'atividade_concluida' not in st.session_state:
        st.session_state['atividade_concluida'] = False

questoes = [
    {
        "pergunta": "1. Qual computador foi um dos primeiros a utilizar válvulas eletrônicas para realizar cálculos?",
        "alternativas": ["ENIAC", "UNIVAC I", "IBM 305 RAMAC", "Altair 8800"],
        "correta": "ENIAC"
    },
    {
        "pergunta": "2. Qual tecnologia foi criada em 1969 e é considerada a precursora da internet moderna?",
        "alternativas": ["World Wide Web", "ARPANET", "IBM System/360", "Intel 4004"],
        "correta": "ARPANET"
    },
    {
        "pergunta": "3. Em que ano a Apple lançou o primeiro iPhone, revolucionando o mercado de smartphones?",
        "alternativas": ["2001", "2005", "2007", "2010"],
        "correta": "2007"
    },
    {
        "pergunta": "4. Qual foi o marco importante para a popularização dos sistemas operacionais gráficos, lançado em 1995?",
        "alternativas": ["Windows 1.0", "Mac OS", "Linux", "Windows 95"],
        "correta": "Windows 95"
    }
]

def mostrar_questionario():
    for i, questao in enumerate(questoes):
        st.subheader(questao["pergunta"])
        resposta = st.radio(
            "Escolha uma resposta:",
            questao["alternativas"],
            key=f"questao_{i}"
        )
        st.session_state['respostas'][i] = resposta

    if st.button("Enviar Respostas"):
        acertou = sum(
            1 for i, questao in enumerate(questoes)
            if st.session_state['respostas'].get(i) == questao["correta"]
        )
        total_questoes = len(questoes)
        st.success(f"Você acertou {acertou} de {total_questoes} questões.")
        st.session_state['atividade_concluida'] = True

inicializar_estado()

st.title("Questionário de Avaliação")

if not st.session_state['atividade_concluida']:
    mostrar_questionario()
else:
    st.success("Atividade Concluída!")