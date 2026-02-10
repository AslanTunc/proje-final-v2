# Online Restaurant Menu Project

## Description
This is a web application for managing a digital restaurant menu. I developed this project using **Django** for the backend. It allows restaurant owners to add new food items, change prices, and upload images. The application is hosted on **Microsoft Azure**.

## Requirements Checklist

### Hard Requirements
- **Framework:** The application is written in Django.
- **Hosting:** It runs on Azure App Service.
- **Database:** It uses Azure SQL Database to store menu information.
- **Configuration:** Database credentials and secrets are read from environment variables (not hardcoded).

### Soft Requirements
- **CRUD Operations:** Users can Create, Read, Update, and Delete menu items.
- **File Storage:** Food images are stored in **Azure Blob Storage**.
- **Automation:** The project is set up to deploy automatically to Azure via GitHub Actions.

## Tech Stack
- Python / Django
- Azure App Service
- Azure SQL Database
- Azure Blob Storage