const mongoose = require('mongoose');

let mongoMemoryServer = null;

const connectDB = async () => {
  try {
    let uri = process.env.MONGO_URI;

    if (!uri || uri.trim() === '' || uri === 'memory') {
      console.log('⚡  No external MONGO_URI found. Starting in-memory MongoDB server...');
      const { MongoMemoryServer } = require('mongodb-memory-server');
      mongoMemoryServer = await MongoMemoryServer.create({
        instance: { dbName: 'hungry_helm' }
      });
      uri = mongoMemoryServer.getUri();
      console.log('🧠  In-memory MongoDB instance started for local development.');
    }

    const conn = await mongoose.connect(uri);
    console.log(`✅  MongoDB connected: ${conn.connection.host}`);

    // Auto-seed if database is currently empty
    const Outlet = require('../models/Outlet');
    const outletCount = await Outlet.countDocuments();
    if (outletCount === 0) {
      console.log('🌱  Empty database detected — automatically seeding campus outlets & accounts...');
      const { seed } = require('./seed');
      await seed(false);
    }
  } catch (err) {
    console.error(`❌  MongoDB connection failed: ${err.message}`);
    process.exit(1);
  }
};

module.exports = connectDB;