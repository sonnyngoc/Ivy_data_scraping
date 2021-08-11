import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv, time, re, datetime, hashlib

from insertdatabase_update import InsertDB

# table_name = "ivy_skiptrace_data"
table_name = "ivy_July12"

def wait(broswer, xpath):
    WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))

def auto_process(htmlstring, driver):
    
    print("-------------Start Processing--------------")

    email = "dan@dannomajr.com"
    pwd = "$Baxter12"

    # email_input = driver.find_element_by_name("email")
    email_input = driver.find_element_by_id("login_email")
    email_input.send_keys(email)
    time.sleep(0.3)
    
    # pwd_input = driver.find_element_by_name("password")
    pwd_input = driver.find_element_by_id("login_password")
    pwd_input.send_keys(pwd)
    time.sleep(0.3)
    
    # login_btn = driver.find_element_by_xpath("//button[@data-userflow-id='sign-in-submit']")
    login_btn = driver.find_element_by_xpath("//button[contains(@class, 'ant-btn') and contains(@class, 'ant-btn-primary')]")
    login_btn.click()
    time.sleep(10)
    
    single_btn = driver.find_elements_by_xpath("//div[@class='ant-collapse-header']")
    single_btn[0].click()
    time.sleep(0.5)
    
    with open("Template(July12)_clean.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            print("-----------------------------------------> : ",  line_count)
            
            if line_count == 0:
                print("Read Headers")
                
            elif line_count > 885:
                
                f_name    = row[0]
                m_name    = row[1]
                l_name    = row[2]
                m_address = row[3]
                m_city    = row[4]
                m_state   = row[5]
                m_zipcode = row[6]
                m_faddress = m_address + ", " + m_city + ", " + m_state + ", " + m_zipcode
                
                data = {
                    "f_name"    : f_name,
                    "m_name"    : m_name,
                    "l_name"    : l_name,
                    "m_address" : m_address,
                    "m_city"    : m_city,
                    "m_state"   : m_state,
                    "m_zipcode" : m_zipcode
                }
                
                phone_data ={
                    "phone1" : "",
                    "dnc1" : "",
                    "phone2" : "",
                    "dnc2" : "",
                    "phone3" : "",
                    "dnc3" : "",
                    "phone4" : "",
                    "dnc4" : "",
                    "phone5" : "",
                    "dnc5" : "",
                    "phone6" : "",
                    "dnc6" : "",
                    "phone7" : "",
                    "dnc7" : "",
                    "phone8" : "",
                    "dnc8" : "",
                    "phone9" : "",
                    "dnc9" : "",
                    "phone10" : "",
                    "dnc10" : ""
                }
                
                email_data = {
                    "email1" : "",
                    "lastseen1" : "",
                    "email2" : "",
                    "lastseen2" : "",
                    "email3" : "",
                    "lastseen3" : "",
                    "email4" : "",
                    "lastseen4" : "",
                    "email5" : "",
                    "lastseen5" : "",
                    "email6" : "",
                    "lastseen6" : "",
                    "email7" : "",
                    "lastseen7" : "",
                    "email8" : "",
                    "lastseen8" : "",
                    "email9" : "",
                    "lastseen9" : "",
                    "email10" : "",
                    "lastseen10" : "",
                }
                
                address_data = {
                    "address1" : "",
                    "address2" : "",
                    "address3" : "",
                    "address4" : "",
                    "address5" : ""
                }
                
                mortgage_data = {
                    "amount1" : "",
                    "loan_type1" : "",
                    "loan_to_value1" : "",
                    "deep_type1" : "",
                    "date1" : "",
                    "term1" : "",
                    "due_date1" : "",
                    "lender_name1" : "",
                    "amount2" : "",
                    "loan_type2" : "",
                    "loan_to_value2" : "",
                    "deep_type2" : "",
                    "date2" : "",
                    "term2" : "",
                    "due_date2" : "",
                    "lender_name2" : "",
                    "amount3" : "",
                    "loan_type3" : "",
                    "loan_to_value3" : "",
                    "deep_type3" : "",
                    "date3" : "",
                    "term3" : "",
                    "due_date3" : "",
                    "lender_name3" : "",
                }
                
                print("First Name--------------> : ", f_name)
                print("Last Name---------------> : ", l_name)
                print("M Address---------------> : ", m_address)
                print("M City------------------> : ", m_city)
                print("M State-----------------> : ", m_state)
                print("M Zipcode---------------> : ", m_zipcode)
                print("M Full Address----------> : ", m_faddress)
                
                try:
                    wait(driver, "//input[@data-cy='searchRequest-fname']")
                except:
                    print("There is no xpath")
                
                # input_fname = driver.find_element_by_id("__first-name-input__")
                # input_fname = driver.find_element_by_xpath("//input[@data-cy='single-fname']")
                input_fname = driver.find_element_by_xpath("//input[@data-cy='searchRequest-fname']")
                input_fname.send_keys(f_name)
                # input_fname.send_keys("Adrian")
                time.sleep(0.1)
                
                # input_lname = driver.find_element_by_id("__last-name-input__")
                # input_lname = driver.find_element_by_xpath("//input[@data-cy='single-lname']")
                input_lname = driver.find_element_by_xpath("//input[@data-cy='searchRequest-lname']")
                input_lname.send_keys(l_name)
                # input_lname.send_keys("Carranza")
                time.sleep(0.1)
                
                # input_faddress = driver.find_element_by_id("__full-address-input__")
                input_faddress = driver.find_element_by_xpath("//input[@data-cy='map-search']")
                input_faddress.send_keys(m_faddress)
                # input_faddress.send_keys("8708 W C P HAYES DR,TOLLESON,AZ,85353")
                time.sleep(5)
                
                try:
                    # driver.find_element_by_xpath("//ul[contains(@class, 'kf6xmg-4') and contains(@class, 'gumXwT')]/li[1]").click()
                    driver.find_element_by_xpath("//div[@class='rc-virtual-list-holder-inner']//div[1]").click()
                    
                    # driver.find_element_by_xpath("//div[@data-cy='map-result-0']").click()
                    time.sleep(3)
                    
                    # search_btn = driver.find_element_by_xpath("//button[@data-userflow-id='sgl-search']")
                    # mydb_btn = driver.find_element_by_xpath("//button[@data-cy='single-lookup-button']")
                    # mydb_btn.click()
                    # time.sleep(4)
                    
                    match_btn = driver.find_element_by_xpath("//button[@data-cy='match-confirm-button']")
                    match_btn.click()
                    time.sleep(20)
                    
                    try:
                        valid_data = driver.find_element_by_xpath("//span[contains(@class, 'sc-fzoNJl') and contains(@class, 'bKfsfp')]").text
                    
                        print("No Data Available")
                        final_data = {
                            "f_name"       : data["f_name"],
                            "m_name"       : data["m_name"],
                            "l_name"       : data["l_name"],
                            "m_address"    : data["m_address"],
                            "m_city"       : data["m_city"],
                            "m_state"      : data["m_state"],
                            "m_zipcode"    : data["m_zipcode"],
                            "contact_name" : "",
                            "email1"       : email_data["email1"],
                            "lastseen1"    : email_data["lastseen1"],
                            "email2"       : email_data["email2"],
                            "lastseen2"    : email_data["lastseen2"],
                            "email3"       : email_data["email3"],
                            "lastseen3"    : email_data["lastseen3"],
                            "email4"       : email_data["email4"],
                            "lastseen4"    : email_data["lastseen4"],
                            "email5"       : email_data["email5"],
                            "lastseen5"    : email_data["lastseen5"],
                            "email6"       : email_data["email6"],
                            "lastseen6"    : email_data["lastseen6"],
                            "email7"       : email_data["email7"],
                            "lastseen7"    : email_data["lastseen7"],
                            "email8"       : email_data["email8"],
                            "lastseen8"    : email_data["lastseen8"],
                            "email9"       : email_data["email9"],
                            "lastseen9"    : email_data["lastseen9"],
                            "email10"      : email_data["email10"],
                            "lastseen10"   : email_data["lastseen10"],
                            "phone1"       : phone_data["phone1"],
                            "dnc1"         : phone_data["dnc1"],
                            "phone2"       : phone_data["phone2"],
                            "dnc2"         : phone_data["dnc2"],
                            "phone3"       : phone_data["phone3"],
                            "dnc3"         : phone_data["dnc3"],
                            "phone4"       : phone_data["phone4"],
                            "dnc4"         : phone_data["dnc4"],
                            "phone5"       : phone_data["phone5"],
                            "dnc5"         : phone_data["dnc5"],
                            "phone6"       : phone_data["phone6"],
                            "dnc6"         : phone_data["dnc6"],
                            "phone7"       : phone_data["phone7"],
                            "dnc7"         : phone_data["dnc7"],
                            "phone8"       : phone_data["phone8"],
                            "dnc8"         : phone_data["dnc8"],
                            "phone9"       : phone_data["phone9"],
                            "dnc9"         : phone_data["dnc9"],
                            "phone10"      : phone_data["phone10"],
                            "dnc10"        : phone_data["dnc10"],
                            "address1"     : address_data["address1"],
                            "address2"     : address_data["address2"],
                            "address3"     : address_data["address3"],
                            "address4"     : address_data["address4"],
                            "address5"     : address_data["address5"],
                            "current_owername" : "",
                            "tax_address"      : "",
                            "mail_address"     : "",
                            "recently_vacant"  : "",
                            "absentee_owner"   : "",
                            "municipal_name"   : "",
                            "zoning_code"      : "",
                            "range_code"       : "",
                            "section_code"     : "",
                            "coordinates"      : "",
                            "property_land_usage"     : "",
                            "assessors_parcel_number" : "",
                            "business_property"       : "",
                            "property_type"           : "",
                            "buildings_on_parcel"     : "",
                            "building_type"           : "",
                            "stories"                 : "",
                            "property_construction_quality" : "",
                            "building_method"         : "",
                            "year_built"              : "",
                            "view_from_the_building"  : "",
                            "land_total"              : "",
                            "property_total"          : "",
                            "building_total"          : "",
                            "rooms_total"             : "",
                            "pool"                    : "",
                            "garage_carport"          : "",
                            "sewer_system_type"       : "",
                            "roof_covering_type"      : "",
                            "heating"                 : "",
                            "tax_amount_total"        : "",
                            "deed_type"               : "",
                            "sales_transaction_date"  : "",
                            "seller_name"             : "",
                            "sales_completion_date"   : "",
                            "sales_price"             : "",
                            "parcel_sale_type"        : "",
                            "last_assessment"         : "",
                            "sale_situation"          : "",
                            "mortgage_amount1"        : mortgage_data["amount1"],
                            "mortgage_loan_type1"     : mortgage_data["loan_type1"],
                            "mortgage_loan_to_value1" : mortgage_data["loan_to_value1"],
                            "mortgage_deep_type1"     : mortgage_data["deep_type1"],
                            "mortgage_date1"          : mortgage_data["date1"],
                            "mortgage_term1"          : mortgage_data["term1"],
                            "mortgage_due_date1"      : mortgage_data["due_date1"],
                            "mortgage_lender_name1"   : mortgage_data["lender_name1"],
                            "mortgage_amount2"        : mortgage_data["amount1"],
                            "mortgage_loan_type2"     : mortgage_data["loan_type2"],
                            "mortgage_loan_to_value2" : mortgage_data["loan_to_value2"],
                            "mortgage_deep_type2"     : mortgage_data["deep_type2"],
                            "mortgage_date2"          : mortgage_data["date2"],
                            "mortgage_term2"          : mortgage_data["term2"],
                            "mortgage_due_date2"      : mortgage_data["due_date2"],
                            "mortgage_lender_name2"   : mortgage_data["lender_name2"],
                            "mortgage_amount3"        : mortgage_data["amount3"],
                            "mortgage_loan_type3"     : mortgage_data["loan_type3"],
                            "mortgage_loan_to_value3" : mortgage_data["loan_to_value3"],
                            "mortgage_deep_type3"     : mortgage_data["deep_type3"],
                            "mortgage_date3"          : mortgage_data["date3"],
                            "mortgage_term3"          : mortgage_data["term3"],
                            "mortgage_due_date3"      : mortgage_data["due_date3"],
                            "mortgage_lender_name3"   : mortgage_data["lender_name3"],
                        }
                        
                        db_insert(final_data)
                        
                    except:        
                        print("Data Available")
                        parse_information(driver.page_source, driver, data, phone_data, email_data, address_data, mortgage_data)
                        
                    back_btn = driver.find_element_by_xpath("//span[contains(@class, 'anticon') and contains(@class, 'anticon-arrow-left')]")
                    back_btn.click()
                    time.sleep(0.5)
                        
                except:
                    print("No Matching Address")
                    final_data = {
                        "f_name"       : data["f_name"],
                        "m_name"       : data["m_name"],
                        "l_name"       : data["l_name"],
                        "m_address"    : data["m_address"],
                        "m_city"       : data["m_city"],
                        "m_state"      : data["m_state"],
                        "m_zipcode"    : data["m_zipcode"],
                        "contact_name" : "",
                        "email1"       : email_data["email1"],
                        "lastseen1"    : email_data["lastseen1"],
                        "email2"       : email_data["email2"],
                        "lastseen2"    : email_data["lastseen2"],
                        "email3"       : email_data["email3"],
                        "lastseen3"    : email_data["lastseen3"],
                        "email4"       : email_data["email4"],
                        "lastseen4"    : email_data["lastseen4"],
                        "email5"       : email_data["email5"],
                        "lastseen5"    : email_data["lastseen5"],
                        "email6"       : email_data["email6"],
                        "lastseen6"    : email_data["lastseen6"],
                        "email7"       : email_data["email7"],
                        "lastseen7"    : email_data["lastseen7"],
                        "email8"       : email_data["email8"],
                        "lastseen8"    : email_data["lastseen8"],
                        "email9"       : email_data["email9"],
                        "lastseen9"    : email_data["lastseen9"],
                        "email10"      : email_data["email10"],
                        "lastseen10"   : email_data["lastseen10"],
                        "phone1"       : phone_data["phone1"],
                        "dnc1"         : phone_data["dnc1"],
                        "phone2"       : phone_data["phone2"],
                        "dnc2"         : phone_data["dnc2"],
                        "phone3"       : phone_data["phone3"],
                        "dnc3"         : phone_data["dnc3"],
                        "phone4"       : phone_data["phone4"],
                        "dnc4"         : phone_data["dnc4"],
                        "phone5"       : phone_data["phone5"],
                        "dnc5"         : phone_data["dnc5"],
                        "phone6"       : phone_data["phone6"],
                        "dnc6"         : phone_data["dnc6"],
                        "phone7"       : phone_data["phone7"],
                        "dnc7"         : phone_data["dnc7"],
                        "phone8"       : phone_data["phone8"],
                        "dnc8"         : phone_data["dnc8"],
                        "phone9"       : phone_data["phone9"],
                        "dnc9"         : phone_data["dnc9"],
                        "phone10"      : phone_data["phone10"],
                        "dnc10"        : phone_data["dnc10"],
                        "address1"     : address_data["address1"],
                        "address2"     : address_data["address2"],
                        "address3"     : address_data["address3"],
                        "address4"     : address_data["address4"],
                        "address5"     : address_data["address5"],
                        "current_owername" : "",
                        "tax_address"      : "",
                        "mail_address"     : "",
                        "recently_vacant"  : "",
                        "absentee_owner"   : "",
                        "municipal_name"   : "",
                        "zoning_code"      : "",
                        "range_code"       : "",
                        "section_code"     : "",
                        "coordinates"      : "",
                        "property_land_usage"     : "",
                        "assessors_parcel_number" : "",
                        "business_property"       : "",
                        "property_type"           : "",
                        "buildings_on_parcel"     : "",
                        "building_type"           : "",
                        "stories"                 : "",
                        "property_construction_quality" : "",
                        "building_method"         : "",
                        "year_built"              : "",
                        "view_from_the_building"  : "",
                        "land_total"              : "",
                        "property_total"          : "",
                        "building_total"          : "",
                        "rooms_total"             : "",
                        "pool"                    : "",
                        "garage_carport"          : "",
                        "sewer_system_type"       : "",
                        "roof_covering_type"      : "",
                        "heating"                 : "",
                        "tax_amount_total"        : "",
                        "deed_type"               : "",
                        "sales_transaction_date"  : "",
                        "seller_name"             : "",
                        "sales_completion_date"   : "",
                        "sales_price"             : "",
                        "parcel_sale_type"        : "",
                        "last_assessment"         : "",
                        "sale_situation"          : "",
                        "mortgage_amount1"        : mortgage_data["amount1"],
                        "mortgage_loan_type1"     : mortgage_data["loan_type1"],
                        "mortgage_loan_to_value1" : mortgage_data["loan_to_value1"],
                        "mortgage_deep_type1"     : mortgage_data["deep_type1"],
                        "mortgage_date1"          : mortgage_data["date1"],
                        "mortgage_term1"          : mortgage_data["term1"],
                        "mortgage_due_date1"      : mortgage_data["due_date1"],
                        "mortgage_lender_name1"   : mortgage_data["lender_name1"],
                        "mortgage_amount2"        : mortgage_data["amount1"],
                        "mortgage_loan_type2"     : mortgage_data["loan_type2"],
                        "mortgage_loan_to_value2" : mortgage_data["loan_to_value2"],
                        "mortgage_deep_type2"     : mortgage_data["deep_type2"],
                        "mortgage_date2"          : mortgage_data["date2"],
                        "mortgage_term2"          : mortgage_data["term2"],
                        "mortgage_due_date2"      : mortgage_data["due_date2"],
                        "mortgage_lender_name2"   : mortgage_data["lender_name2"],
                        "mortgage_amount3"        : mortgage_data["amount3"],
                        "mortgage_loan_type3"     : mortgage_data["loan_type3"],
                        "mortgage_loan_to_value3" : mortgage_data["loan_to_value3"],
                        "mortgage_deep_type3"     : mortgage_data["deep_type3"],
                        "mortgage_date3"          : mortgage_data["date3"],
                        "mortgage_term3"          : mortgage_data["term3"],
                        "mortgage_due_date3"      : mortgage_data["due_date3"],
                        "mortgage_lender_name3"   : mortgage_data["lender_name3"],
                    }
                        
                    db_insert(final_data)
                
                    input_fname.send_keys(Keys.CONTROL, 'a')
                    input_fname.send_keys(Keys.DELETE)
                    
                    input_lname.send_keys(Keys.CONTROL, 'a')
                    input_lname.send_keys(Keys.DELETE)
                    
                    input_faddress.send_keys(Keys.CONTROL, 'a')
                    input_faddress.send_keys(Keys.DELETE)
                    
                    time.sleep(1)

            line_count += 1
            
def parse_information(htmlstring, driver, data, phone_data, email_data, address_data, mortgage_data):
    # phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', driver.page_source)
    
    #-------------------------Personal Information-------------------------#
    more_buttons = driver.find_elements_by_xpath("//div[@class='ant-card-extra']")
    for more_button in more_buttons:
        more_button.click()
        time.sleep(0.3)
    
    personal_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]")
    personal_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]")
    personal_info_element = driver.find_element_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]")
    
    contact_name = ""
    dnc_array = []
    address_array = []
    
    for personal_info_label, personal_info_txt in zip(personal_info_labels, personal_info_txts):
        personal_info_label = personal_info_label.text
        
        if "Name" == personal_info_label:
            contact_name = personal_info_txt.text
        elif "DNC" in personal_info_label:
            dnc = personal_info_txt.text
            dnc_array.append(dnc)
        elif "Address #" in personal_info_label:
            address = personal_info_txt.text
            address_array.append(address)
            

    print("Contact Name--------------------------> : ", contact_name)

    phones = re.findall(r'[\d]{3}-[\d]{3}-[\d]{4}', personal_info_element.text)
    print(phones)
    print(dnc_array)
    
    # emails = re.findall(r'[\w\.-]+@[\w\.-]+', personal_info_element.text)
    # email_last_seens = re.findall(r'[\d]{4}-[\d]{2}-[\d]{2}', personal_info_element.text)
    
    # for phone in range(1, len(phones) + 1):
    #     phone_data["phone{}".format(phone)] = phones[phone - 1]
    #     if len(dnc_array) != 0 :
    #         phone_data["dnc{}".format(phone)] = dnc_array[phone - 1]
    # phone_info_counts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]/div[4]//div[contains(@class, 'sc-fznzOf') and contains(@class, 'ftgBjv')]")
    phone_info_counts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]/div[4]//div[contains(@class, 'sc-fznzOf')]")
    print(len(phone_info_counts))
    
    for p in range(1, len(phone_info_counts) + 1):
        # phone_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]/div[4]//div[contains(@class, 'sc-fznzOf') and contains(@class, 'ftgBjv')][{}]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]".format(p))
        # phone_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]/div[4]//div[contains(@class, 'sc-fznzOf') and contains(@class, 'ftgBjv')][{}]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]".format(p))
        
        phone_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]/div[4]//div[contains(@class, 'sc-fznzOf')][{}]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]".format(p))
        phone_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]/div[4]//div[contains(@class, 'sc-fznzOf')][{}]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]".format(p))

        for phone_info_label, phone_info_txt in zip(phone_info_labels, phone_info_txts):
            phone_info_label = phone_info_label.text
            if "Number" in phone_info_label or "Landline" in phone_info_label or "Mobile" in phone_info_label or "Phone" in phone_info_label:
                phone_data["phone{}".format(p)] = phone_info_txt.text
            elif "DNC" in phone_info_label:
                phone_data["dnc{}".format(p)] = phone_info_txt.text
            
        
    # for email in range(1, len(emails) + 1):
    #     if 'truepeople' not in emails[email - 1]:
    #         email_data["email{}".format(email)] = emails[email - 1]
    #         email_data["lastseen{}".format(email)] = email_last_seens[email - 1]
            
    for address in range(1, len(address_array) + 1):
        address_data["address{}".format(address)] = address_array[address - 1]
        
    # email_info_counts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//div[contains(@class, 'sc-fznzOf') and contains(@class, 'ftgBjv')]")
    email_info_counts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//div[contains(@class, 'sc-fznzOf')]")
    print(len(email_info_counts))
    
    for e in range(1, len(email_info_counts)):
        # email_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//div[contains(@class, 'sc-fznzOf') and contains(@class, 'ftgBjv')][{}]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]".format(e))
        # email_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//div[contains(@class, 'sc-fznzOf') and contains(@class, 'ftgBjv')][{}]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]".format(e))

        email_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//div[contains(@class, 'sc-fznzOf')][{}]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]".format(e))
        email_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][1]//div[contains(@class, 'sc-fznzOf')][{}]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]".format(e))
        
        for email_info_label, email_info_txt in zip(email_info_labels, email_info_txts):
            email_info_label = email_info_label.text
            if "Email" in email_info_label:
                email_data["email{}".format(e)] = email_info_txt.text
            elif "Last Seen" in email_info_label:
                email_data["lastseen{}".format(e)] = email_info_txt.text
            
                
                

    
    #-------------------------Location and Ownership---------------------#
    
    current_owername = ""
    tax_address = ""
    mail_address = ""
    recently_vacant = ""
    absentee_owner = ""
    
    municipal_name = ""
    zoning_code = ""
    range_code = ""
    section_code = ""
    coordinates = ""
    property_land_usage = ""
    assessors_parcel_number = ""
    
    business_property = ""
    property_type = ""
    buildings_on_parcel = ""
    building_type = ""
    stories = ""
    property_construction_quality = ""
    building_method = ""
    
    current_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][2]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]")
    current_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][2]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]")
    
    for current_info_label, current_info_txt in zip(current_info_labels, current_info_txts):
        current_info_label = current_info_label.text
        #-----------------Current Owner Information-------------------#
        if "Name" == current_info_label:
            current_owername = current_info_txt.text
        elif "Tax Address" in current_info_label:
            tax_address = current_info_txt.text
        elif "Mail Address" in current_info_label:
            mail_address = current_info_txt.text
        elif "Recently Vacant" in current_info_label:
            recently_vacant = current_info_txt.text
        elif "Absentee Owner" in current_info_label:
            absentee_owner = current_info_txt.text
        #---------------Property Location Information----------------#
        elif "Municipal Name" in current_info_label:
            municipal_name = current_info_txt.text
        elif "Zoning Code" in current_info_label:
            zoning_code = current_info_txt.text
        elif "Range Code" in current_info_label:
            range_code = current_info_txt.text
        elif "Section Code" in current_info_label:
            section_code = current_info_txt.text
        elif "Coordinates" in current_info_label:
            coordinates = current_info_txt.text
        elif "Property Land Usage" in current_info_label:
            property_land_usage = current_info_txt.text
        elif "Parcel Number" in current_info_label:
            assessors_parcel_number = current_info_txt.text
        #------------Property OwnerShip-----------------------------#
        elif "Business Property" in current_info_label:
            business_property = current_info_txt.text
        elif "Property Type" in current_info_label:
            property_type = current_info_txt.text
        elif "Buildings on Parcel" in current_info_label:
            buildings_on_parcel = current_info_txt.text
        elif "Building Type" in current_info_label:
            building_type = current_info_txt.text
        elif "Stories" in current_info_label:
            stories = current_info_txt.text
        elif "Property Construction Quality" in current_info_label:
            property_construction_quality = current_info_txt.text
        elif "Building Method" in current_info_label:
            building_method = current_info_txt.text
            
            
    #-------------------------Location and Ownership---------------------#
    
    year_built = ""
    view_from_the_building = ""
    land_total = ""
    property_total = ""
    building_total = ""
    rooms_total = ""
    pool = ""
    garage_carport = ""
    sewer_system_type = ""
    roof_covering_type = ""
    heating = ""
    
    additional_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][3]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]")
    additional_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][3]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]")
    
    for additional_info_label, additional_info_txt in zip(additional_info_labels, additional_info_txts):
        additional_info_label = additional_info_label.text
        #----------------------Property Attributes Info---------------#
        if "Year Built" in additional_info_label:
            year_built = additional_info_txt.text
        elif "View from the building" in additional_info_label:
            view_from_the_building = additional_info_txt.text
        elif "Land Total" in additional_info_label:
            land_total = additional_info_txt.text
        elif "Property, Total" in additional_info_label:
            property_total = additional_info_txt.text
        elif "Building, Total" in additional_info_label:
            building_total = additional_info_txt.text
        #-------------------Property Details--------------------------#
        elif "Rooms, Total" in additional_info_label:
            rooms_total = additional_info_txt.text
        elif "Pool" == additional_info_label:
            pool = additional_info_txt.text
        elif "Garage/Carport" in additional_info_label:
            garage_carport = additional_info_txt.text
        elif "Sewer System Type" in additional_info_label:
            sewer_system_type = additional_info_txt.text
        elif "Roof Covering Type" in additional_info_label:
            roof_covering_type = additional_info_txt.text
        elif "Heating" in additional_info_label:
            heating = additional_info_txt.text
    
    
    #---------------------- Deed, Sales and Mortage--------------------#
    tax_amount_total = ""
    deed_type = ""
    sales_transaction_date = ""
    seller_name = ""
    sales_completion_date = ""
    sales_price = ""
    parcel_sale_type = ""
    last_assessment = ""
    sale_situation = ""
    
    sales_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][4]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]")
    sales_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][4]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]")
    
    for sales_info_label, sales_info_txt in zip(sales_info_labels, sales_info_txts):
        sales_info_label = sales_info_label.text
        #-----------------Assessor/Deed Information--------------#
        if "Tax amount, total" in sales_info_label:
            tax_amount_total = sales_info_txt.text
        elif "Deed type" in sales_info_label:
            deed_type = sales_info_txt.text
        elif "Sales transaction date" in sales_info_label:
            sales_transaction_date = sales_info_txt.text
        elif "Seller name" in sales_info_label:
            seller_name = sales_info_txt.text
        elif "Sales completion date" in sales_info_label:
            sales_completion_date = sales_info_txt.text
        elif "Sales price" in sales_info_label:
            sales_price = sales_info_txt.text
        elif "Parcel Sale Type" in sales_info_label:
            parcel_sale_type = sales_info_txt.text
        elif "Last assessment" in sales_info_label:
            last_assessment = sales_info_txt.text
        elif "Sale situation" in sales_info_label:
            sale_situation = sales_info_txt.text
            
    #---------------------Mortgage Information1---------------#
    mortgage_info_counts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][4]//div[contains(@class, 'sc-fzpkJw') and contains(@class, 'iZQcEX')]")
    print("#############", len(mortgage_info_counts))
    
    for i in range(1, len(mortgage_info_counts) + 1):
        
        mortgage_info_labels = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][4]//div[contains(@class, 'sc-fzpkJw') and contains(@class, 'iZQcEX')][{}]//span[contains(@class, 'sc-fzoKki') and contains(@class, 'gZQCqW')]".format(i))
        mortgage_info_txts = driver.find_elements_by_xpath("//div[contains(@class, 'ant-space-vertical')]//div[@class='ant-space-item'][4]//div[contains(@class, 'sc-fzpkJw') and contains(@class, 'iZQcEX')][{}]//span[contains(@class, 'sc-fzoYkl') and contains(@class, 'clZSGL')]".format(i))
        
        for mortgage_info_label, mortgage_info_txt in zip(mortgage_info_labels, mortgage_info_txts):
            mortgage_info_label = mortgage_info_label.text
            if "Amount" in mortgage_info_label:
                mortgage_data["amount{}".format(i)] = mortgage_info_txt.text
            elif "Loan type" in mortgage_info_label:
                mortgage_data["loan_type{}".format(i)] = mortgage_info_txt.text
            elif "Loan to value" in mortgage_info_label:
                mortgage_data["loan_to_value{}".format(i)] = mortgage_info_txt.text
            elif "Deep type" in mortgage_info_label:
                mortgage_data["deep_type{}".format(i)] = mortgage_info_txt.text
            elif "Date" == mortgage_info_label:
                mortgage_data["date{}".format(i)] = mortgage_info_txt.text
            elif "Term" == mortgage_info_label:
                mortgage_data["term{}".format(i)] = mortgage_info_txt.text
            elif "Due date" == mortgage_info_label:
                mortgage_data["due_date{}".format(i)] = mortgage_info_txt.text
            elif "Lender name" in mortgage_info_label:
                mortgage_data["lender_name{}".format(i)] = mortgage_info_txt.text
    
    print("First Name-----------------------> : ", data["f_name"])
    print("Middle Name----------------------> : ", data["m_name"])
    print("Last Name------------------------> : ", data["l_name"])
    print("M Address------------------------> : ", data["m_address"])
    print("M City---------------------------> : ", data["m_city"])
    print("M State--------------------------> : ", data["m_state"])
    print("M Zipcode------------------------> : ", data["m_zipcode"])
    print("#########################################################################")
    print("Contact Name-----------------------> : ", contact_name)
    print("Email Data-------------------------> : ", email_data)
    print("Phone Data-------------------------> : ", phone_data)
    print("Address Data-----------------------> : ", address_data)
    print("#########################################################################")
    print("Current Owner Name-----------------> : ", current_owername)
    print("Tax Address------------------------> : ", tax_address)
    print("Mail Address-----------------------> : ", mail_address)
    print("Recently Vavant--------------------> : ", recently_vacant)
    print("Absentee Owner---------------------> : ", absentee_owner)
    print("Municipal Name---------------------> : ", municipal_name)
    print("Zoning Code------------------------> : ", zoning_code)
    print("Range Code-------------------------> : ", range_code)
    print("Section Code-----------------------> : ", section_code)
    print("Coordinates------------------------> : ", coordinates)
    print("Property Land Usage----------------> : ", property_land_usage)
    print("Assessor`s Parcel Number-----------> : ", assessors_parcel_number)
    print("Business Property------------------> : ", business_property)
    print("Property Type----------------------> : ", property_type)
    print("Buildings on Parcel----------------> : ", buildings_on_parcel)
    print("Building Type----------------------> : ", building_type)
    print("Stories----------------------------> : ", stories)
    print("Property Construction Quality------> : ", property_construction_quality)
    print("Building Method--------------------> : ", building_method)
    print("#########################################################################")
    print("Year Built-------------------------> : ", year_built)
    print("View from the building-------------> : ", view_from_the_building)
    print("Land Total (sqft)------------------> : ", land_total)
    print("Property, Total (sqft)-------------> : ", property_total)
    print("Building, Total (sqft)-------------> : ", building_total)
    print("Rooms, Total-----------------------> : ", rooms_total)
    print("Pool-------------------------------> : ", pool)
    print("Garage/Carport---------------------> : ", garage_carport)
    print("Sewer System Type------------------> : ", sewer_system_type)
    print("Roof Covering Type-----------------> : ", roof_covering_type)
    print("Heating----------------------------> : ", heating)
    print("#########################################################################")
    print("Tax amount, total------------------> : ", tax_amount_total)
    print("Deed type--------------------------> : ", deed_type)
    print("Sales transaction date-------------> : ", sales_transaction_date)
    print("Seller name------------------------> : ", seller_name)
    print("Sales completion date--------------> : ", sales_completion_date)
    print("Sales price------------------------> : ", sales_price)
    print("Parcel Sale Type-------------------> : ", parcel_sale_type)
    print("Last assessment--------------------> : ", last_assessment)
    print("Sale situation---------------------> : ", sale_situation)
    print("#########################################################################")
    print("Mortgage Information---------------> : ", mortgage_data)
    
    
    final_data = {
        "f_name"       : data["f_name"],
        "m_name"       : data["m_name"],
        "l_name"       : data["l_name"],
        "m_address"    : data["m_address"],
        "m_city"       : data["m_city"],
        "m_state"      : data["m_state"],
        "m_zipcode"    : data["m_zipcode"],
        "contact_name" : contact_name,
        "email1"       : email_data["email1"],
        "lastseen1"    : email_data["lastseen1"],
        "email2"       : email_data["email2"],
        "lastseen2"    : email_data["lastseen2"],
        "email3"       : email_data["email3"],
        "lastseen3"    : email_data["lastseen3"],
        "email4"       : email_data["email4"],
        "lastseen4"    : email_data["lastseen4"],
        "email5"       : email_data["email5"],
        "lastseen5"    : email_data["lastseen5"],
        "email6"       : email_data["email6"],
        "lastseen6"    : email_data["lastseen6"],
        "email7"       : email_data["email7"],
        "lastseen7"    : email_data["lastseen7"],
        "email8"       : email_data["email8"],
        "lastseen8"    : email_data["lastseen8"],
        "email9"       : email_data["email9"],
        "lastseen9"    : email_data["lastseen9"],
        "email10"      : email_data["email10"],
        "lastseen10"   : email_data["lastseen10"],
        "phone1"       : phone_data["phone1"],
        "dnc1"         : phone_data["dnc1"],
        "phone2"       : phone_data["phone2"],
        "dnc2"         : phone_data["dnc2"],
        "phone3"       : phone_data["phone3"],
        "dnc3"         : phone_data["dnc3"],
        "phone4"       : phone_data["phone4"],
        "dnc4"         : phone_data["dnc4"],
        "phone5"       : phone_data["phone5"],
        "dnc5"         : phone_data["dnc5"],
        "phone6"       : phone_data["phone6"],
        "dnc6"         : phone_data["dnc6"],
        "phone7"       : phone_data["phone7"],
        "dnc7"         : phone_data["dnc7"],
        "phone8"       : phone_data["phone8"],
        "dnc8"         : phone_data["dnc8"],
        "phone9"       : phone_data["phone9"],
        "dnc9"         : phone_data["dnc9"],
        "phone10"      : phone_data["phone10"],
        "dnc10"        : phone_data["dnc10"],
        "address1"     : address_data["address1"],
        "address2"     : address_data["address2"],
        "address3"     : address_data["address3"],
        "address4"     : address_data["address4"],
        "address5"     : address_data["address5"],
        "current_owername" : current_owername,
        "tax_address"      : tax_address,
        "mail_address"     : mail_address,
        "recently_vacant"  : recently_vacant,
        "absentee_owner"   : absentee_owner,
        "municipal_name"   : municipal_name,
        "zoning_code"      : zoning_code,
        "range_code"       : range_code,
        "section_code"     : section_code,
        "coordinates"      : coordinates,
        "property_land_usage"     : property_land_usage,
        "assessors_parcel_number" : assessors_parcel_number,
        "business_property"       : business_property,
        "property_type"           : property_type,
        "buildings_on_parcel"     : buildings_on_parcel,
        "building_type"           : building_type,
        "stories"                 : stories,
        "property_construction_quality" : property_construction_quality,
        "building_method"         : building_method,
        "year_built"              : year_built,
        "view_from_the_building"  : view_from_the_building,
        "land_total"              : land_total,
        "property_total"          : property_total,
        "building_total"          : building_total,
        "rooms_total"             : rooms_total,
        "pool"                    : pool,
        "garage_carport"          : garage_carport,
        "sewer_system_type"       : sewer_system_type,
        "roof_covering_type"      : roof_covering_type,
        "heating"                 : heating,
        "tax_amount_total"        : tax_amount_total,
        "deed_type"               : deed_type,
        "sales_transaction_date"  : sales_transaction_date,
        "seller_name"             : seller_name,
        "sales_completion_date"   : sales_completion_date,
        "sales_price"             : sales_price,
        "parcel_sale_type"        : parcel_sale_type,
        "last_assessment"         : last_assessment,
        "sale_situation"          : sale_situation,
        "mortgage_amount1"        : mortgage_data["amount1"],
        "mortgage_loan_type1"     : mortgage_data["loan_type1"],
        "mortgage_loan_to_value1" : mortgage_data["loan_to_value1"],
        "mortgage_deep_type1"     : mortgage_data["deep_type1"],
        "mortgage_date1"          : mortgage_data["date1"],
        "mortgage_term1"          : mortgage_data["term1"],
        "mortgage_due_date1"      : mortgage_data["due_date1"],
        "mortgage_lender_name1"   : mortgage_data["lender_name1"],
        "mortgage_amount2"        : mortgage_data["amount1"],
        "mortgage_loan_type2"     : mortgage_data["loan_type2"],
        "mortgage_loan_to_value2" : mortgage_data["loan_to_value2"],
        "mortgage_deep_type2"     : mortgage_data["deep_type2"],
        "mortgage_date2"          : mortgage_data["date2"],
        "mortgage_term2"          : mortgage_data["term2"],
        "mortgage_due_date2"      : mortgage_data["due_date2"],
        "mortgage_lender_name2"   : mortgage_data["lender_name2"],
        "mortgage_amount3"        : mortgage_data["amount3"],
        "mortgage_loan_type3"     : mortgage_data["loan_type3"],
        "mortgage_loan_to_value3" : mortgage_data["loan_to_value3"],
        "mortgage_deep_type3"     : mortgage_data["deep_type3"],
        "mortgage_date3"          : mortgage_data["date3"],
        "mortgage_term3"          : mortgage_data["term3"],
        "mortgage_due_date3"      : mortgage_data["due_date3"],
        "mortgage_lender_name3"   : mortgage_data["lender_name3"]
    }
    
    db_insert(final_data)
 
    
