# 🚀 DevOps & Backend Challenge: Legacy Migration

**Submission Deadline:** 12pm. Nov 30, 2025.
**Total Score:** 100

## 📝 Scenario

We have a legacy inventory script that currently stores data in a static JSON file. We need to modernize this by moving it to a real database, wrapping it in a REST API, and deploying it behind a robust web server.

## 🛠 Prerequisites

  * **OS:** WSL (Ubuntu/Debian) or a Standard Linux VM.
  * **Language:** Python (FastAPI/Flask) OR Node.js (Express).
  * **Tools:** Nginx, SQLite/PostgreSQL, git.

## 📂 Repository Contents

  * `inventory.json` and `categories.json`: Current static data.
  * `lib.py`: Contains critical business logic for pricing. **You must use this.**

-----

## 🎯 Objectives

### 1\. Environment & Database (30 Marks)

  * Setup a proper project environment (virtualenv for Python or correct package.json for Node).
  * Write a migration script to move data from `inventory.json` into a SQL database (SQLite is acceptable).
  * **Deliverable:** A database file (or schema) populated with the JSON data.

### 2\. REST API Development (20 Marks)

Create a web server (running on `localhost:8000`) with the following endpoints:

  * `GET /api/products`: Return all products from the database.
  * `POST /api/order`: Accept `{"product_id": 1, "quantity": 2}`.
      * **Constraint:** You must use the logic inside `lib.py` to calculate the price.
      * Update the stock in the database (decrement quantity).
      * Return the total price calculated by the legacy library.

### 3\. Nginx Reverse Proxy (20 Marks)

  * Install and configure **Nginx** to listen on Port 80.
  * Configure Nginx to proxy requests from `http://localhost/api/...` to your application running on `http://localhost:8000`.
  * Direct traffic should go through Nginx, not directly to the app port.

### 4\. Service Reliability (20 Marks)

  * The application must **not** run in a foreground terminal tab.
  * Create a **systemd unit file** (or use PM2) to ensure the application runs in the background and restarts automatically if the server reboots or crashes.

### 5\. Public Access (10 Marks)

  * Expose your local Nginx server to the public internet securely.
  * Use **ngrok**, **Cloudflare Tunnel**, or a similar tool.
  * **Deliverables:** A public URL (e.g., `https://xyz.ngrok.io/api/products`) that serves your API.

### 6\. Submission Requirements

  * Create a github repo of your submission. Make it publicly available.
  * Email the link to your repo to **gridplexdigital@gmail.com**. Subject of email must have your name and roll number.
  * Please create a folder named `screenshots/` in your repo for images. 
**Failure to provide these may result in a deduction of marks.**

   1.  **`db_proof.png`**: A terminal screenshot running a SQL query that JOINs the `products` and `categories` tables to show data was migrated successfully.
   2.  **`logic_proof.png`**: A `curl` or Postman screenshot of a POST request to `/api/order` showing the calculated total price.
   4.  **`service_status.png`**: A screenshot of `systemctl status your-service`.
   5.  **`browser_proof.png`**: A screenshot of your web browser visiting your public (ngrok/tunnel) URL.
   6.  **Code:** detailed `server` code and `migration` scripts.
   7.  **Config:** Include your Nginx configuration file (usually in `/etc/nginx/sites-available`).
   8.  **Live Link:** Provide a screenshot of Postman/cURL usage with the live link using ngrok or similar.

**Good Luck\!**

