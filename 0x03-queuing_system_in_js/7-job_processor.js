import kue from 'kue';

// Create a function of blacklsted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notification
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Track progress of the job of 0 out of 100
  
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phnoe number ${phoneNumber} is blacklisted`)); // Fail the job with an error
  }

  job.progress(50, 100); // Track the progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  done(); // Complete the job
}

// Create a kue queue
const queue = kue.createQueue();

// Process jobs in the queue 'push_notification_code_2' with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
