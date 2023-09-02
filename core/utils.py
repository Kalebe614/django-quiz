import datetime

def iniciar_quiz(request):
# Obtenha o tempo inicial
    tempo_inicial = datetime.datetime.now()

    # Converta o tempo inicial em uma string ISO 8601
    tempo_inicial_iso = tempo_inicial.isoformat()
    
    # Armazene o tempo inicial na sessão do usuário
    request.session['tempo_inicial'] = tempo_inicial_iso

#Reset old quiz data
def reset_quiz_data(self, QuizModel):
    QuizModel.objects.all().delete()