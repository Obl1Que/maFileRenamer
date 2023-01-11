import os, json

ABSmaFilePath = os.path.abspath('maFiles')

for maFileName in os.listdir(ABSmaFilePath):
    if maFileName != 'manifest.json':
        try:
            maFile = ABSmaFilePath + '\\' + maFileName

            file = open(maFile, encoding = 'utf-8')
            info = json.loads(file.read())
            file. close()

            maFileNameNew = ABSmaFilePath + '\\' + info["account_name"] + '.maFile'
            os.rename(maFile, maFileNameNew)
            print(f'{maFileName} успешно переименован в {info["account_name"]}.maFile!')
        except:
            print(f'\nОткрыть {maFileName} не удалось, возможно они зашифрованы в SDA.\n'
                  'Удалите пароль в SDA и попробуйте снова.\n')