import kue from 'kue';

// Create a kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message',
};

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log(`Error creating job:`, err);
    }
  });

// Handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
