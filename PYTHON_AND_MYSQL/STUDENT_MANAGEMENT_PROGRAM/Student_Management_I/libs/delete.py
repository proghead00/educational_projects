# importing third party modules
import pymysql
import colorama
# importing local modules
import libs.banner
import libs.config


# class to delete an Entry
class delete():
    def __init__(self):
        self.dbhost = libs.config.dbhost
        self.dbname = libs.config.dbname
        self.dbuser = libs.config.dbuser
        self.dbpass = libs.config.dbpass
        try:
            self.conn = pymysql.connect(self.dbhost, self.dbuser, self.dbpass, self.dbname)
        except:
            print(colorama.Fore.LIGHTRED_EX, "\n[x] Error - UNABLE TO CONNECT TO DATABASE",
                  colorama.Fore.LIGHTYELLOW_EX, "\n[!] Info - Exiting")
            print(colorama.Style.RESET_ALL)  # resetting colors
            os._exit(1)
            pass

        self.cur = self.conn.cursor()
        pass

    # method for asking roll number to delete
    def get(self):
        libs.banner.banner()
        print("<--=[Delete Entry]=-->\n\n")
        self.roll_numbr = input("enter roll number you want to delete : ")
        pass

    # method for executing the Query
    def execute(self):
        sql = "DELETE FROM `stumanage_students` WHERE `roll_no`='{}'".format(self.roll_numbr) #sql statement
        try:
            self.cur.execute(sql) # executing sql
            self.conn.commit()  # committing changes
            print(colorama.Fore.LIGHTGREEN_EX, "\n[!] Success - Entry for {} has been deleted".format(self.roll_numbr))
        except: # on error
            self.conn.rollback() # rolling back the changes
            print(colorama.Fore.LIGHTRED_EX, "\n[x] Error - Can't Run Query".format(self.roll_numbr))
            pass
        pass

    # method for checking if roll_number exists or not
    def is_exists(self):
        sql = "SELECT 1 FROM `stumanage_students` WHERE `roll_no`='{}'".format(self.roll_numbr)
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            if len(data) < 1:
                return False
            return True
        except:
            self.conn.rollback()
            print(colorama.Fore.LIGHTRED_EX, "\n[x] Error - Can't Run Query")
            pass
        pass

    # method for closinng sql connection
    def destroy(self):
        self.conn.close()
        pass

    pass
