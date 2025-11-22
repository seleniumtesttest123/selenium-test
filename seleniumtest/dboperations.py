# insert, update, delete
import mysql.connector

insert_query = "insert into student value(104,'Kim',60)"
update_query = "update student set sname='Mary' where sno=104"
delete_query = "delete from student where sno=104"

try:
    con = mysql.connector.connect(
        host="localhost", port=3306, user="root", passwd="root", database="mydb"
    )
    curs = con.cursor()
    curs.execute(delete_query)
    con.commit()
    con.close()
except:
    print("connection unsuccessful...")

print("finished.....")
