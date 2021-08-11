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
            sql = "CREATE TABLE {} (id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, First_Name TEXT, Mid_Name TEXT, Last_Name TEXT, Mail_Addr TEXT, Mail_City TEXT, Mail_State TEXT, Mail_Zip TEXT, Contact_Name TEXT, Email1 TEXT, Last_Seen1 TEXT, Email2 TEXT, Last_Seen2 TEXT, Email3 TEXT, Last_Seen3 TEXT, Email4 TEXT, Last_Seen4 TEXT, Email5 TEXT, Last_Seen5 TEXT, Email6 TEXT, Last_Seen6 TEXT, Email7 TEXT, Last_Seen7 TEXT, Email8 TEXT, Last_Seen8 TEXT, Email9 TEXT, Last_Seen9 TEXT, Email10 TEXT, Last_Seen10 TEXT, phone1 TEXT, dnc1 TEXT, phone2 TEXT, dnc2 TEXT, phone3 TEXT, dnc3 TEXT, phone4 TEXT, dnc4 TEXT, phone5 TEXT, dnc5 TEXT, phone6 TEXT, dnc6 TEXT, phone7 TEXT, dnc7 TEXT, phone8 TEXT, dnc8 TEXT, phone9 TEXT, dnc9 TEXT, phone10 TEXT, dnc10 TEXT, address1 TEXT, address2 TEXT, address3 TEXT, address4 TEXT, address5 TEXT, current_owername TEXT, tax_address TEXT, mail_address TEXT, recently_vacant TEXT, absentee_owner TEXT, municipal_name TEXT, zoning_code TEXT, range_code TEXT, section_code TEXT, coordinates TEXT, property_land_usage TEXT, assessors_parcel_number TEXT, business_property TEXT, property_type TEXT, buildings_on_parcel TEXT, building_type TEXT, stories TEXT, property_construction_quality TEXT, building_method TEXT, year_built TEXT, view_from_the_building TEXT, land_total TEXT, property_total TEXT, building_total TEXT, rooms_total TEXT, pool TEXT, garage_carport TEXT, sewer_system_type TEXT, roof_covering_type TEXT, heating TEXT, tax_amount_total TEXT, deed_type TEXT, sales_transaction_date TEXT, seller_name TEXT, sales_completion_date TEXT, sales_price TEXT, parcel_sale_type TEXT, last_assessment TEXT, sale_situation TEXT, mortgage_amount1 TEXT, mortgage_loan_type1 TEXT, mortgage_loan_to_value1 TEXT, mortgage_deep_type1 TEXT, mortgage_date1 TEXT, mortgage_term1 TEXT, mortgage_due_date1 TEXT, mortgage_lender_name1 TEXT, mortgage_amount2 TEXT, mortgage_loan_type2 TEXT, mortgage_loan_to_value2 TEXT, mortgage_deep_type2 TEXT, mortgage_date2 TEXT, mortgage_term2 TEXT, mortgage_due_date2 TEXT, mortgage_lender_name2 TEXT, mortgage_amount3 TEXT, mortgage_loan_type3 TEXT, mortgage_loan_to_value3 TEXT, mortgage_deep_type3 TEXT, mortgage_date3 TEXT, mortgage_term3 TEXT, mortgage_due_date3 TEXT, mortgage_lender_name3 TEXT, Identifier TEXT, CreatedTime TEXT, UpdatedTime TEXT, INDEX (Identifier))".format(table_name)

            mycursor.execute(sql)
            mydb.commit()


        sql = "SELECT Identifier FROM {0} WHERE Identifier='{1}'".format(table_name, documents[116])
        mycursor.execute(sql)
        identifier_result = mycursor.fetchone()

        if not identifier_result:
            print("MYSQL ADD")
            insert_sql = """INSERT INTO {} (First_Name, Mid_Name, Last_Name, Mail_Addr, Mail_City, Mail_State, Mail_Zip, Contact_Name, Email1, Last_Seen1, Email2, Last_Seen2, Email3, Last_Seen3, Email4, Last_Seen4, Email5, Last_Seen5, Email6, Last_Seen6, Email7, Last_Seen7, Email8, Last_Seen8, Email9, Last_Seen9, Email10, Last_Seen10, phone1, dnc1, phone2, dnc2, phone3, dnc3, phone4, dnc4, phone5, dnc5, phone6, dnc6, phone7, dnc7, phone8, dnc8, phone9, dnc9, phone10, dnc10, address1, address2, address3, address4, address5, current_owername, tax_address, mail_address, recently_vacant, absentee_owner, municipal_name, zoning_code, range_code, section_code, coordinates, property_land_usage, assessors_parcel_number, business_property, property_type, buildings_on_parcel, building_type, stories, property_construction_quality, building_method, year_built, view_from_the_building, land_total, property_total, building_total, rooms_total, pool, garage_carport, sewer_system_type, roof_covering_type, heating, tax_amount_total, deed_type, sales_transaction_date, seller_name, sales_completion_date, sales_price, parcel_sale_type, last_assessment, sale_situation, mortgage_amount1, mortgage_loan_type1, mortgage_loan_to_value1, mortgage_deep_type1, mortgage_date1, mortgage_term1, mortgage_due_date1, mortgage_lender_name1, mortgage_amount2, mortgage_loan_type2, mortgage_loan_to_value2, mortgage_deep_type2, mortgage_date2, mortgage_term2, mortgage_due_date2, mortgage_lender_name2, mortgage_amount3, mortgage_loan_type3, mortgage_loan_to_value3, mortgage_deep_type3, mortgage_date3, mortgage_term3, mortgage_due_date3, mortgage_lender_name3, Identifier, CreatedTime, UpdatedTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(table_name)

            mycursor.execute(insert_sql, documents)
            mydb.commit()

        else:
            print("MYSQL UPDATE")
            
            update_sql = 'UPDATE {0} SET First_Name="{1}", Mid_Name="{2}", Last_Name="{3}", Mail_Addr="{4}", Mail_City="{5}", Mail_State="{6}", Mail_Zip="{7}", Contact_Name="{8}", Email1="{9}", Last_Seen1="{10}", Email2="{11}", Last_Seen2="{12}", Email3="{13}", Last_Seen3="{14}", Email4="{15}", Last_Seen4="{16}", Email5="{17}", Last_Seen5="{18}", Email6="{19}", Last_Seen6="{20}", Email7="{21}", Last_Seen7="{22}", Email8="{23}", Last_Seen8="{24}", Email9="{25}", Last_Seen9="{26}", Email10="{27}", Last_Seen10="{28}", phone1="{29}", dnc1="{30}", phone2="{31}", dnc2="{32}", phone3="{33}", dnc3="{34}", phone4="{35}", dnc4="{36}", phone5="{37}", dnc5="{38}", phone6="{39}", dnc6="{40}", phone7="{41}", dnc7="{42}", phone8="{43}", dnc8="{44}", phone9="{45}", dnc9="{46}", phone10="{47}", dnc10="{48}", address1="{49}", address2="{50}", address3="{51}", address4="{52}", address5="{53}", current_owername="{54}", tax_address="{55}", mail_address="{56}", recently_vacant="{57}", absentee_owner="{58}", municipal_name="{59}", zoning_code="{60}", range_code="{61}", section_code="{62}", coordinates="{63}", property_land_usage="{64}", assessors_parcel_number="{65}", business_property="{66}", property_type="{67}", buildings_on_parcel="{68}", building_type="{69}", stories="{70}", property_construction_quality="{71}", building_method="{72}", year_built="{73}", view_from_the_building="{74}", land_total="{75}", property_total="{76}", building_total="{77}", rooms_total="{78}", pool="{79}", garage_carport="{80}", sewer_system_type="{81}", roof_covering_type="{82}", heating="{83}", tax_amount_total="{84}", deed_type="{85}", sales_transaction_date="{86}", seller_name="{87}", sales_completion_date="{88}", sales_price="{89}", parcel_sale_type="{90}", last_assessment="{91}", sale_situation="{92}", mortgage_amount1="{93}", mortgage_loan_type1="{94}", mortgage_loan_to_value1="{95}", mortgage_deep_type1="{96}", mortgage_date1="{97}", mortgage_term1="{98}", mortgage_due_date1="{99}", mortgage_lender_name1="{100}", mortgage_amount2="{101}", mortgage_loan_type2="{102}", mortgage_loan_to_value2="{103}", mortgage_deep_type2="{104}", mortgage_date2="{105}", mortgage_term2="{106}", mortgage_due_date2="{107}", mortgage_lender_name2="{108}", mortgage_amount3="{109}", mortgage_loan_type3="{110}", mortgage_loan_to_value3="{111}", mortgage_deep_type3="{112}", mortgage_date3="{113}", mortgage_term3="{114}", mortgage_due_date3="{115}", mortgage_lender_name3="{116}", UpdatedTime="{117}" WHERE Identifier="{118}"'.format(table_name, documents[0], documents[1], documents[2], documents[3], documents[4], documents[5], documents[6], documents[7], documents[8], documents[9], documents[10], documents[11], documents[12], documents[13], documents[14], documents[15], documents[16], documents[17], documents[18], documents[19], documents[20], documents[21], documents[22], documents[23], documents[24], documents[25], documents[26], documents[27], documents[28], documents[29], documents[30], documents[31], documents[32], documents[33], documents[34], documents[35], documents[36], documents[37], documents[38], documents[39], documents[40], documents[41], documents[42], documents[43], documents[44], documents[45], documents[46], documents[47], documents[48], documents[49], documents[50], documents[51], documents[52], documents[53], documents[54], documents[55], documents[56], documents[57], documents[58], documents[59], documents[60], documents[61], documents[62], documents[63], documents[64], documents[65], documents[66], documents[67], documents[68], documents[69], documents[70], documents[71], documents[72], documents[73], documents[74], documents[75], documents[76], documents[77], documents[78], documents[79], documents[80], documents[81], documents[82], documents[83], documents[84], documents[85], documents[86], documents[87], documents[88], documents[89], documents[90], documents[91], documents[92], documents[93], documents[94], documents[95], documents[96], documents[97], documents[98], documents[99], documents[100], documents[101], documents[102], documents[103], documents[104], documents[105], documents[106], documents[107], documents[108], documents[109], documents[110], documents[111], documents[112], documents[113], documents[114], documents[115], datetime.datetime.now(), documents[116])
            print("Updated")
            mycursor.execute(update_sql)
        
            mydb.commit()
            print("==================> Now time:", datetime.datetime.now())