import yaml

class ConfigLoader:
    def __init__(self,config='../config.yaml'):
        self.config_path = config

    def load_config(self):
        with open(self.config_path,'r') as f:
            print(self.config_path)
            config = yaml.safe_load(f)
        return config
    
if __name__ =="__main__":
    conf = ConfigLoader()