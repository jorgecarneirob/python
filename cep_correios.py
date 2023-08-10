import requests
import json


def infos_cep(cep):
    req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    infos = json.loads(req.text)
    return infos


cep_info = infos_cep('06414025')

keys = ['logradouro', 'bairro', 'localidade', 'uf']
ref = ['Rua', 'Bairo', 'Cidade', 'Estado']

print('Confirme se as informações estão corretas:')
for k, j in zip(keys, ref):
    print(f'{j} : {cep_info[k]}')
