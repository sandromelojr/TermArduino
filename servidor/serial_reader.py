import serial

def iniciar_serial(porta, baudrate=9600, timeout=1):
    """
    Inicializa a conexão serial com o Arduino.
    """
    try:
        ser = serial.Serial(porta, baudrate, timeout=timeout)
        print(f"Conexão aberta na porta {porta}")
        return ser
    except Exception as e:
        print(f"Erro ao abrir porta serial {porta}: {e}")
        return None

def ler_temperatura(ser):
    """
    Lê uma linha da porta serial e tenta converter para float.
    Retorna None se não conseguir.
    """
    if ser is None or not ser.is_open:
        return None
    try:
        linha = ser.readline().decode(errors="ignore").strip()
        if linha:
            return float(linha)
    except ValueError:
        # Caso a linha não seja um número válido
        return None
    except Exception as e:
        print(f"Erro na leitura serial: {e}")
        return None
