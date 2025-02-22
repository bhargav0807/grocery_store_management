# Grocery Management System

## Overview
The Grocery Management System is a web application designed to manage grocery store operations efficiently. The system allows users to view products, manage inventory, and handle customer orders. The backend is built using **Flask** and **MySQL**, while the frontend utilizes **HTML, CSS, JavaScript, and Bootstrap**.

## Technologies Used
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap

## Database Structure
The project uses **four tables** in MySQL:
1. **orders** - Stores customer orders
2. **order_details** - Stores details of products in each order
3. **products** - Stores product details
4. **uom (Unit of Measurement)** - Stores unit of measurement for products

## Features
- **View Products**: Fetch and display available products
- **Manage Inventory**: Add, update, and delete products
- **Order Processing**: Place new orders and view order history
- **Unit of Measurement Management**: Manage different measurement units
- **Cross-Origin Support**: APIs include CORS headers for frontend integration

## API Endpoints
### 1. Product Management
- `GET /getProducts` - Fetch all products
- `POST /insertProduct` - Insert a new product
- `POST /deleteProduct` - Delete a product

### 2. Order Management
- `GET /getAllOrders` - Fetch all orders
- `POST /insertOrder` - Insert a new order

### 3. Unit of Measurement
- `GET /getUOM` - Fetch all units of measurement
