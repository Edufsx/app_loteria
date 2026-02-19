import streamlit as st
import random

def check_numbers(sorte, usario):
    if usario == sorte:
        return True
    elif usario > sorte:    
        st.markdown(f"O seu chute é maior que o número sorteado! O total de tentativas é: {st.session_state.tentativas}", 
                text_alignment="center")
        return False
    else:
        st.markdown(f"O seu chute é menor que o número sorteado! O total de tentativas é: {st.session_state.tentativas}", 
                text_alignment = "center")
        return False    

def rerun_click():
    st.session_state.clear()


# Inicialização dos estados das variáveis
if "numero_sorteado" not in st.session_state:
    st.session_state.numero_sorteado = random.randint(1,15)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 3

if "jogo_ativo" not in st.session_state:
    st.session_state.jogo_ativo = False

numero_sorteado = st.session_state.numero_sorteado


# Configurações de Texto da página - Explicação jogo e título
st.set_page_config(page_title = "Loteria da Babilônia", page_icon="🎲")
st.title("**Loteria da Babilônia 🎲**", text_alignment = "center")
st.markdown(
    """
    Nesse jogo será sorteado um número de 1 a 15 e o seu objetivo é acertá-lo.
    Se você errar seu chute você saberá se ele é maior ou menor que o número sorteado. \n
    Boa sorte!""",
    text_alignment = "center") 



# Cotainer para colocar a caixa de seleção de número e dois botões
with st.container(border = True, horizontal_alignment="center", width="stretch"):
    
    # Caixa para seleção de números 
    valor = st.number_input("Escolha seu número da sorte",
                            min_value= 1, 
                            max_value = 15, 
                            value=1, 
                            disabled=st.session_state.jogo_ativo )

    # Botão de confirmar escolha
    botao = st.button("Confirmar", 
                      icon="✅",  
                      type="primary",
                      width="stretch",
                      shortcut="Enter",
                      disabled=st.session_state.jogo_ativo)
    

# Teste botão confimar
if botao == True: 
    # Igual o chute ao valor que estão no number input
    chute = valor

    # Diminuir uma Tentativa
    st.session_state.tentativas -= 1

    # Testaando se o número é correto com função, se for true exibe mensagem, botão de reinicar e encerra
    if check_numbers(numero_sorteado, chute):
        # Desativar Botao
        st.session_state.jogo_ativo = True

        st.success("✔️Parabéns, você acertou o número sorteado! \n" \
        "Para jogar novamente clique no botão Reiniciar Sorteio")
        reinicar_v = st.button("Reiniciar Sorteio", 
                      icon="🔄", 
                      width= "stretch",
                      shortcut="k",
                      type = "primary",
                      on_click=rerun_click)
        st.balloons()
        st.stop()
        

# Teste para o número de tentativas
if st.session_state.tentativas <= 0 or st.session_state.jogo_ativo == True:
    
    # Desativar Botao
    st.session_state.jogo_ativo = True
    
     # Mensagem que acabou as tentativas
    st.warning(f"❌Game Over! O número sorteado era {numero_sorteado}. Para jogar novamente clique no botão Reiniciar Sorteio")
        
    # Botão para reiniciar   
    reinicar = st.button("Reiniciar Sorteio", 
                      icon="🔄", 
                      shortcut="k",
                      width= "stretch",
                      type="secondary", 
                      on_click=rerun_click)
   
    # Mostrar flocos de neve na tela e tirar a possibilidade do botão
    st.snow()
   