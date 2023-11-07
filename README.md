# MQTT_LIBERATO

Um dispositivo IoT realiza a tarefa de fazer a “chamada” dos alunos das turmas de quarto ano. 
A chamada é feita através de uma mensagem que contém, entre outros campos, o número de matrícula do aluno que deve responder. Esta mensagem é codificada em formato  JSON e transmitida através do protocolo MQTT.

## Sua tarefa consiste em:

- Identificar os dados contidos na mensagem enviada (campos e tipos de dados)
 
### Desenvolver uma aplicação que:

- Responda somente quando o campo matricula conter o seu número de matrícula 

#### Modifique os campos da mensagem  segundo as regras: 

- Seq deve receber seq + 800000
- Completar os campos com conteúdo vazio.
- Indicar, através do campo climatizado, se o condicionador de ar está ativo (considere que o equipamento só refrigera);
- Suprima as variáveis de temperatura e umidade informadas.

##  Os dados relativos a comunicação encontram-se abaixo:

Broker: test.mosquitto.org porta 1883 (não criptografado)
Liberato/iotTro/44xx/data - tópico por onde são enviados os dados do dispositivo
Liberato/iotTro/44xx/rply/<matricula> - tópico por onde deve ser enviada a resposta solicitada.

## Em caso de sucesso na comunicação:
Liberato/iotTro/44xx/ack/<matricula> – ao receber uma resposta, o dispositivo envia, através deste tópico, uma mensagem confirmando a recepção. A confirmação consiste no id do remetente. O número de matrícula corresponde ao enviado na mensagem confirmada

##  Em caso de erro:

Liberato/iotTro/44xx/ack/ – será enviada mensagem com o número de sequência recebido e código de erro no campo ack, conforme mensagem abaixo:

NSTR - mensagem enviada em formato diferente de string

NOK - não foi possível interpretar a mensagem. Erro grave de formato.

NID - erro/ausência no campo id e/ou matrícula.

NSQ - sequência inválida

NAN - erro/ausência de dados solicitados

NEX - campos extras não solicitados na mensagem
	
Não são necessárias muitas respostas, 3 ou 4 são suficientes. As respostas ficam registradas no dispositivo IoT.

