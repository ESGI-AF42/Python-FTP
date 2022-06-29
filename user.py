import pathlib, csv, shutil
from tempfile import NamedTemporaryFile



class User():
    actual_path= pathlib.Path(__file__ )
    parent_path = actual_path.parent.__str__()
    user_file_path = parent_path+'\\user.csv'

    def __init__(self, nickname,password,status,site):
        self.nickname = nickname
        self.password = password
        self.status = status
        self.site = site 
        # P = Paris, R = Rennes , S= Strasbourg et G= Grenoble



    def get_user_nickname(self):
        return self.nickname

    def get_user_password(self):
        return self.password

    def get_user_status(self):
        return self.status

    def get_user_site(self):
        return self.site

    def set_user_status(self,status):
        self.status = status

        
    

    #debut load_user_from_csv()
    def load_user_from_csv():
            user_list = []
            cpt_column = User.search_in_file()
            with open(User.user_file_path, 'r') as csvfile:
                filereader = csv.reader(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for line in filereader:
                    user_list.append(User(line[cpt_column["Nickname"]],line[cpt_column["Password"]], line[cpt_column["Status"]],line[cpt_column["Site"]]))
                csvfile.close()
            return user_list    
    #fin load_user_from_csv()


    #debut search_in_file()
    def search_in_file():
        columnInfile = {}

        with open(User.user_file_path, 'r') as csvfile:
            filereader = csv.reader(csvfile, lineterminator = '\n', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            tmp_cpt = 0       
            for line in filereader:
                for column in line:
                    if column == "Nickname":
                        columnInfile["Nickname"] = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Password":
                        columnInfile["Password"] = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Status":
                        columnInfile["Status"] = tmp_cpt
                        tmp_cpt=tmp_cpt+1

                    elif column == "Site":
                        columnInfile["Site"] = tmp_cpt
                        tmp_cpt=tmp_cpt+1
                            
                    else:
                        break   
            csvfile.close()
        return columnInfile

   


