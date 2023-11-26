from zeep import Client, Settings
import yaml

with open(r"config.yaml") as f:
    data = yaml.safe_load(f)
print(data["url"])
def check_word(word):

    settings = Settings(strict=False)
    client = Client(wsdl=data["url"],settings=settings)
    return client.service.checkText(word)[0]["s"]

