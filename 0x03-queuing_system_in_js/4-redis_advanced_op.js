import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create hash with key-value pairs
const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

// Store each key-value pair in the hash HolbertonSchools
for (const [key, value] of Object.entries(schools)) {
  client.hset('HolbertonSchools', key, value, print);
}

// Retrieve and display the hash
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.log(`Error: ${err.message}`);
  } else {
    console.log(result);
  }
});
