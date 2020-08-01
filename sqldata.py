import sqlite3

class SQLighter:
    def __init__(self, database_file):
        """CONNECT"""
        self.connection = sqlite3.connect(database_file,check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_sub(self, SAT=True):
        """ALL SUBSCRIBERS"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'databaseofazcamp' WHERE 'SAT' ="+str(SAT)).fetchall()

    def sub_exist(self, user_id):#success
        """CHECK IF EXISTS"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'databaseofazcamp' WHERE 'user_id' =?",(str(user_id),)).fetchall()
            return bool(str(result))

    def add_sub(self, user_id,name,surname,phone,sat,sport,time,style):#success
        """ADD"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'databaseofazcamp'('user_id','name_user', 'surname_user','phone_user','sat_user', 'sport_user', 'timem_user', 'style_user' )VALUES(?,?,?,?,?,?,?,?)", (str(user_id),name,surname,phone, str(sat),str(sport),str(time),str(style)))



    def name_data(self, name_id,user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'name_user'=? WHERE 'user_id' = ?",(name_id,str(user_id)))

    def sur_data(self, surname_id,user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'surname_user'=? WHERE 'user_id' = ?",(surname_id, str(user_id)))

    def phone_data(self, phone_id, user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'phone_user'=? WHERE 'user_id' = ?",(phone_id, str(user_id)))

    def sat_data(self, sat_id,user_id):  # surname_id, phone_id, sat_id, sport_id, time_id, style_id, full_id, user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'ПОСТУПЛЕНИЕ'=? WHERE 'user_id' = ?",(str(sat_id), str(user_id)))


    def sport_data(self, sport_id,user_id):  # surname_id, phone_id, sat_id, sport_id, time_id, style_id, full_id, user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'СПОРТ'=? WHERE 'user_id' = ?",(str(sport_id), str(user_id)))

    def time_data(self, time_id,user_id):  # surname_id, phone_id, sat_id, sport_id, time_id, style_id, full_id, user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'TIME_MANAGEMENT'=? WHERE 'user_id' = ?",(str(time_id), str(user_id),))

    def style_data(self, style_id,user_id):  # surname_id, phone_id, sat_id, sport_id, time_id, style_id, full_id, user_id):

        return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'STYLE'=? WHERE 'user_id' =?",(str(style_id), str(user_id),))
                    #def update_sub(self, user_id):#success
     #   """UPADATE"""
       # return self.cursor.execute("UPDATE 'databaseofazcamp' SET 'SAT'="+str(SAT)+" WHERE 'user_id' ="+str(user_id))

    def close(self):
        self.connection.close()
