```
PUC-Rio
Especialização em Desenvolvimento Fullstack
Disciplina: Desenvolvimento Back-end Avançado

Aluno: Rodrigo Alves Costa
```

# PUC-Rio  
**Especialização em Desenvolvimento Fullstack**  
**Disciplina: Desenvolvimento Back-end Avançado**  

Aluno: Rodrigo Alves Costa  

## Market Master: Address Management Service

The Market Master project consists of a set of microservices designed to manage different aspects of a supermarket e-commerce platform, providing a unified experience for users to shop from various stores in their city. The `mm-address` service is responsible for managing address information and integrating with external postal code services like ViaCEP to fetch address details automatically.

### Related Market Master Microservices:
- [mm-inventory](https://github.com/MarketMasterPlus/mm-inventory) — Inventory (available items) Management for Market Master
- [mm-product](https://github.com/MarketMasterPlus/mm-product) — Product (item registry) Management
- [mm-shopping-cart](https://github.com/MarketMasterPlus/mm-shopping-cart) — Shopping Cart Management
- [mm-customer](https://github.com/MarketMasterPlus/mm-customer) — Customer/User Management
- [mm-address](https://github.com/MarketMasterPlus/mm-address) — Address Management with External Call of ViaCEP API
- [mm-store](https://github.com/MarketMasterPlus/mm-store) — Store Management
- [mm-pact-broker](https://github.com/MarketMasterPlus/mm-pact-broker) — Supporting repo holding the Pact Broker for Contract tests
- [mm-ui](https://github.com/MarketMasterPlus/mm-ui) — UI for Market Master

---

## Quick Start

### Prerequisites
- **Docker** and **Docker Compose** are required to run this service.

### Steps to Run the Service
1. Clone the repository:  
   ```bash
   git clone https://github.com/MarketMasterPlus/mm-address
   ```
2. Navigate to the project directory:
   ```bash
   cd mm-address
   ```
3. Start the services with Docker Compose:

   ```bash
    docker-compose up -d
   ```
4. Access the Address Management API at:

    ```bash
    http://localhost:5700/mm-address
    ```

## Project Description

The `mm-address` microservice handles all address-related operations for Market Master, including creating, retrieving, updating, and deleting addresses. Additionally, it integrates with the ViaCEP API to allow users to look up address details based on the Brazilian postal code (CEP). This service is part of the Market Master ecosystem, providing accurate and efficient address management, which is essential for both customer and store interactions within the platform.

### Key Features
- **Address Management**: Provides API endpoints for creating, updating, retrieving, and deleting address records.
- **ViaCEP Integration**: Automatically fetches address details using the postal code (CEP) via an external API.
- **PostgreSQL Database**: Stores all address information, ensuring persistence and scalability.

---

## Docker Setup

The `docker-compose.yml` for this project configures the `mm-address` service along with a PostgreSQL database for persistence. To start the service using Docker, run:
    ```bash
      docker compose up -d
    ```

## API Endpoints

### Address Management:
- **GET /mm-address/**  
  Retrieves all addresses or allows for filtering via a query parameter (`q`).  
  Example:  
  ```bash
  curl http://localhost:5700/mm-address/?q=streetname
  ```
- **POST /mm-address/
  Creates a new address record by submitting a JSON payload.
  Example:
  ```bash
  curl -X POST http://localhost:5700/mm-address/ -H "Content-Type: application/json" -d '{"street": "Rua A", "city": "Patos", "state": "PB", "cep": "58700123"}'
  ```
- **GET /mm-address/{id}
  Retrieves an address by its unique identifier.
  Example:
  ```bash
  curl http://localhost:5700/mm-address/1
  ```
- **PUT /mm-address/{id}
  Updates an existing address by submitting a JSON payload with the updated data.
  Example:
  ```bash
  curl -X PUT http://localhost:5700/mm-address/1 -H "Content-Type: application/json" -d '{"city": "Patos Updated"}'
  ```
- **DELETE /mm-address/{id}
  Deletes an address by its unique identifier.
  Example:
  ```bash
  curl -X DELETE http://localhost:5700/mm-address/1
  ```
  
### ViaCEP API Integration:
- **GET /viacep/{cep}**  
  Fetches address information based on a Brazilian postal code (CEP) using the ViaCEP API.  
  Example:  
  ```bash
  curl http://localhost:5700/viacep/58700123
  ```
  
  This endpoint validates the postal code format and retrieves address information such as street, city, state, neighborhood, and complement from ViaCEP's external API.

---

## Running the Flask Application Locally

If you prefer to run the service without Docker, follow the steps below.

### Step 1: Install Dependencies

Make sure you have Python 3 and `pip` installed. Then, install the required dependencies:

  ```bash
    pip install -r requirements.txt
  ```

### Step 2: Configure Environment Variables

Create a `.env` file in the root of the project with the following content:


  ```bash
  FLASK_APP=app.py  
  FLASK_ENV=development  
  DATABASE_URL=postgresql://marketmaster:password@localhost:5432/marketmaster
  ```

### Step 3: Run the Application

With the environment variables set, you can run the Flask application:

  ```bash
  flask run
  ```

By default, the service will be accessible at `http://localhost:5700`.

---

## Additional Information

This microservice is part of the larger Market Master project, which aims to provide a scalable and flexible e-commerce platform for supermarkets. Address management is a key component, ensuring accurate delivery and user-friendly interactions when setting up delivery addresses.

For more details about the Market Master project and to explore other microservices, visit the respective repositories:

- [mm-inventory](https://github.com/MarketMasterPlus/mm-inventory)
- [mm-product](https://github.com/MarketMasterPlus/mm-product)
- [mm-shopping-cart](https://github.com/MarketMasterPlus/mm-shopping-cart)
- [mm-customer](https://github.com/MarketMasterPlus/mm-customer)
- [mm-store](https://github.com/MarketMasterPlus/mm-store)
- [mm-pact-broker](https://github.com/MarketMasterPlus/mm-pact-broker)
- [mm-ui](https://github.com/MarketMasterPlus/mm-ui)

For any further questions, feel free to open an issue on GitHub or consult the provided documentation within each repository.
