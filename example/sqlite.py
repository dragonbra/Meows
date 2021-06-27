import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('news.db')

    c = conn.cursor()
    print("Opened succefully")

    cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()