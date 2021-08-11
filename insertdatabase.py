import mysql.connector
import datetime

class InsertDB:
    
    mydb_name = "Dan_DB"

    def insert_document(self, documents, table_name):
        print(documents)

        # ************** DIGITAL SERVER ***************#
        mydb = mysql.connector.connect(
            user = "root",
            password = "",
            host = "localhost"
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS " + self.mydb_name + " CHARACTER SET utf8 COLLATE utf8_general_ci")

        # ********** DIGITAL OCEAN SERVER ***********#
        mydb = mysql.connector.connect(
            user = "root",
            password = "",
            host = "localhost",
            database = self.mydb_name
        )

        documents = documents[0]
        print(documents)

        mycursor = mydb.cursor()

        stmt = "SHOW TABLES LIKE '{}'".format(table_name)
        mycursor.execute(stmt)
        result = mycursor.fetchone()

        if not result:
            sql = "CREATE TABLE {} (id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(30), MidName VARCHAR(30), LastName VARCHAR(30), Mail_Addr VARCHAR(50), Mail_City VARCHAR(50), Mail_State VARCHAR(20), Mail_Zip VARCHAR(20), CurrentOwnerName_Ivy VARCHAR(50), PropertyAddress_Ivy VARCHAR(100), MailingAddress_Ivy VARCHAR(100), Phone1 VARCHAR(20), Phone2 VARCHAR(20), Phone3 VARCHAR(20), Phone4 VARCHAR(20), Phone5 VARCHAR(20), Phone6 VARCHAR(20), Phone7 VARCHAR(20), Phone8 VARCHAR(20), Phone9 VARCHAR(20), Phone10 VARCHAR(20), Email1 VARCHAR(30), Email2 VARCHAR(30), Email3 VARCHAR(30), Email4 VARCHAR(30), Email5 VARCHAR(30), Email6 VARCHAR(30), Email7 VARCHAR(30), Email8 VARCHAR(30), Email9 VARCHAR(30), Email10 VARCHAR(30), Identifier VARCHAR(100), CreatedTime VARCHAR(30), UpdatedTime VARCHAR(30), INDEX (Identifier))".format(table_name)

            mycursor.execute(sql)
            mydb.commit()


        sql = "SELECT Identifier FROM {0} WHERE Identifier='{1}'".format(table_name, documents[30])
        mycursor.execute(sql)
        identifier_result = mycursor.fetchone()

        if not identifier_result:
            print("MYSQL ADD")
            insert_sql = """INSERT INTO {} (FirstName, MidName, LastName, Mail_Addr, Mail_City, Mail_State, Mail_Zip, CurrentOwnerName_Ivy, PropertyAddress_Ivy, MailingAddress_Ivy, Phone1, Phone2, Phone3, Phone4, Phone5, Phone6, Phone7, Phone8, Phone9, Phone10, Email1, Email2, Email3, Email4, Email5, Email6, Email7, Email8, Email9, Email10, Identifier, CreatedTime, UpdatedTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(table_name)

            mycursor.execute(insert_sql, documents)
            mydb.commit()

        else:
            print("MYSQL UPDATE")
            
            update_sql = 'UPDATE {0} SET FirstName="{1}", MidName="{2}", LastName="{3}", Mail_Addr="{4}", Mail_City="{5}", Mail_State="{6}", Mail_Zip="{7}", CurrentOwnerName_Ivy="{8}", PropertyAddress_Ivy="{9}", MailingAddress_Ivy="{10}", Phone1="{11}", Phone2="{12}", Phone3="{13}", Phone4="{14}", Phone5="{15}", Phone6="{16}", Phone7="{17}", Phone8="{18}", Phone9="{19}", Phone10="{20}", Email1="{21}", Email2="{22}", Email3="{23}", Email4="{24}", Email5="{25}", Email6="{26}", Email7="{27}", Email8="{28}", Email9="{29}", Email10="{30}", UpdatedTime="{31}" WHERE Identifier="{32}"'.format(table_name, documents[0], documents[1], documents[2], documents[3], documents[4], documents[5], documents[6], documents[7], documents[8], documents[9], documents[10], documents[11], documents[12], documents[13], documents[14], documents[15], documents[16], documents[17], documents[18], documents[19], documents[20], documents[21], documents[22], documents[23], documents[24], documents[25], documents[26], documents[27], documents[28], documents[29], datetime.datetime.now(), documents[30])
            print("Updated")
            mycursor.execute(update_sql)
        
            mydb.commit()
            print("==================> Now time:", datetime.datetime.now())