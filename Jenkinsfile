pipeline {
    agent any

    parameters {
        string(name: 'PERGUNTA', defaultValue: '', description: 'Pergunta a ser processada pelo chatbot')
        string(name: 'LIMIAR_DISTANCIA', defaultValue: '5', description: 'Distância limiar para considerar uma pergunta semelhante')
        string(name: 'EMAIL_RECIPIENTS', defaultValue: 'jpfalcuci@gmail.com', description: 'Endereços de email dos destinatários, separados por vírgula')
    }

    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'ja instalado'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                sh 'python3 levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                sh "python3 chat_bot.py '${params.PERGUNTA}' '${params.LIMIAR_DISTANCIA}'"
            }
        }

    }
    
    post {
        always {
            mail body: 'O pipeline ${currentBuild.fullDisplayName} foi executado!',
                subject: 'Pipeline ${currentBuild.fullDisplayName} executado',
                to: "${params.EMAIL_RECIPIENTS}"
        }
    }
}