def db_insert(final_data):
    data_base = []
    
    string_id = final_data["f_name"] + final_data["m_name"] + final_data["l_name"] + final_data["m_address"] + final_data["m_city"] + final_data["m_state"] + final_data["m_zipcode"] + final_data["contact_name"]
     
    m = hashlib.md5()
    m.update(string_id.encode('utf8'))
    identifier = m.hexdigest()
    create_time = str(datetime.datetime.now())
    update_time = ""
    
    insertdb = InsertDB()
    data_base.append((final_data["f_name"], final_data["m_name"], final_data["l_name"], final_data["m_address"], final_data["m_city"], final_data["m_state"], final_data["m_zipcode"], final_data["contact_name"], final_data["email1"], final_data["lastseen1"], final_data["email2"], final_data["lastseen2"], final_data["email3"], final_data["lastseen3"], final_data["email4"], final_data["lastseen4"], final_data["email5"], final_data["lastseen5"], final_data["email6"], final_data["lastseen6"], final_data["email7"], final_data["lastseen7"], final_data["email8"], final_data["lastseen8"], final_data["email9"], final_data["lastseen9"], final_data["email10"], final_data["lastseen10"], final_data["phone1"], final_data["dnc1"], final_data["phone2"], final_data["dnc2"], final_data["phone3"], final_data["dnc3"], final_data["phone4"], final_data["dnc4"], final_data["phone5"], final_data["dnc5"], final_data["phone6"], final_data["dnc6"], final_data["phone7"], final_data["dnc7"], final_data["phone8"], final_data["dnc8"], final_data["phone9"], final_data["dnc9"], final_data["phone10"], final_data["dnc10"], final_data["address1"], final_data["address2"], final_data["address3"], final_data["address4"], final_data["address5"], final_data["current_owername"], final_data["tax_address"], final_data["mail_address"], final_data["recently_vacant"], final_data["absentee_owner"], final_data["municipal_name"], final_data["zoning_code"], final_data["range_code"], final_data["section_code"], final_data["coordinates"], final_data["property_land_usage"], final_data["assessors_parcel_number"], final_data["business_property"], final_data["property_type"], final_data["buildings_on_parcel"], final_data["building_type"], final_data["stories"], final_data["property_construction_quality"], final_data["building_method"], final_data["year_built"], final_data["view_from_the_building"], final_data["land_total"], final_data["property_total"], final_data["building_total"], final_data["rooms_total"], final_data["pool"], final_data["garage_carport"], final_data["sewer_system_type"], final_data["roof_covering_type"], final_data["heating"], final_data["tax_amount_total"], final_data["deed_type"], final_data["sales_transaction_date"], final_data["seller_name"], final_data["sales_completion_date"], final_data["sales_price"], final_data["parcel_sale_type"], final_data["last_assessment"], final_data["sale_situation"], final_data["mortgage_amount1"], final_data["mortgage_loan_type1"], final_data["mortgage_loan_to_value1"], final_data["mortgage_deep_type1"], final_data["mortgage_date1"], final_data["mortgage_term1"], final_data["mortgage_due_date1"], final_data["mortgage_lender_name1"], final_data["mortgage_amount2"], final_data["mortgage_loan_type2"], final_data["mortgage_loan_to_value2"], final_data["mortgage_deep_type2"], final_data["mortgage_date2"], final_data["mortgage_term2"], final_data["mortgage_due_date2"], final_data["mortgage_lender_name2"], final_data["mortgage_amount3"], final_data["mortgage_loan_type3"], final_data["mortgage_loan_to_value3"], final_data["mortgage_deep_type3"], final_data["mortgage_date3"], final_data["mortgage_term3"], final_data["mortgage_due_date3"], final_data["mortgage_lender_name3"], identifier, create_time, update_time))
    
    insertdb.insert_document(data_base, table_name)
    
                
if __name__ == "__main__":
    options = Options()
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    path = "driver\\chromedriver.exe"
    driver = Chrome(executable_path=path, chrome_options = options)
    
    driver.get("https://app.getivydata.com/#/sign-in")
    
    driver.maximize_window()
    
    auto_process(driver.page_source, driver)