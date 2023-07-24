from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# uvicorn main:app --reload
app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/get_devices_measures/auth/rfid"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

devices = {
    "lights": {
    "led" : False,
    "rgb" : False
    },
    "interactives" : {
        "humidifier": False,
        "cats_water" : False
    },
    "auth": {
        "rfid": False
    }

}

dictteste = {
    'valor1': True
}

@app.get("/")
def home():
    return {"status_API": "Ativa"}

@app.get("/dev_esp")
def dev_esp():
    return dictteste

@app.get("/post_devices_measures/{device}/{measure}/{value}")
def post_measures(device: str, measure: str, value: int):
    if value == 1 or value == 0:
        if device in devices:
            if measure in devices[device]:
                devices[device][measure] = True if value == 1 else False
                print(devices)
                return devices
            else:
                return {"Erro": "Medida não encontrado."}
        else:
            return {"Erro": "Dispositivo não encontrado."}
    else:
        return {"Erro": "Valor de medida incorreta."}

@app.get("/get_devices_measures/{device}/{measure}")
def get_measures(device: str, measure: str):
    if device in devices:
        if measure in devices[device]:
            return devices[device][measure]
        else:
            return {"Erro": "Medida não encontrado."}
    else:
        return {"Erro": "Dispositivo não encontrado."}