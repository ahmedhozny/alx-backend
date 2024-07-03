import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()
  .on('error', err => console.log('Redis client not connected to the server:', err))
  .on('connect', () => console.log('Redis client connected to the server'));


const updateHash = (hashName, fieldName, fieldValue) => {
  client.hset(hashName, fieldName, fieldValue, print);
};


const printHash = (hashName) => {
  client.hgetall(hashName, (_err, reply) => console.log(reply));
};


const hashObj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};
for (const [field, value] of Object.entries(hashObj)) {
  updateHash('HolbertonSchools', field, value);
}
printHash('HolbertonSchools');
