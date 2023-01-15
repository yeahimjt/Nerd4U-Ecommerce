import mysql.connector

db = mysql.connector.connect(user="jtmoney", password="HelpHimRnPlz1327!", host="nerd4u-ecommerce-database.mysql.database.azure.com", port=3306, database="nerd4u")

TABLE_NAME = "product_information"

    #########################################
    ## Queries Database for products that  ##
    ## have specified category.            ##
    #########################################   
def Get_Product_By_UID(uid):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product_information where seller_id = '{}'".format(uid))
    new_array = cursor.fetchall()
    return (new_array)
def Get_Product_By_Catagory(category):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM product_information where catagory = '" + category + "'")
    array = cursor.fetchall()
    return (array)
def Get_Product_By_Pid(pid):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product_information where PID = '{}'".format(pid))
    new_array = cursor.fetchone()
    return (new_array)
def Get_Product_By_Category_If_Valid(array, category):
    cursor = db.cursor()
    # make a new string with spliced list
    
    cursor.execute("SELECT * FROM product_information where catagory like '%" + category + "%' AND  tags like '%" + str(array[0][10]) + "%'")
    new_array = cursor.fetchall()
    return (new_array)

def Get_Product_By_Tag(tag):
    cursor = db.cursor()

    tag = str(tag)

    cursor.execute("SELECT * FROM product_information where tags like '%" + tag + "%' or catagory like '%" + tag + "%' or name like '%" + tag +"%'")
    array = cursor.fetchall()
    return (array)
def Get_Product_By_Tag_Only(tag):
    cursor = db.cursor()
    print(tag)
    cursor.execute("SELECT * FROM product_information where tags like '%" + tag + "%'")
    array = cursor.fetchall()
    return (array)

def Get_Product_By_SubCategory_Only(subcategory):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product_information where sub_category like '%" + subcategory + "%'")
    array = cursor.fetchall()
    return (array)

def Get_Product_By_SubCategory(subcategory,title):
    cursor = db.cursor()
    test = "" + str(title) + ""
    cursor.execute("SELECT * FROM product_information where sub_category like '%" + subcategory + "%' AND  name like '" + test + "'")
    array = cursor.fetchall()
    return (array)

def Insert_New_Product(uid,list_of_tags,title,description, image,price,quantity,catagory,subcategory):
    
    cursor = db.cursor()

    sql="INSERT INTO product_information (name, price, picture, seller_id, description, quantity, remaining_items, catagory, sub_category, tags) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    #### CHANGE PRICE (DOLLAR) TO ACTUAL SUM OF DOLLAR + CENT
    val = (title, price, image, uid, description, quantity, quantity, catagory, subcategory, str(list_of_tags))
    cursor.execute(sql,val)
    db.commit()

def strArrayToArray(array):
    new_array = []
    array = array[1:-1]
    array = array.split(',')
    for i in range(0,len(array)):
        array[i] = array[i].strip()
        new_array.append(array[i].strip("'"))
        print(new_array[i])
    return new_array