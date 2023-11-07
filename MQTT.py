# MQTT chama - Rafael V. Volkmer - 4422 - 06/11/2023

import paho.mqtt.client as mqtt
import json

# Configurações do MQTT Broker
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883

# Matricula para verificar a correspondencia
matricula = "20000213"

# Acessa o endereço
def on_connect(client, userdata, flags, rc):
    client.subscribe("Liberato/iotTro/44xx/data")

def on_message(client, userdata, msg):
    
    try:
        
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)

        if "matricula" in data and int(data["matricula"]) == int(matricula):
            
            # Checa se a temperatura interna é menor que a externa. Se for, o ar condicionado está ativo
            if "tempInt" in data and "tempExt" in data:
                
                temp_int = float(data["tempInt"]["valor"])
                temp_ext = float(data["tempExt"]["valor"])
                
                if temp_int < temp_ext:
                    
                    data["climatizado"] = True
                    
                else:
                    
                    data["climatizado"] = False
                    
            else:
                
                data["climatizado"] = False  # Caso a informação seja perdida, define para false

            # Modifica os campos da mensagem
            data["seq"] += 800000
            data["nome"] = "Rafael Volkmer"
            data["turma"] = "4422"
            data["temperatura"] = None # Suprime a variável
            data["umidade"] = None     # Suprime a variável

            # Publica a resposta no tópico apropriado
            response_topic = f"Liberato/iotTro/44xx/rply/{matricula}"
            client.publish(response_topic, json.dumps(data))
            print(f"Resposta enviada para {response_topic}: {data}")
            
        else:
            
            print(f"Matrícula não corresponde: {data['matricula']}")

    except json.JSONDecodeError:
        print("Erro: mensagem não está no formato JSON válido")

def on_publish(client, userdata, mid):
    print(f"Resposta publicada com sucesso (MID: {mid})")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Inscrito no tópico Liberato/iotTro/44xx/data")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.connect(mqtt_broker, mqtt_port, 60)
client.loop_forever()
