import configparser

def Create_Config():
    config = configparser.ConfigParser()
    config["General"] = {"noTumorDir":"no", "yesTumorDir":"yes", "size": 64, "epoches":20}

    with open("config.ini", "w") as configfile:
        config.write(configfile)

Create_Config()

