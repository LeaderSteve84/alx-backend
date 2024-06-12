import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * sets a new key-value pair
 * @param {string} schoolName - key to set in Redis
 * @param {string} value - The value to set for the key
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Display the value of a key from Redis
 * @param {string} schoolName - The key to retrieve from Redis
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.get(`Error: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
