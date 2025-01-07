# Introduction

This project is a demonstration of how to integrate Django with Amazon S3 for media file storage. It provides a basic setup to get you started with storing and serving media files using S3.

## Getting Started

### Prerequisites

- Python 3.x
- Django >= 4.2
- AWS account with S3 access

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/charlesu49/django_s3_demo.git
   cd django_s3_demo
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up your AWS credentials and S3 bucket information in the `.env` file:

   ```env
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_STORAGE_BUCKET_NAME=your_bucket_name
   ```

5. Apply migrations and start the development server:

   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000` to see the application in action.
