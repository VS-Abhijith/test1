# Python Vercel API

This project is a simple Python application deployed on Vercel that exposes an API endpoint. The API returns a JSON response containing the marks of specified names in the order requested. It also supports CORS for GET requests from any origin.

## Project Structure

```
python-vercel-api
├── api
│   └── index.py
├── requirements.txt
└── README.md
```

## API Endpoint

The API endpoint is defined in `api/index.py`. It handles GET requests and retrieves the names from the query parameters. The response is a JSON object containing the marks of the requested names.

### Example Request

```
GET /api?names=name1,name2,name3
```

### Example Response

```json
{
    "results": [
        {"name": "name1", "marks": 45},
        {"name": "name2", "marks": 67},
        {"name": "name3", "marks": 89}
    ]
}
```

## CORS Support

CORS is enabled for all origins, allowing the API to be accessed from any domain.

## Deployment Instructions

1. Ensure you have the Vercel CLI installed. If not, you can install it using npm:

   ```
   npm install -g vercel
   ```

2. Navigate to the project directory:

   ```
   cd python-vercel-api
   ```

3. Deploy the application to Vercel:

   ```
   vercel
   ```

4. Follow the prompts to complete the deployment.

## Usage

After deployment, you can access the API endpoint using the provided URL. Make sure to include the `names` query parameter to retrieve the corresponding marks.