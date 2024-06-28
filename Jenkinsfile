pipeline {
    agent any

    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'ja instalado'
            }
        }

        stage('Ler Perguntas do Arquivo') {
            steps {
                script {
                    def perguntasFile = 'perguntas_disponiveis.txt'
                    perguntasDisponiveis = readFile(perguntasFile).split('\n').collect { it.split('\\|')[0].trim() }
                }
            }
        }

        stage('Definir Parâmetros') {
            steps {
                script {
                    // Definir parâmetros dinamicamente
                    def paramsFileContent = """{
                        "parameters": [
                            {
                                "name": "PERGUNTAS",
                                "description": "Selecione as perguntas a serem processadas (Ctrl/Cmd para selecionar múltiplas)",
                                "choices": ${perguntasDisponiveis as List}
                            },
                            {
                                "name": "LIMIAR_DISTANCIA",
                                "description": "Distância limiar para considerar uma pergunta semelhante",
                                "default": 5,
                                "type": "number"
                            }
                        ]
                    }"""
                    writeFile file: 'params.json', text: paramsFileContent
                    sh 'cat params.json'
                }
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
                script {
                    def perguntasSelecionadas = params.PERGUNTAS.tokenize('\n')
                    def limiarDistancia = params.LIMIAR_DISTANCIA.toInteger()
                    perguntasSelecionadas.each { pergunta ->
                        sh "python3 chat_bot.py '${pergunta}' ${limiarDistancia}"
                    }
                }
            }
        }
    }
}
