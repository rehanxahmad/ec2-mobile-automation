# API Gateway Setup Notes

1. Create HTTP API (not REST API) in API Gateway.
2. Add two routes:
   - POST /start → Lambda: StartEC2Instance
   - POST /stop → Lambda: StopEC2Instance
3. Enable "API Key required" for both routes.
4. Create an API Key and Usage Plan, associate both.
5. Deploy the API and test using curl/Postman/Shortcut.

Required Header:
x-api-key: YOUR_API_KEY