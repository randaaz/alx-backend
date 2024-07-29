# 0x03. Queuing System in JS

## Project Overview
This project involves creating a basic queuing system using JavaScript, Node.js, Redis, and Kue. The project aims to provide hands-on experience with Redis operations, async handling, and implementing a queue system with Kue.

## Technologies Used
- JavaScript (ES6)
- Node.js
- Redis
- ExpressJS
- Kue

## Learning Objectives
By the end of this project, you should be able to:
1. Set up and run a Redis server on your machine.
2. Perform basic operations using the Redis client.
3. Integrate Redis with a Node.js application.
4. Store and manipulate hash values in Redis.
5. Handle async operations with Redis.
6. Use Kue as a queue system.
7. Develop a basic Express app interacting with Redis and Kue.

## Project Requirements
- All code should be compatible with Ubuntu 18.04, Node 12.x, and Redis 5.0.7.
- Include a `README.md` file at the root of the project.
- Use `.js` extension for JavaScript files.
- Ensure all files end with a newline.

## Project Setup
1. **Install Redis:**
   ```bash
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
   make
   src/redis-server &

