 TermArduino 🌡️
Este projeto faz o monitoramento de temperatura usando Arduino, o sensor DS18B20 e um servidor Flask em Python.
O Arduino lê a temperatura através do DS18B20 e envia os dados pela porta serial. O Flask recebe essas leituras e disponibiliza em tempo real via API e interface web com gráfico dinâmico.

*Funcionalidades*
- Leitura contínua da temperatura via DS18B20 conectado ao Arduino.
- API REST (/temperatura) que retorna a última leitura em JSON.
- Interface web (/) que mostra:
   - Temperatura em Celsius, Fahrenheit e Kelvin.
   - Gráfico em tempo real com histórico das últimas leituras.
   - Atualização automática a cada segundo.

*Estrutura do projeto*
- app.py: servidor Flask que gerencia rotas e integra com a leitura serial.
- serial_reader.py: funções para inicializar a porta serial e ler dados do Arduino.
- templates/index.html: página principal com exibição das temperaturas e gráfico.
- static/conversor.js: lógica frontend para atualizar valores e desenhar o gráfico.
- arduino/: pasta contendo o código do Arduino para leitura do DS18B20.
- README.md: documentação do projeto.

*Instalação*
1. Clone o repositório:
   - git clone https://github.com/sandromelojr/TermArduino.git
   - cd TermArduino/servidor
2. Crie e ative o ambiente virtual:
   - python -m venv .venv
   - .venv\Scripts\Activate.ps1   # no PowerShell
3. Instale as dependências:
   - pip install -r requirements.txt

*Dependências*
- Flask
- pyserial
  Essas bibliotecas estão listadas no requirements.txt.

*Código do Arduino*
Para que o projeto funcione corretamente, é necessário enviar o código para o Arduino utilizando a Arduino IDE.  
O código está disponível dentro da pasta arduino/ do projeto.

- Bibliotecas necessárias
Antes de compilar e enviar o código, instale as seguintes bibliotecas na Arduino IDE:

- OneWire → usada para comunicação com o sensor DS18B20.  
- DallasTemperature → facilita a leitura da temperatura a partir do DS18B20.  

*Execução*
1. Conecte o Arduino na porta correta (ex.: COM6 no Windows).
2. Envie o código para o Arduino usando a Arduino IDE (o código está na pasta arduino/).
3. Inicie o servidor Flask:
   - python app.py
4. Abra no navegador:
   - http://127.0.0.1:5000/
  
*Uso*
- A página inicial mostra a temperatura atual em três unidades.
- O gráfico exibe as últimas 20 leituras.
- A API pode ser acessada diretamente em:

*Hardware utilizado*
- Arduino Uno (ou compatível)
- Sensor DS18B20 (digital, protocolo 1-Wire)
- Dois resistores de 10kΩ em paralelo (equivalem a ~5kΩ)
- Recomendação: usar resistor de 4,7kΩ como pull-up, que é o valor mais indicado para o DS18B20
- Protoboard e cabos jumper

*Observações*
- Certifique-se de que o Arduino está enviando apenas valores numéricos pela serial.
- Ajuste a porta serial em app.py conforme necessário (COM6, /dev/ttyUSB0, etc).
- O código do Arduino deve ser enviado pela Arduino IDE antes de iniciar o servidor Flask.
- Este projeto é para fins educacionais e não deve ser usado em produção sem ajustes de segurança.

*Licença*
- Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.
