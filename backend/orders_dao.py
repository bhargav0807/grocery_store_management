from datetime import datetime
import mysql
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    try:
        # Insert into `orders` table
        order_query = ("INSERT INTO orders "
                       "(customer_name, total, datetime) "
                       "VALUES (%s, %s, %s)")
        order_data = (order['customer_name'], order['grand_total'], datetime.now())

        cursor.execute(order_query, order_data)
        order_id = cursor.lastrowid
        print(f"Generated Order ID: {order_id}")  # Debugging

        if not order_id:
            raise ValueError("Failed to retrieve order_id")

        # Insert into `order_details` table
        order_details_query = ("INSERT INTO order_details "
                               "(order_id, product_id, quantity, total_price) "
                               "VALUES (%s, %s, %s, %s)")

        order_details_data = [
            (order_id, int(detail['product_id']), float(detail['quantity']), float(detail['total_price']))
            for detail in order['order_details']
        ]

        cursor.executemany(order_details_query, order_details_data)

        # Commit transaction
        connection.commit()
        return order_id

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()  # Rollback on error
        return None

    finally:
        cursor.close()  # Ensure cursor is closed properly

def get_order_details(connection, order_id):
    cursor = connection.cursor()

    query = "SELECT * from order_details where order_id = %s"

    query = "SELECT order_details.order_id, order_details.quantity, order_details.total_price, "\
            "products.name, products.price_per_unit FROM order_details LEFT JOIN products on " \
            "order_details.product_id = products.product_id where order_details.order_id = %s"

    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # append order details in each order
    for record in response:
        record['order_details'] = get_order_details(connection, record['order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(get_order_details(connection,4))
    # print(insert_order(connection, {
    #     'customer_name': 'dhaval',
    #     'total': '500',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))