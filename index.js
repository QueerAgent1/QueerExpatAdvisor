// Import necessary modules and dependencies
const express = require('express');
// Add more imports as needed

// Create an instance of Express app
const app = express();

// Define routes and middleware
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

